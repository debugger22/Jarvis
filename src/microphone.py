import os
import sys
import wave
import tempfile
import pyaudio
from array import array
from struct import pack

THRESHOLD = 2000
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
SILENCE_DURATION = 40
WAIT_DURATION = 500
SPEECH_DURATION = 300

class Microphone:
	"""
	This class uses PyAudio to record on terminal
	"""
	def __init__(self):
		self.recordedWavFilename = ""

	def listen(self):
		(_, rec_wav_filename) = tempfile.mkstemp('.wav')

		sample_width, data = self.record()
		s_data = data[:]
		data = pack('<' + ('h'*len(data)), *data)
		wf = wave.open(rec_wav_filename, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(sample_width)
		wf.setframerate(RATE)
		wf.writeframes(b''.join(data))
		wf.close()

		self.recordedWavFilename = rec_wav_filename
		return self.recordedWavFilename,s_data

	def rate(self):
		return RATE

	def filename(self):
		return self.recordedWavFilename

	def housekeeping(self):
		os.remove(self.recordedWavFilename)

	def is_silent(self, sound_data):
		return max(sound_data) < THRESHOLD

	def add_silence(self, sound_data, seconds):
		r = array('h', [0 for i in xrange(int(seconds*RATE))])
		r.extend(sound_data)
		r.extend([0 for i in xrange(int(seconds*RATE))])
		return r

	def record(self):
		p = pyaudio.PyAudio()
		stream = p.open(format = FORMAT,
						channels = CHANNELS, 
						rate = RATE, 
						input = True, 
						frames_per_buffer = CHUNK)
		sys.stdout.write("Jarvis is listening...")

		speech_started = False
		speech = 0
		silence_before_speech = 0
		silence_after_speech = 0
		r = array('h')

		while 1:
			sound_data = array('h', stream.read(CHUNK))
			if sys.byteorder == 'big':
				sound_data.byteswap()
			r.extend(sound_data)

			silent = self.is_silent(sound_data)

			if speech_started:
				if silent:
					silence_after_speech += 1
				elif not silent:
					silence_after_speech = 0
					speech += 1

				if silence_after_speech > SILENCE_DURATION:
					break
				if speech > SPEECH_DURATION:
					break
			else: 
				if silent:
					silence_before_speech += 1
				elif not silent: 
					speech_started = True
				if silence_before_speech > WAIT_DURATION:
					break
		sys.stdout.write("Processing...")
		sample_width = p.get_sample_size(FORMAT)
		stream.stop_stream() 
		stream.close()
		p.terminate()
		r = self.add_silence(r, 0.5)
		return sample_width, r
