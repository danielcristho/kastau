# Panduan Kontribusi Data Kastau

Tujuan kami adalah menyajikan kebijakan asli yang kompleks ke dalam bahasa yang ramah warga Kabupaten Jayapura.

## Alur Kontribusi

1. **Pencarian Dokumen:** Cari PDF peraturan resmi di JDIH Kabupaten Jayapura atau BPK RI.
2. **Kategorisasi:** Masukkan ke dalam salah satu dari kategori berikut: `infrastruktur`, `pendidikan`, `kesehatan`, `lingkungan-hidup`, `ekonomi-umkm`, `adat-budaya`, `tata-ruang`, `hukum-peraturan`.
3. **Penyusunan Konten:**
    - **Ringkasan (Summary):** Maksimal 3 kalimat. Fokus pada inti kebijakan bagi masyarakat.
    - **Detail:** Penjelasan lebih teknis, misalnya cara daftar, persyaratan, atau konsekuensi hukum.
    - **Status:** Tentukan apakah aktif (`berlaku`), dicabut (`telah dicabut`), atau diubah (`direvisi`).

## Format Pengisian

Saat ini data dikumpulkan melalui file `apps/api/app/seed.py`.

```python
{
    "id": 1,
    "number": "Perda No. 3 Tahun 2024",
    "title": "Pengelolaan dan Perlindungan Hutan Adat",
    "category": "adat-budaya",
    "year": 2024,
    "date": "12 Maret 2024",
    "status": "berlaku",
    "type": "Perda",
    "summary": "Ringkasan manfaat kebijakan...",
    "detail": "Penjelasan detail...",
    "document_url": "link-peraturan-asli",
}
```

## Etika Penulisan

- Selalu cantumkan nomor dan tahun peraturan dengan benar.
- Gunakan bahasa yang objektif dan mudah dipahami.
- Hindari jargon hukum sejauh mungkin untuk bagian `summary`.
- Gunakan data resmi dari pemerintah sebagai satu-satunya rujukan.

Terima kasih atas kontribusi Anda dalam membuat kebijakan daerah lebih mudah diakses masyarakat!
