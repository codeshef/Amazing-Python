
<!Doctype html>
<html>
<head>
<body>
<h1><center>Amazing Python</center></h1>
<h3>Text to Speech conversion</h3>
We can make the computer speak with Python.
Given a text string, it will speak the written words in the English language.
This process is called Text To Speech (TTS).
<h3> Pyttsx text to speech</h3>
Pyttsx is a cross-platform text-to-speech wrapper.
It uses different speech engines based on your operating system
<h4>Install with pip :sudo pip install pyttsx </h4>
Here we use pyttsx but there are several other options:
<li>using GTTS module</li>
<li>using ios TTS and speech recognition</li>
<li>Microsoft speech engine</li>
<li>IBM Watson TTS</li>

<h3>Speech Recognition in Python using Google Speech API</h3>
Speech recognition is the process of converting spoken words to text. Python supports many speech recognition engines and APIs, including Google Speech Engine, Google Cloud Speech API,
Microsoft Bing Voice Recognition and IBM Speech to Text.
Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc. This article aims to provide an introduction on how to make use of the SpeechRecognition library of Python. This is useful as it can be used on microcontrollers such as Raspberri Pis with the help of an external microphone.
<h4>Required installations</h4>
The following must be installed:
<h4>1.Python Speech Recognition module:</h4>
sudo pip install SpeechRecognition 
<h4>2.PyAudio:</h4>
Use the following command for linux users
sudo apt-get install python-pyaudio python3-pyaudio
If the versions in the repositories are too old, install pyaudio using the following command

sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && 
sudo pip install pyaudio

Use pip3 instead of pip for python3.
Windows users can install pyaudio by executing the following command in a terminal

pip install pyaudio

<h4>Speech Recognition demo</h4>
You can test the speech recognition module, with the command:

python -m speech_recognition
 

</body>
</head>
</html>
