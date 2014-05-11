from src import google_tts
import os
import random
speak_engine = google_tts.Google_TTS()

UHOH_PATH = "wav/uhoh/"
uhoh_files = os.listdir(UHOH_PATH)


def uhoh():
    '''
    This method will play pre-recorded uhoh wav files
    '''
    speak_engine.play_wav(
        UHOH_PATH +
        random.choice(uhoh_files)
    )

SORRY_PATH = "wav/sorry/"
sorry_files = os.listdir(SORRY_PATH)


def sorry():
    '''
    This method will play pre-recorded sorry wav files
    '''
    speak_engine.play_wav(
        SORRY_PATH +
        random.choice(sorry_files)
    )

SLEEPY_PATH = "wav/sleepy/"
sleepy_files = os.listdir(SLEEPY_PATH)


def sleepy():
    '''
    This method will play pre-recorded sleepy wav files
    '''
    speak_engine.play_wav(
        SLEEPY_PATH +
        random.choice(sleepy_files)
    )
