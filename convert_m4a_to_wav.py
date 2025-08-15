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
            subprocess.run([
                ffmpeg_path, "-y", "-i", m4a_path, wav_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"✅ Конвертировано: {m4a_path} → {wav_path}")