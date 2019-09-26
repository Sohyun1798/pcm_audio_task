import wave
import subprocess

def amr2wav(wav_path, amr_path, amr_file):

    wave_file = amr_file.replace(".amr", ".wav")

    amr_file_path = amr_path + amr_file
    wave_file_path = wav_path + wave_file

    subprocess.call('ffmpeg -i %s -ar 16000 %s' % (amr_file_path, wave_file_path), shell=True)

def mp32wav(wav_path, mp3_path, mp3_file):

    wave_file = mp3_file.replace(".mp3", ".wav")

    mp3_file_path = mp3_path + mp3_file
    wave_file_path = wav_path + wave_file

    subprocess.call('ffmpeg -i %s -acodec pcm_s16le -ac 1 -ar 16000 %s' % (mp3_file_path, wave_file_path), shell=True)

def wav2pcm(pcm_path, wav_path, wave_file):

    wav_file_path = wav_path + wave_file
    stream = wave.open(wav_file_path, "rb")

    sample_width = stream.getsampwidth()
    num_frames = stream.getnframes()

    sample_rate = stream.getframerate()
    raw_data = stream.readframes(num_frames)

    stream.close()

    if sample_width == 1 or sample_width ==2:
        oFilename = wave_file.replace(".wav", ".pcm")

        pcm_file_path = pcm_path + oFilename
        f = open(pcm_file_path, "wb")
        f.write(raw_data)
        f.close()

    else:
        raise ValueError("Error in " + wave_file + " Only supports 8 and 16 bit audio formats.")


