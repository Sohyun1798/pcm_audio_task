import argparse
import ac_utils
import os

# flags for converting
parser = argparse.ArgumentParser(description = "Enter the mode, path for .amr folder(if you need), .wav folder and .pcm folder")
parser.add_argument("mode", choices = ['amr2pcm', 'mp32pcm', 'wav2pcm'])
parser.add_argument("-ap", "--amrpath", default = "")
parser.add_argument("-mp", "--mp3path", default = "")
parser.add_argument("-wp", "--wavpath", default = "")
parser.add_argument("-pp", "--pcmpath", default = "")
args = parser.parse_args()

if args.mode == 'amr2pcm':

    amr_directory = os.fsencode(args.amrpath)

    for amr_file in os.listdir(amr_directory):
        amr_file = amr_file.decode('utf-8')
        if amr_file.endswith(".amr"):
            ac_utils.amr2wav(args.wavpath, args.amrpath, amr_file)
        else:
            continue

    wav_directory = os.fsencode(args.wavpath)

    for wav_file in os.listdir(wav_directory):
        wav_file = wav_file.decode('utf-8')
        if wav_file.endswith(".wav"):
            ac_utils.wav2pcm(args.pcmpath, args.wavpath, wav_file)
        else:
            continue

        wav_file_path = args.wavpath + wav_file
        os.remove(wav_file_path)

elif args.mode == 'mp32pcm':

    mp3_directory = os.fsencode(args.mp3path)

    for mp3_file in os.listdir(mp3_directory):
        mp3_file = mp3_file.decode('utf-8')
        if mp3_file.endswith(".mp3"):
            ac_utils.mp32wav(args.wavpath, args.mp3path, mp3_file)
        else:
            continue

    wav_directory = os.fsencode(args.wavpath)

    for wav_file in os.listdir(wav_directory):
        wav_file = wav_file.decode('utf-8')
        if wav_file.endswith(".wav"):
            ac_utils.wav2pcm(args.pcmpath, args.wavpath, wav_file)
        else:
            continue

        wav_file_path = args.wavpath + wav_file
        os.remove(wav_file_path)

else:

    wav_directory = os.fsencode(args.wavpath)

    for wav_file in os.listdir(wav_directory):
        wav_file = wav_file.decode('utf-8')
        if wav_file.endswith(".wav"):
            ac_utils.wav2pcm(args.pcmpath, args.wavpath, wav_file)
        else:
            continue
