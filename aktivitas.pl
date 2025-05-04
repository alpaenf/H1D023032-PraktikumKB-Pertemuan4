% Fakta: aktivitas dan kategori
aktivitas(membaca_buku, tenang).
aktivitas(menonton_film, hiburan).
aktivitas(bermain_game, hiburan).
aktivitas(berolahraga, aktif).
aktivitas(memasak, kreatif).
aktivitas(mendengarkan_musik, santai).
aktivitas(melukis, kreatif).
aktivitas(meditasi, tenang).
aktivitas(berjalan_jalan, aktif).
aktivitas(bermain_alat_musik, kreatif).

% Pertanyaan
pertanyaan(suka_kegiatan_tenang, 'Apakah Anda menyukai kegiatan yang tenang?').
pertanyaan(suka_hiburan, 'Apakah Anda menyukai hiburan seperti film atau game?').
pertanyaan(suka_kegiatan_aktif, 'Apakah Anda menyukai kegiatan fisik atau aktif?').
pertanyaan(suka_kegiatan_kreatif, 'Apakah Anda menyukai kegiatan kreatif seperti melukis atau memasak?').
pertanyaan(suka_kegiatan_santai, 'Apakah Anda menyukai kegiatan santai seperti mendengarkan musik?').

% Aturan rekomendasi
rekomendasi(Aktivitas) :-
    preferensi(tenang),
    aktivitas(Aktivitas, tenang).

rekomendasi(Aktivitas) :-
    preferensi(hiburan),
    aktivitas(Aktivitas, hiburan).

rekomendasi(Aktivitas) :-
    preferensi(aktif),
    aktivitas(Aktivitas, aktif).

rekomendasi(Aktivitas) :-
    preferensi(kreatif),
    aktivitas(Aktivitas, kreatif).

rekomendasi(Aktivitas) :-
    preferensi(santai),
    aktivitas(Aktivitas, santai).

% Preferensi dinamis
:- dynamic(preferensi/1).
