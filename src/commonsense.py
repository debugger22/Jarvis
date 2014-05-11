from src import google_tts
import os
import random
speak_engine = google_tts.Google_TTS()

SORRY_PATH = "wav/sorry/"
sorry_files = os.listdir(SORRY_PATH)


def sorry():
    '''
    This method will play pre-recorded sorry wav files
    '''
    speak_engine.play_wav(
        SORRY_PATH +
        sorry_files[
            random.randint(
                0,
                len(sorry_files) -
                1)])

SLEEPY_PATH = "wav/sleepy/"
sleepy_files = os.listdir(SLEEPY_PATH)


def sleepy():
    '''
    This method will play pre-recorded sorry wav files
    '''
    speak_engine.play_wav(
        SLEEPY_PATH +
        sleepy_files[
            random.randint(
                0,
                len(sleepy_files) -
                1)])
