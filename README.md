Jarvis
======


How to use
---------
```
python jarvis.py
```

How does it work
---------------
* It uses Google's speech to text and text to speech engines to interact with the users.
* It uses ALICE's aiml set for most of the answers.
* It can open some website for you such as Google, Facebook, etc. Just say "Can you open twitter for me"
  and see the magic
* It can do basic mathematics
* It can search for information on Wikipedia. "Search Microsoft"
* It can tell about your current location. Say "Where am I" or "Where are we"
* It can play music(Not developed completely)


Dependencies
-----------

Dependencies can be installed by running this [pip](https://pypi.python.org/pypi/pip) command `sudo pip install -r requirements.txt`

1. BeautifulSoup (version 4)
2. [PyAIML](http://pyaiml.sourceforge.net/)
3. PyAudio
4. PyDub
5. Requests
6. PyYAML

Operating Systems
----------------
* Linux
    - `sudo apt-get install libjack-jackd2-dev portaudio19-dev` for PyAudio to install
* Mac
    - `brew install portaudio` for PyAudio to install
* Don't try on Windows, it won't work

