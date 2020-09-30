Jarvis
======


How to use (For Mac and linux)
---------
```
python jarvis.py
```

How to use(For Windows)
----------------
```
python main.py
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

Features for Windows 
-------------------------

* It can send emails for you.
* It can play music for you.
* It can do Wikipedia searches for you.
* It is capable of opening websites like Google, Youtube, etc., in a web browser.
* It is capable of opening your code editor or IDE with a single voice command.

Dependencies
-----------

Dependencies can be installed by running this [pip](https://pypi.python.org/pypi/pip) command `sudo pip install -r requirements.txt` (Not to be done for windows)

1. BeautifulSoup (version 4)
2. [PyAIML](http://pyaiml.sourceforge.net/)
3. PyAudio
4. PyDub
5. Requests
6. PyYAML
7. Pyttsx3  (Only for windows)
8. SpeachRecognition (Only for windows)
9. Wikipedia (Only for windows)

Operating Systems
----------------
* Linux
    - `sudo apt-get install libjack-jackd2-dev portaudio19-dev` for PyAudio to install
* Mac
    - `brew install portaudio` for PyAudio to install
* Windows with just some basic features (Not Fully Functioned)
```
pip install pyttsx3
```
In case you receive such errors: 
* No module named win32com.client
* No module named win32
* No module named win32api
run the following command and repeat the previous step:
```
pip install pypiwin32
```
Now as soon as the previous installation is complete run the next command:
```
pip install speechRecognition
```
Now as soon as the previous installation is complete run the next command:
```
pip install wikipedia
```


