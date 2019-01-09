# Pengantar Pengolahan Citra

- [Pengantar Pengolahan Citra](#pengantar-pengolahan-citra)
  - [Penggunaan](#penggunaan)
  - [Main](#main)
    - [ImageMenu](#imagemenu)
    - [SmoothMenu](#smoothmenu)
      - [Mean](#mean)
      - [LowPass](#lowpass)
      - [Median](#median)

## Penggunaan

```
    >> Main
```

## Main

berisi perintah untuk memanggil `ImageMenu` dan dilanjutkan dengan `SmoothMenu`.

### ImageMenu

berisi perintah untuk menampilkan menu untuk memuat gambar `img`. Terdapat dua pilihan, mengunduh gambar dari alamat url atau menggunakan gambar yang sudah ada.

```
    ==== Smoothing Program ====
    1. Save image from url
    2. Read image from folder
    0. Exit
    ==========================
    Command:

```

### SmoothMenu

menu dipanggil setelah gambar `img` diisi. Berisi menu yang terdiri dari beberapa filter untuk proses pelembutan gambar (_Smoothing_), diantaranya: _Low Pass_, _Mean_, dan _Median_.

```
    ==== Smoothing Filter ====
    1. Mean filter
    2. Low Pass filter
    3. Median filter
    0. Exit
    ==========================
    Command:

```

#### Mean

di awal dijalankan, program akan meminta pengguna untuk memasukkan ukuran dari matriks filter `Z(i x j)`.

#### LowPass

di awal dijalankan, program akan meminta pengguna untuk memasukkan matriks filter `Z`. Syarat filter Low Pass adalah jumlah dari semua anggota elemen `Z` harus sama dengan 1, sehingga jika tidak memenuhi syarat program tidak akan diteruskan.

#### Median

di awal dijalankan, program akan meminta pengguna untuk memasukkan ukuran dari matriks filter `Z(i x j)`.
