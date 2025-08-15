import os
import numpy as np
import librosa
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Параметры
DATA_DIR = "data"  # Папка с подпапками аккордов

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def load_dataset(data_dir):
    X, y = [], []
    for chord_name in os.listdir(data_dir):
        chord_dir = os.path.join(data_dir, chord_name)
        if not os.path.isdir(chord_dir):
            continue
        for filename in os.listdir(chord_dir):
            if filename.endswith(".wav"):
                file_path = os.path.join(chord_dir, filename)
                try:
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(chord_name)
                except Exception as e:
                    print(f"Ошибка при обработке {file_path}: {e}")
    return np.array(X), np.array(y)

# Загрузка и обучение
X, y = load_dataset(DATA_DIR)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Оценка
y_pred = clf.predict(X_test)
print("\n📊 Отчёт по точности:")
print(classification_report(y_test, y_pred))

# Тестовая проверка
def predict_file(path):
    features = extract_features(path)
    pred = clf.predict([features])[0]
    print(f"\n🎵 Предсказанный аккорд для '{os.path.basename(path)}': {pred}")

# Пример использования:
# predict_file("test.wav")
