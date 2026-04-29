import numpy as np
import librosa
import soundfile as sf
from sklearn.decomposition import FastICA
from pydub import AudioSegment
import os


# Load MP3 audio
def load_audio(file1, file2):
    audio1, sr1 = librosa.load(file1, sr=None, mono=True)
    audio2, sr2 = librosa.load(file2, sr=None, mono=True)

    if sr1 != sr2:
        raise ValueError("Sample rates must match")

    # Trim to same length
    min_len = min(len(audio1), len(audio2))
    audio1 = audio1[:min_len]
    audio2 = audio2[:min_len]

    # Stack signals
    mixed = np.vstack((audio1, audio2)).T
    return mixed, sr1


# Apply ICA
def apply_ica(mixed):
    ica = FastICA(n_components=2)
    separated = ica.fit_transform(mixed)
    return separated


# Save as MP3
def save_as_mp3(sources, sr):
    # Temporary WAV files
    sf.write("temp1.wav", sources[:, 0], sr)
    sf.write("temp2.wav", sources[:, 1], sr)

    # Convert to MP3
    AudioSegment.from_wav("temp1.wav").export("source1.mp3", format="mp3")
    AudioSegment.from_wav("temp2.wav").export("source2.mp3", format="mp3")

    # Remove temp files
    os.remove("temp1.wav")
    os.remove("temp2.wav")


def main():
    file1 = "../mic1.mp3"
    file2 = "../mic2.mp3"

    print("Loading audio...")
    mixed, sr = load_audio(file1, file2)

    print("Running ICA...")
    sources = apply_ica(mixed)

    print("Saving MP3 outputs...")
    save_as_mp3(sources, sr)

    print("Done! Files saved as source1.mp3 and source2.mp3")


if __name__ == "__main__":
    main()