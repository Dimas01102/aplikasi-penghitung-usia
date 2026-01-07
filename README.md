# 🎂 Aplikasi Penghitung Usia

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-success.svg)

---

## 🎯 Tentang Projek

**Aplikasi Penghitung Usia** adalah projek Akhir Akhir Semester (AAS) mata kuliah Algoritma dan Pemrograman. Aplikasi ini dirancang untuk menghitung usia pengguna secara detail dan akurat berdasarkan tanggal lahir.

### Mengapa Projek Ini Spesial?

✅ **Kompleksitas Tinggi** - Algoritma perhitungan tanggal yang kompleks  
✅ **OOP Implementation** - Struktur kode yang terorganisir dengan baik  
✅ **Error Handling** - Validasi input yang komprehensif  
✅ **UI Modern** - Interface yang user-friendly dan menarik  
✅ **Fitur Lengkap** - Lebih dari sekadar perhitungan usia dasar  

---

## ✨ Fitur

### 🎯 Fitur Utama

1. **Perhitungan Usia Akurat**
   - Menghitung usia dalam format: Tahun, Bulan, Hari
   - Menggunakan library `datetime` untuk akurasi tinggi
   - Menangani tahun kabisat secara otomatis

2. **Informasi Lengkap**
   - Total hari hidup sejak lahir
   - Countdown hari ke ulang tahun berikutnya
   - Tanggal ulang tahun yang akan datang
   - Zodiak berdasarkan tanggal lahir

3. **Validasi Input Komprehensif**
   - Validasi format tanggal
   - Pengecekan tanggal valid untuk setiap bulan
   - Penanganan 29 Februari untuk tahun kabisat
   - Mencegah input tanggal masa depan

4. **User Interface Profesional**
   - Design modern dengan warna-warna menarik
   - Layout yang rapi dan terorganisir
   - Dropdown menu untuk input yang mudah
   - Responsive dan user-friendly

---

## 📸 Screenshot

```
┌──────────────────────────────────────────────┐
│              🎂                              │
│     APLIKASI PENGHITUNG USIA                 │
│   Hitung usia Anda dengan akurat             │
└──────────────────────────────────────────────┘

┌─ 📅 Masukkan Tanggal Lahir ────────────────┐
│  Tanggal:  [-- Pilih Tanggal --       ▼]   │
│  Bulan:    [-- Pilih Bulan --         ▼]   │
│  Tahun:    [-- Pilih Tahun --         ▼]   │
└──────────────────────────────────────────────┘

     [🔢 HITUNG USIA]    [🔄 RESET]

┌─ 📊 Hasil Perhitungan ─────────────────────┐
│  🎂 USIA: 25 Tahun, 4 Bulan, 23 Hari       │
│  📊 Total Hari: 9,277 hari                 │
│  ⭐ Zodiak: Leo ♌                          │
└──────────────────────────────────────────────┘
```

---

## 🚀 Instalasi

### Persyaratan Sistem

- **OS**: Windows 7+, macOS 10.12+, Linux (Ubuntu 18.04+)
- **Python**: Versi 3.6 atau lebih tinggi
- **RAM**: Minimal 512 MB
- **Storage**: 50 MB ruang kosong

### Langkah Instalasi

#### 1. Install Python

**Windows:**
```bash
# Download dari python.org
# Centang "Add Python to PATH" saat instalasi
python --version
```

**macOS:**
```bash
brew install python3
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-tk
python3 --version
```

#### 2. Download Projek

Download dan extract file ZIP projek ini.

#### 3. Jalankan Setup

```bash
cd Aplikasi_Penghitung_Usia
python setup.py
```

Setup script akan:
- ✅ Mengecek versi Python
- ✅ Memverifikasi instalasi Tkinter
- ✅ Menguji import semua module
- ✅ Memberikan instruksi jika ada yang kurang

---

## 💻 Cara Menggunakan

### Menjalankan Aplikasi

