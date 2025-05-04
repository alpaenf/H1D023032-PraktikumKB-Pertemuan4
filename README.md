# 🎮 Sistem Pakar: Rekomendasi Aktivitas Saat Bosan

Halo! Ini adalah project sederhana sistem pakar yang saya buat untuk membantu merekomendasikan aktivitas yang bisa dilakukan saat merasa bosan. Sistem ini dibangun pakai **Python** (untuk GUI-nya) dan **Prolog** (untuk logika pakarnya) dengan bantuan library **PySWIP**.

---

## 🔧 Cara Kerja Singkat

1. Program akan menampilkan beberapa pertanyaan seputar apa yang kamu sukai (misal: suka hiburan, suka kegiatan tenang, dll).
2. Jawaban kamu akan disimpan sebagai preferensi.
3. Preferensi ini dikirim ke Prolog, lalu dianalisis dengan aturan yang sudah ditentukan.
4. Hasilnya adalah beberapa aktivitas yang direkomendasikan buat kamu lakukan.

---

## 📂 Struktur Folder

sistem-pakar-aktivitas/
├── gui.py # Tampilan utama dengan Tkinter
├── engine.py # Menghubungkan Python dengan Prolog
├── preferensi_mapping.py # Kumpulan pertanyaan dan kodenya
└── basis_pengetahuan.pl # Logika sistem pakar (aturan + fakta Prolog)

---

## ▶️ Cara Menjalankan

1. Pastikan Python dan SWI-Prolog sudah terinstal.
2. Install PySWIP (penghubung Python ke Prolog): pip install pyswip
3. Jalankan program dengan:
python gui.py

---

## 🧠 Contoh Pertanyaan

Beberapa contoh pertanyaan yang muncul di awal:
- Apakah kamu suka kegiatan yang tenang?
- Apakah kamu suka hiburan seperti nonton atau dengerin musik?
- Apakah kamu suka kegiatan yang aktif?

Tinggal pilih "Ya" atau "Tidak", dan sistem akan mencocokkan preferensimu dengan aktivitas yang paling cocok.

---

## 💬 Contoh Output

Kalau kamu jawab suka hiburan dan santai, sistem mungkin akan merekomendasikan:
Aktivitas yang direkomendasikan:
Menonton film
Mendengarkan musik
Tidur siang

---

## 👤 Tentang

Nama: Mukhammad Alfaen Fadillah  
Tugas Praktikum Sistem Pakar Semester 4  
Universitas Jenderal Soedirman

---
