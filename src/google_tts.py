import os
import wave
import tempfile
import requests
from pydub import AudioSegment
import sys

if sys.platform == 'darwin':
    PLAYER = 'afplay %s'
else:
    PLAYER = 'aplay -q %s'


class Google_TTS:

    """
    This class uses Google's Text to Speech engine to convert passed text to a wav(audio) file
    """

    def say(self, text):
        """
        This method converts the passd text to wav an plays it
        """
        wav_file = self.__convert_text_to_wav(text)
        if not wav_file:
            return False
        self.play_wav(wav_file)
        os.remove(wav_file)

    def __convert_text_to_wav(self, text):
        """
        This is a private method to convert text to wav using Google's Text to Speech engine
        """
        (_, tts_mp3_filename) = tempfile.mkstemp('.mp3')
        r_url = "http://translate.google.com/translate_tts?ie=utf-8&tl=en&q=" + \
            text.replace(" ", "+")
        try:
            r = requests.get(r_url)
        except requests.exceptions.ConnectionError:
            os.remove(tts_mp3_filename)
            return False
        f = open(tts_mp3_filename, 'wb')
        f.write(r.content)
        f.close()
        (_, tts_wav_filename) = tempfile.mkstemp('.wav')
        sound = AudioSegment.from_mp3(tts_mp3_filename)
        sound.export(tts_wav_filename, format="wav")
        os.remove(tts_mp3_filename)
        return tts_wav_filename

    def play_wav(self, filename):
        """
        This method plays passed wav file using a terminal software called aplay
        """
        os.system(PLAYER % (filename,))