#### Metode 1: Command Line
```bash
cd Aplikasi_Penghitung_Usia/src
python main.py
```

#### Metode 2: Double Click (Windows)
1. Buka folder `src`
2. Double-click `main.py`
3. Pilih "Open with Python"

### Cara Pakai Aplikasi

1. **Jalankan Aplikasi** - Window akan terbuka
2. **Input Tanggal Lahir**
   - Pilih Tanggal (1-31)
   - Pilih Bulan (Januari-Desember)
   - Pilih Tahun (dropdown otomatis)
3. **Klik "HITUNG USIA"** - Tombol hijau
4. **Lihat Hasil** - Hasil ditampilkan di area bawah
5. **Reset** (Opsional) - Klik tombol "RESET" untuk menghitung lagi

### Contoh Output

```
Input:  15 Agustus 2000
Output: 
  🎂 Usia: 25 Tahun, 4 Bulan, 23 Hari
  📊 Total Hari: 9,277 hari
  🎉 Ulang Tahun: 220 hari lagi (15 Agustus 2026)
  ⭐ Zodiak: Leo ♌
```

---

## 📁 Struktur Project

```
Aplikasi_Penghitung_Usia/
│
├── src/
│   └── main.py                 # File aplikasi utama
│
│
│
├── README.md                   # File ini
├── requirements.txt            # Dependencies (kosong - semua built-in)
└── LICENSE                     # Lisensi MIT
```

---

## 📚 Dokumentasi

### Dokumentasi Tersedia

1. **[FUNGSI_DAN_MODUL.md](docs/FUNGSI_DAN_MODUL.md)**
   - Penjelasan detail semua fungsi
   - Dokumentasi module & package
   - Algoritma dan complexity analysis

## 🛠️ Teknologi yang Digunakan

| Teknologi | Versi | Fungsi |
|-----------|-------|--------|
| Python | 3.6+ | Bahasa pemrograman utama |
| Tkinter | Built-in | Framework GUI |
| datetime | Built-in | Operasi tanggal dan waktu |
| calendar | Built-in | Utilitas kalender |

## 🎓 Konsep Pemrograman

### Yang Diimplementasikan

1. **Object-Oriented Programming (OOP)**
   - Class & Objects
   - Encapsulation
   - Methods & Attributes

2. **GUI Programming**
   - Event-driven programming
   - Widget management
   - Layout design

3. **Algoritma & Struktur Data**
   - Date calculations
   - Dictionary operations
   - String manipulation

4. **Error Handling**
   - Try-except blocks
   - Input validation
   - User feedback

---

## 👥 Tim Pengembang

**Projek AAS Algoritma dan Pemrograman**

- **Nama Tim**: [PBL-TRPL104-BM4]

**Program Studi**: Teknologi Rekayasa Perangkat Lunak (TRPL)  
**Kelas**: Malam  
**Tahun**: 2026  
**Dosen**: Gilang Bagus Ramadhan, A.Md. Kom

---

## 🔧 Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'tkinter'"

**Solusi:**
```bash
# Linux
sudo apt-get install python3-tk

# macOS
brew reinstall python3

# Windows
# Reinstall Python dengan opsi tcl/tk
```

### Problem: Window tidak muncul

**Solusi:**
1. Pastikan Python 3.6+ terinstall
2. Jalankan `python setup.py` untuk diagnosa
3. Cek apakah ada error message di terminal

### Problem: Error saat hitung usia

**Solusi:**
1. Pastikan semua field terisi
2. Pastikan tanggal valid (misal: 31 Februari = invalid)
3. Pastikan tanggal tidak di masa depan

---

## 📄 Lisensi

MIT License

Copyright (c) 2026 TEAM PBL-TRPL104-BM4

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 📞 Kontak & Dukungan

Jika ada pertanyaan atau menemukan bug:
- **GitHub**: [https://github.com/Dimas01102)]

<div align="center">

**Made with by TEAM PBL-TRPL104-BM4**

</div>
