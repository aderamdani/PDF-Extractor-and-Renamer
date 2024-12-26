# PDF Extractor and Renamer

PDF Extractor and Renamer adalah aplikasi desktop yang memungkinkan pengguna untuk mengekstrak halaman dari file PDF dan mengganti namanya berdasarkan input pengguna. Aplikasi ini dibangun menggunakan Python dan Tkinter, dengan antarmuka pengguna yang sederhana dan intuitif.

## Fitur

- **Ekstraksi Halaman PDF**: Ekstrak halaman dari file PDF dan simpan sebagai file PDF terpisah.
- **Penggantian Nama**: Ganti nama file PDF yang diekstrak berdasarkan daftar nama yang dimasukkan oleh pengguna.
- **Tema Gelap dan Terang**: Beralih antara mode gelap dan terang untuk kenyamanan pengguna.
- **Impor Nama**: Impor daftar nama dari file CSV atau Excel untuk memudahkan penggantian nama.
- **Unduh Template**: Unduh template CSV atau Excel untuk memudahkan pengguna dalam menyiapkan daftar nama.
- **Ikon Kustom**: Aplikasi dilengkapi dengan ikon kustom untuk branding yang lebih baik.

## Prasyarat

Sebelum menjalankan aplikasi ini, pastikan Anda memiliki Python 3.x terinstal di sistem Anda. Anda juga perlu menginstal beberapa paket Python yang diperlukan.

## Instalasi

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/aderamdani/PDF-Extractor-and-Renamer.git
   cd PDF-Extractor-and-Renamer
   ```

2. **Instal Dependensi**:
   Anda dapat menginstal dependensi yang diperlukan dengan menggunakan pip. Jalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

   **Catatan**: Jika Anda tidak memiliki file `requirements.txt`, Anda dapat menginstal paket yang diperlukan secara manual:
   ```bash
   pip install PyPDF2 pandas openpyxl
   ```

## Cara Menggunakan

1. Jalankan aplikasi dengan perintah berikut:
   ```bash
   python main.py
   ```

2. Pilih file PDF yang ingin Anda ekstrak.
3. Tentukan direktori output untuk menyimpan file PDF yang diekstrak.
4. Masukkan daftar nama yang akan digunakan untuk mengganti nama file PDF.
5. Klik tombol "Start Extraction" untuk memulai proses ekstraksi dan penggantian nama.
6. Anda juga dapat mengimpor daftar nama dari file CSV atau Excel dan mengunduh template jika diperlukan.

## Rilis

Untuk melihat rilis terbaru dan mengunduh versi terbaru dari aplikasi, kunjungi [halaman rilis](https://github.com/aderamdani/PDF-Extractor-and-Renamer/releases).

## Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan fork repositori ini dan kirim pull request dengan perubahan Anda.

## Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

## Kontak

Jika Anda memiliki pertanyaan atau saran, silakan hubungi saya di [mr.aderamdani@gmail.com](mailto:mr.aderamdani@gmail.com).
```
