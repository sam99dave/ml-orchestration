import librosa
import soundfile
import os
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from constants import CONSTANT
import tqdm
from prefect import task


# Extract features (mfcc, chroma, mel) from a sound file
# @task
def extract_feature(file_name, mfcc=False, chroma=False, mel=False):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        result = np.array([])
        if mfcc:
            mfccs = np.mean(
                librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0
            )
            result = np.hstack((result, mfccs))
        if chroma:
            stft = np.abs(librosa.stft(X))
            chroma = np.mean(
                librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0
            )
            result = np.hstack((result, chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)  # type: ignore
            result = np.hstack((result, mel))
    return result


# Load the data and extract features for each sound  [ Flow ]
# @flow(log_prints = True)
@task
def load_data(
    test_size=0.2,
    data_path=CONSTANT["DATA_READ_PATH"],
    mfcc=True,
    chroma=True,
    mel=True,
):
    x, y = [], []
    for file in tqdm.tqdm(glob.glob(data_path)):
        file_name = os.path.basename(file)
        emotion = CONSTANT["EMOTIONS"][file_name.split("-")[2]]
        if emotion not in CONSTANT["OBSERVED_EMOTIONS"]:
            continue
        feature = extract_feature(file, mfcc, chroma, mel)
        x.append(feature)
        y.append(emotion)

    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)
