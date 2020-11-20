from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp

mp3_audio = AudioSegment.from_file('audio/test.mp3', format="mp3")

wname = mktemp('.wav')  # use temporary file
mp3_audio.export(wname, format="wav")
FS, data = wavfile.read(wname)

plt.specgram(data, Fs=FS, NFFT=128, noverlap=0)
plt.axis('off')
plt.savefig('spectrogram_image/test.png', bbox_inches='tight', transparent=True, pad_inches=0)
plt.show()

