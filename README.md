# audio_task

Actually, I'm not that kind of person who is good at explaning codes, programs, whatever(Screw me!😂). But anyways I'll do my best for describing what I made.

## 1. voice_recorder.py

* You need "pyaudio" to use this program. (maybe the command is "pip install pyaudio" but I can't remember well so recommand you searching through google.)
* And also need 'wave'. Anyways you should install it to use 'ac_utils.py'.
* After you run this code(with command window or pycharm whatever) the program will record your voice or sound if it's at certain frequency.
* And the program will end if it senses a period of silence.
* It will keep record sounds unless you press " control + c "

notice!) I revised certain codes on website to make this program so if there is any problem related to copyright or something, please let me know.

## 2. ac_utils.py

* Install 'wave' before you use this. (command: pip install wave)
* You need 'ffmpeg' also for using this. (Search google and install it appropriately according to your OS)
* And this file is a set of functions so only existence of the file is enough.

## 3. audioconverter.py

parser.add_argument("mode", choices = ['amr2pcm', 'mp32pcm', 'wav2pcm'])

parser.add_argument("-ap", "--amrpath", default = "")

parser.add_argument("-mp", "--mp3path", default = "")

parser.add_argument("-wp", "--wavpath", default = "")

parser.add_argument("-pp", "--pcmpath", default = "")

* You need directories before you run this code. And even though you don't actually work with .wav file( for instance, amr file to pcm file or mp3 file to pcm file), you need wav file directory because of the converting process.
* command: python audioconverter.py mode -ap amr_directory -mp mp3_directory -wp wav_directory -pp pcm_directory
* command example(wav file to pcm file): python audioconverter.py wav2pcm -wp m2w/ -pp m2p/
