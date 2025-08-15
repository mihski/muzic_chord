import os
import shutil
from sklearn.model_selection import train_test_split

# Папка с исходными аккордами
DATA_DIR = "data"  # внутри data папки Am, C, Dm, F, G и т.д.
TEST_SIZE = 0.2    # доля тестовой выборки

# Проходим по всем папкам с аккордами
for chord in os.listdir(DATA_DIR):
    chord_path = os.path.join(DATA_DIR, chord)
    if not os.path.isdir(chord_path):
        continue  # пропускаем файлы, если они есть

    # Создаём подпапки train и test внутри каждой папки аккорда
    train_dir = os.path.join(chord_path, "train")
    test_dir = os.path.join(chord_path, "test")
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Список всех файлов в папке аккорда
    files = [f for f in os.listdir(chord_path) if os.path.isfile(os.path.join(chord_path, f))]
    
    # Если файлов меньше 2, пропускаем деление (иначе ошибка)
    if len(files) < 2:
        print(f"Недостаточно файлов для аккорда {chord}, пропускаем.")
        continue

    # Разделяем на train и test
    train_files, test_files = train_test_split(files, test_size=TEST_SIZE, random_state=42)

    # Копируем файлы в соответствующие папки
    for f in train_files:
        shutil.copy(os.path.join(chord_path, f), os.path.join(train_dir, f))
    for f in test_files:
        shutil.copy(os.path.join(chord_path, f), os.path.join(test_dir, f))

    print(f"{chord}: {len(train_files)} файлов в train, {len(test_files)} файлов в test")