import tkinter as tk
from tkinter import messagebox
from preferensi_mapping import pertanyaan_list
from engine import ambil_pertanyaan, simpan_preferensi, dapatkan_rekomendasi

class PakarAktivitasApp:
    def __init__(self, master):
        self.master = master
        master.title("Sistem Pakar: Rekomendasi Aktivitas Saat Bosan")
        master.configure(bg="#f2f2f2")
        master.geometry("500x300")
        master.resizable(False, False)

        self.index = 0
        self.preferensi = []

        self.label = tk.Label(master, text="Sistem Pakar Aktivitas", font=("Segoe UI", 20, "bold"), bg="#f2f2f2", fg="#333")
        self.label.pack(pady=(20, 5))

        self.sub_label = tk.Label(master, text="Jawab pertanyaan berikut untuk mendapatkan rekomendasi aktivitas.", 
                                  font=("Segoe UI", 10), bg="#f2f2f2", fg="#666")
        self.sub_label.pack()

        self.pertanyaan_label = tk.Label(master, text="", font=("Segoe UI", 12), wraplength=400, bg="#f2f2f2", fg="#000")
        self.pertanyaan_label.pack(pady=20)

        self.button_frame = tk.Frame(master, bg="#f2f2f2")
        self.button_frame.pack()

        self.yes_button = tk.Button(self.button_frame, text="👍 Ya", width=12, bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"),
                                    activebackground="#45a049", command=self.jawab_ya)
        self.yes_button.grid(row=0, column=0, padx=10)

        self.no_button = tk.Button(self.button_frame, text="👎 Tidak", width=12, bg="#f44336", fg="white", font=("Segoe UI", 10, "bold"),
                                   activebackground="#da190b", command=self.jawab_tidak)
        self.no_button.grid(row=0, column=1, padx=10)

        self.mulai_diagnosa()

    def mulai_diagnosa(self):
        self.index = 0
        self.preferensi = []
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index < len(pertanyaan_list):
            kode, _ = pertanyaan_list[self.index]
            pertanyaan = ambil_pertanyaan(kode)
            self.pertanyaan_label.config(text=pertanyaan)
        else:
            self.tampilkan_rekomendasi()

    def jawab_ya(self):
        _, pref = pertanyaan_list[self.index]
        self.preferensi.append(pref)
        simpan_preferensi(pref)
        self.index += 1
        self.tampilkan_pertanyaan()

    def jawab_tidak(self):
        self.index += 1
        self.tampilkan_pertanyaan()

    def tampilkan_rekomendasi(self):
        hasil = dapatkan_rekomendasi()
        if hasil:
            aktivitas = "\n• " + "\n• ".join(hasil)
            messagebox.showinfo("Rekomendasi Aktivitas", f"Berikut aktivitas yang cocok untuk kamu:\n{aktivitas}")
        else:
            messagebox.showinfo("Rekomendasi Aktivitas", "Maaf, tidak ditemukan aktivitas yang sesuai.")
        self.master.destroy()

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = PakarAktivitasApp(root)
    root.mainloop()
