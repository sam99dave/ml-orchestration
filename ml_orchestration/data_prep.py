import librosa
import soundfile
import os
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from constants import CONSTANT
from prefect import task, flow


# Extract features (mfcc, chroma, mel) from a sound file
@task
def extract_feature(file_name, emotion, mfcc=False, chroma=False, mel=False):
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
    return [result, emotion]


# Load the data and extract features for each sound  [ Flow ]
@flow(log_prints=True)
def load_data(
    test_size=0.2,
    data_path=CONSTANT["DATA_READ_PATH"],
    mfcc=True,
    chroma=True,
    mel=True,
):
    x, y = [], []
    issues = []
    for file in glob.glob(data_path):
        file_name = os.path.basename(file)
        emotion = CONSTANT["EMOTIONS"][file_name.split("-")[2]]
        if emotion not in CONSTANT["OBSERVED_EMOTIONS"]:
            continue
        issues.append(extract_feature.submit(file, emotion, mfcc, chroma, mel))
        # print(f'len issues: {len(issues)}')
        # print(f'issues: {issues[0].result()}')
        x = [p.result()[0] for p in issues]
        y = [p.result()[1] for p in issues]

    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)
