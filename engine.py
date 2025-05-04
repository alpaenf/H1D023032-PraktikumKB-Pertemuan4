from pyswip import Prolog

# Inisialisasi dan muat basis pengetahuan Prolog
prolog = Prolog()
prolog.consult("aktivitas.pl")

def ambil_pertanyaan(kode_pertanyaan):
    query = f"pertanyaan({kode_pertanyaan}, Pertanyaan)"
    hasil = list(prolog.query(query))
    return hasil[0]['Pertanyaan'] if hasil else "Pertanyaan tidak ditemukan."

def simpan_preferensi(preferensi):
    prolog.assertz(f"preferensi({preferensi})")

def dapatkan_rekomendasi():
    hasil = list(prolog.query("rekomendasi(Aktivitas)"))
    return list(set([h['Aktivitas'] for h in hasil]))
