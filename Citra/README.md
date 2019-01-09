# Pengantar Pengolahan Citra

- [Pengantar Pengolahan Citra](#pengantar-pengolahan-citra)
  - [Penggunaan](#penggunaan)
  - [Main.m](#mainm)
    - [ImageMenu.m](#imagemenum)
    - [SmoothMenu.m](#smoothmenum)
      - [Mean.m](#meanm)
      - [LowPass.m](#lowpassm)
      - [Median.m](#medianm)

## Penggunaan

Pada `Command Window` MATLAB, ketikkan perintah berikut.

```
    >> Main
```

## Main.m

berisi perintah untuk memanggil `ImageMenu.m` dan dilanjutkan dengan `SmoothMenu.m`.

### ImageMenu.m

berisi perintah untuk menampilkan menu untuk memuat gambar `img`. Terdapat dua pilihan, mengunduh gambar dari alamat url atau menggunakan gambar yang sudah ada.

```
    ==== Smoothing Program ====
    1. Save image from url
    2. Read image from folder
    0. Exit
    ==========================
    Command:

```

### SmoothMenu.m

perintah ini sebaiknya dilakukan ketika variabel gambar `img` diisi dan terlihat pada bagian `WORKSPACE` di MATLAB. Berisi menu yang terdiri dari beberapa filter untuk proses pelembutan gambar (_Smoothing_), diantaranya: _Low Pass_, _Mean_, dan _Median_.

```
    ==== Smoothing Filter ====
    1. Mean filter
    2. Low Pass filter
    3. Median filter
    0. Exit
    ==========================
    Command:

```

#### Mean.m

di awal dijalankan, program akan meminta pengguna untuk memasukkan ukuran dari matriks filter `Z(i x j)`.

#### LowPass.m

di awal dijalankan, program akan meminta pengguna untuk memasukkan matriks filter `Z`. Syarat filter Low Pass adalah jumlah dari semua anggota elemen `Z` harus sama dengan 1, sehingga jika tidak memenuhi syarat program tidak akan diteruskan.

#### Median.m

di awal dijalankan, program akan meminta pengguna untuk memasukkan ukuran dari matriks filter `Z(i x j)`.
