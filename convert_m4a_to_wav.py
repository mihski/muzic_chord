import os
import subprocess

# Папка с аккордами
base_dir = "data"

# Проходим по всем подпапкам
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(".m4a"):
            m4a_path = os.path.join(root, file)
            wav_path = os.path.splitext(m4a_path)[0] + ".wav"

            # Конвертация через FFmpeg
            ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
            result = subprocess.run(
                [ffmpeg_path, "-y", "-i", m4a_path, wav_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if result.returncode == 0:
                # Удаляем исходный файл .m4a после успешной конвертации
                os.remove(m4a_path)
                print(f"✅ Конвертировано и удалено: {m4a_path} → {wav_path}")
            else:
                print(f"❌ Ошибка при конвертации: {m4a_path}")