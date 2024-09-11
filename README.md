Berikut adalah script Python yang dapat digunakan untuk mengompresi (reduce) file audio .ogg secara batch menggunakan pustaka pydub. Script ini akan membaca semua file .ogg dalam folder tertentu, mengompresnya, dan menyimpan hasilnya dalam folder lain.

Pertama-tama, pastikan Anda sudah menginstal pustaka pydub dan ffmpeg:

bash
Copy code
pip install pydub
Anda juga memerlukan ffmpeg untuk mengonversi dan memproses file audio. Jika belum terinstal, Anda bisa mengunduh dan menginstalnya dari FFmpeg.org.

Penjelasan:
Folder Input dan Output: Pastikan untuk menyesuaikan input_folder dan output_folder sesuai dengan lokasi file audio Anda.
Bitrate: Default bitrate diatur menjadi 64k. Anda bisa menyesuaikannya sesuai kebutuhan Anda untuk pengompresan yang lebih agresif atau lebih ringan.
Pydub: Pydub digunakan untuk memproses file audio .ogg dan menghasilkan file .ogg terkompresi dengan bitrate yang lebih rendah.
