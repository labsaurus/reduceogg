import os
from pydub import AudioSegment

# Folder input dan output
input_folder = "audio"  # Ganti dengan folder tempat file .ogg berada
output_folder = "audioxx"  # Ganti dengan folder tempat hasil kompresi akan disimpan

# Pastikan folder output ada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Fungsi untuk mengompresi file audio
def compress_audio(input_file, output_file, bitrate="64k"):
    try:
        # Load file .ogg
        audio = AudioSegment.from_ogg(input_file)
        
        # Export dengan bitrate lebih rendah
        audio.export(output_file, format="ogg", bitrate=bitrate)
        print(f"File '{input_file}' berhasil dikompresi menjadi '{output_file}'")
    except Exception as e:
        print(f"Gagal mengompresi file '{input_file}': {e}")

# Proses semua file .ogg di folder input
for filename in os.listdir(input_folder):
    if filename.endswith(".ogg"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Kompres file audio
        compress_audio(input_path, output_path)

print("Proses kompresi selesai.")
