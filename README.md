# Railway Puzzle Solver
### Implementasi Algoritma Backtracking dan Constraint Satisfaction Problem (CSP) untuk Menyelesaikan Puzzle Jalur Kereta

## 1. Deskripsi Proyek

**Railway Puzzle Solver** merupakan program berbasis Python yang dirancang untuk menyelesaikan puzzle penyusunan jalur kereta secara otomatis menggunakan algoritma Backtracking dengan pendekatan Constraint Satisfaction Problem (CSP).

Pada puzzle ini, pemain diberikan sebuah grid berukuran M × N yang harus diisi dengan berbagai jenis potongan rel. Setiap baris dan kolom memiliki angka petunjuk yang menunjukkan jumlah kotak yang harus berisi rel.

Selain itu, terdapat beberapa potongan rel yang posisinya sudah ditentukan sejak awal (hint). Potongan tersebut tidak boleh dipindahkan atau diubah jenisnya selama proses pencarian solusi.

Program bertujuan menemukan susunan rel yang memenuhi seluruh batasan jumlah kotak serta membentuk satu jalur kereta yang saling terhubung, tidak bercabang, dan memiliki tepat dua ujung pada tepi grid.

## 2. Latar Belakang Permasalahan

Puzzle jalur kereta merupakan permainan logika yang mengharuskan pemain menyusun berbagai potongan rel berdasarkan sejumlah petunjuk.

Pemain harus mempertimbangkan beberapa kondisi secara bersamaan, yaitu:
- Jumlah kotak yang harus berisi rel pada setiap baris.
- Jumlah kotak yang harus berisi rel pada setiap kolom.
- Posisi dan jenis rel yang sudah ditentukan sebagai hint.
- Kesesuaian sambungan antarpotongan rel.
- Keterhubungan seluruh rel agar membentuk satu jalur yang utuh.

Banyaknya kemungkinan kombinasi penempatan rel membuat penyelesaian secara manual membutuhkan ketelitian dan waktu.

Oleh karena itu, proyek ini mengimplementasikan algoritma pencarian yang mampu mengeksplorasi berbagai kemungkinan susunan rel secara sistematis, memeriksa batasan yang berlaku, dan membatalkan pilihan yang tidak dapat menghasilkan solusi.

## 3. Tujuan Proyek

Tujuan pengembangan Railway Puzzle Solver adalah:

1. Mengimplementasikan algoritma Backtracking untuk mencari solusi puzzle jalur kereta.
2. Menerapkan konsep Constraint Satisfaction Problem (CSP) dalam pemenuhan batasan baris, kolom, dan konektivitas rel.
3. Mempertahankan posisi serta jenis potongan rel yang diberikan sebagai hint.
4. Menghasilkan susunan rel yang membentuk satu jalur terbuka dengan dua ujung pada tepi grid.
5. Mengamati proses pencarian melalui jumlah state yang dieksplorasi oleh algoritma.

## 4. Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Bahasa pemrograman | Python |
| Algoritma utama | Backtracking |
| Pendekatan penyelesaian | Constraint Satisfaction Problem (CSP) |
| Struktur data | List, Dictionary, Set, Tuple |
| Antarmuka | Command Line Interface (CLI) |
| Library eksternal | Tidak diperlukan |

Program menggunakan fitur bawaan Python sehingga tidak memerlukan instalasi library tambahan.

## 5. Aturan dan Batasan Puzzle

Puzzle menggunakan grid berukuran M × N dengan aturan sebagai berikut.

### 5.1. Batasan Horizontal

Setiap baris memiliki angka target yang menunjukkan jumlah sel yang harus berisi rel.

Contoh:

Jika angka horizontal suatu baris adalah 4, maka tepat empat sel pada baris tersebut harus berisi potongan rel.

### 5.2. Batasan Vertikal

Setiap kolom memiliki angka target yang menunjukkan jumlah sel yang harus berisi rel.

Contoh:

Jika angka vertikal suatu kolom adalah 3, maka tepat tiga sel pada kolom tersebut harus berisi potongan rel.

### 5.3. Jenis Potongan Rel

Terdapat enam jenis potongan rel yang dapat digunakan:

| Kode | Simbol | Jenis Rel | Sambungan |
|---|---|---|---|
| 1 | ┌ | Belokan kiri atas | Kanan dan bawah |
| 2 | ┐ | Belokan kanan atas | Kiri dan bawah |
| 3 | └ | Belokan kiri bawah | Kanan dan atas |
| 4 | ┘ | Belokan kanan bawah | Kiri dan atas |
| 5 | ─ | Rel horizontal | Kiri dan kanan |
| 6 | │ | Rel vertikal | Atas dan bawah |

Setiap potongan rel memiliki tepat dua sambungan.

### 5.4. Hint

Hint merupakan potongan rel yang posisi dan jenisnya telah ditentukan sejak awal permainan.

Ketentuannya:
- Setiap hint memiliki koordinat baris dan kolom.
- Setiap hint memiliki salah satu dari enam jenis rel.
- Posisi hint tidak boleh berubah.
- Jenis rel pada hint tidak boleh diganti.
- Seluruh hint harus menjadi bagian dari jalur akhir yang ditemukan.

### 5.5. Konektivitas Jalur

Seluruh potongan rel harus membentuk satu jalur yang utuh dengan ketentuan:

1. Seluruh rel harus saling terhubung.
2. Tidak boleh terdapat rel yang terpisah dari jalur utama.
3. Tidak boleh terdapat percabangan.
4. Sambungan antarpotongan harus memiliki arah yang sesuai.
5. Jalur harus memiliki tepat dua ujung yang berada pada tepi grid.
6. Jalur tidak membentuk lintasan tertutup atau loop.

Kotak yang tidak ditempati rel akan dianggap sebagai sel kosong dan tidak menjadi bagian dari jalur.

## 6. Formulasi Masalah KKA

Permasalahan puzzle dirumuskan menggunakan pendekatan State Space Search dan Constraint Satisfaction Problem.

### 6.1. Initial State

Initial State merupakan kondisi awal sebelum algoritma melakukan pencarian.

Kondisinya terdiri atas:
- Grid berukuran M × N.
- Angka target horizontal setiap baris.
- Angka target vertikal setiap kolom.
- Posisi dan jenis hint yang telah ditentukan.

Sel yang tidak memiliki hint dianggap belum terisi.

### 6.2. State

State merupakan kondisi sementara grid ketika algoritma sedang menyusun jalur.

Setiap state menggambarkan:
- Posisi rel yang sudah ditempatkan.
- Jenis dan orientasi setiap rel.
- Jalur yang sudah terbentuk.
- Jumlah rel pada setiap baris dan kolom.

### 6.3. Action

Action merupakan tindakan yang dilakukan algoritma untuk membangun jalur.

Tindakan tersebut meliputi:
- Memilih arah pergerakan berikutnya.
- Menentukan jenis rel berdasarkan arah masuk dan arah keluar.
- Menempatkan rel pada sel yang sedang diproses.
- Melanjutkan pencarian ke sel berikutnya.
- Membatalkan penempatan rel apabila ditemukan kondisi yang tidak valid.

### 6.4. Goal State

Goal State merupakan kondisi ketika seluruh persyaratan puzzle telah terpenuhi.

Suatu grid dinyatakan sebagai solusi apabila:

1. Jumlah rel setiap baris sama dengan angka horizontal.
2. Jumlah rel setiap kolom sama dengan angka vertikal.
3. Seluruh hint telah digunakan pada posisi dan jenis yang benar.
4. Semua rel membentuk satu jalur yang saling terhubung.
5. Tidak terdapat percabangan atau rel terpisah.
6. Terdapat tepat dua ujung jalur pada tepi grid.

### 6.5. Constraints

Constraint merupakan batasan yang harus dipenuhi selama proses pencarian.

Constraint yang digunakan meliputi:

- **Row Constraint:** jumlah rel pada setiap baris tidak boleh melebihi target.
- **Column Constraint:** jumlah rel pada setiap kolom tidak boleh melebihi target.
- **Hint Constraint:** posisi dan jenis rel pada hint harus dipertahankan.
- **Connectivity Constraint:** setiap rel harus tersambung sesuai arah sambungannya.
- **Path Constraint:** jalur tidak boleh mengunjungi sel yang sama lebih dari satu kali dan tidak boleh membentuk percabangan.
- **Endpoint Constraint:** jalur harus memiliki tepat dua ujung yang berada di tepi grid.

## 7. Algoritma yang Digunakan

### 7.1. Backtracking

Backtracking merupakan algoritma pencarian yang mencoba berbagai kemungkinan solusi secara bertahap.

Apabila suatu pilihan tidak memenuhi batasan atau tidak dapat menghasilkan solusi, algoritma akan membatalkan pilihan tersebut dan mencoba alternatif lainnya.

Dalam proyek ini, Backtracking digunakan untuk:
1. Memilih titik awal pada tepi grid.
2. Menentukan arah pergerakan jalur.
3. Menentukan bentuk rel berdasarkan dua arah sambungan.
4. Memeriksa validitas penempatan rel.
5. Melanjutkan pencarian ke sel berikutnya.
6. Melakukan backtracking ketika ditemukan kondisi yang tidak valid.

### 7.2. Constraint Satisfaction Problem (CSP)

CSP merupakan pendekatan penyelesaian masalah berdasarkan variabel, domain, dan constraint.

Penerapannya pada Railway Puzzle Solver adalah:

**A. Variables**

Variabel berupa sel-sel pada grid yang akan ditempati oleh potongan rel.

**B. Domain**

Domain merupakan kemungkinan bentuk rel yang dapat ditempatkan pada suatu sel, yaitu:
- Belokan kiri atas.
- Belokan kanan atas.
- Belokan kiri bawah.
- Belokan kanan bawah.
- Horizontal.
- Vertikal.

**C. Constraints**

Constraint merupakan seluruh aturan puzzle, meliputi jumlah rel horizontal dan vertikal, kesesuaian hint, serta konektivitas jalur.

### 7.3. Connectivity Checking

Connectivity Checking digunakan untuk memeriksa kesesuaian sambungan antara rel yang ditempatkan.

Program menggunakan empat arah:
- U (Up): atas.
- D (Down): bawah.
- L (Left): kiri.
- R (Right): kanan.

Setiap jenis rel memiliki dua arah sambungan.

Sebagai contoh:
- Rel horizontal memiliki sambungan kiri dan kanan.
- Rel vertikal memiliki sambungan atas dan bawah.
- Rel belokan kiri atas memiliki sambungan kanan dan bawah.

Algoritma memastikan rel yang baru ditempatkan tersambung dengan rel sebelumnya dan tidak membentuk sambungan tambahan yang menyebabkan percabangan.

## 8. Alur Kerja Program

Proses penyelesaian puzzle dilakukan melalui tahapan berikut:

1. Program menerima ukuran grid dari pengguna.
2. Program menerima angka target horizontal.
3. Program menerima angka target vertikal.
4. Program menerima jumlah hint.
5. Untuk setiap hint, pengguna memasukkan posisi baris, kolom, dan jenis rel.
6. Program memvalidasi input dan memeriksa kesesuaian total angka horizontal dan vertikal.
7. Algoritma mencoba titik awal pada tepi grid.
8. Algoritma menentukan bentuk rel berdasarkan arah masuk dan arah keluar.
9. Program memeriksa constraint jumlah rel dan konektivitas.
10. Jika pilihan tidak valid, algoritma melakukan backtracking.
11. Jika jalur mencapai tepi grid dan seluruh constraint terpenuhi, solusi disimpan.
12. Program menampilkan grid hasil dan jumlah state yang dieksplorasi.

## 9. Struktur Program

Program utama disimpan dalam satu file Python.

```text
RailwayPuzzle/
│
└── main.py
```

Penjelasan bagian utama kode:

| Fungsi / Variabel | Kegunaan |
|---|---|
| `TRACK_TYPES` | Menyimpan jenis, simbol, dan arah sambungan rel |
| `DIRECTIONS` | Menentukan arah pergerakan |
| `OPPOSITE` | Menentukan arah kebalikan |
| `inside()` | Memeriksa apakah koordinat berada di dalam grid |
| `solve_puzzle()` | Menjalankan proses pencarian solusi |
| `counts_possible()` | Memeriksa kemungkinan pemenuhan jumlah rel |
| `hint_matches()` | Memeriksa kesesuaian jenis rel dengan hint |
| `adjacency_valid()` | Memeriksa sambungan dengan rel yang telah dikunjungi |
| `all_hints_visited()` | Memastikan seluruh hint telah digunakan |
| `dfs()` | Menjalankan pencarian jalur menggunakan Backtracking |

## 10. Cara Menjalankan Program

### 10.1. Persyaratan

Sebelum menjalankan program, pastikan:
- Python sudah terinstal.
- Terminal atau Command Prompt tersedia.
- File `main.py` sudah disimpan.

Tidak diperlukan instalasi library tambahan.

### 10.2. Menjalankan Program

Buka terminal pada folder proyek, kemudian jalankan:

```bash
py main.py
```

Alternatif:

```bash
python main.py
```

### 10.3. Memasukkan Ukuran Grid

Program akan meminta jumlah baris dan kolom.

Contoh:

```text
Jumlah baris: 6
Jumlah kolom: 7
```

Artinya, puzzle memiliki enam baris dan tujuh kolom.

### 10.4. Memasukkan Angka Horizontal

Masukkan angka target setiap baris dengan pemisah spasi.

Contoh:

```text
Angka horizontal: 4 4 6 5 1 1
```

Karena grid memiliki enam baris, harus terdapat enam angka horizontal.

### 10.5. Memasukkan Angka Vertikal

Masukkan angka target setiap kolom dengan pemisah spasi.

Contoh:

```text
Angka vertikal: 2 3 2 5 3 4 2
```

Karena grid memiliki tujuh kolom, harus terdapat tujuh angka vertikal.

### 10.6. Memasukkan Hint

Program meminta jumlah hint yang tersedia.

Contoh:

```text
Jumlah hint (0 jika tidak ada): 3
```

Kemudian, pengguna memasukkan koordinat dan jenis rel untuk setiap hint.

Contoh:

```text
=== HINT 1 ===
Baris: 2
Kolom: 7

Pilih jenis rel:
1. ┌ - Belokan kiri atas
2. ┐ - Belokan kanan atas
3. └ - Belokan kiri bawah
4. ┘ - Belokan kanan bawah
5. ─ - Rel horizontal
6. │ - Rel vertikal

Jenis rel (1-6 atau simbol): 2
```

Pengguna dapat memasukkan kode angka atau simbol rel secara langsung.

**Catatan:** Koordinat dimulai dari angka 1, bukan 0. Jadi, baris pertama adalah baris 1 dan kolom pertama adalah kolom 1.

Jika tidak terdapat hint, masukkan angka 0.

## 11. Contoh Penggunaan Program

Berikut merupakan contoh input berdasarkan puzzle berukuran 6 × 7.

### Input

```text
================================
      RAILWAY PUZZLE SOLVER
================================

Jumlah baris: 6
Jumlah kolom: 7

Angka horizontal: 4 4 6 5 1 1
Angka vertikal: 2 3 2 5 3 4 2

Jumlah hint (0 jika tidak ada): 3
```

Hint pertama:

```text
=== HINT 1 ===
Baris: 2
Kolom: 7
Jenis rel (1-6 atau simbol): 2
```

Hint kedua:

```text
=== HINT 2 ===
Baris: 3
Kolom: 1
Jenis rel (1-6 atau simbol): 2
```

Hint ketiga:

```text
=== HINT 3 ===
Baris: 6
Kolom: 4
Jenis rel (1-6 atau simbol): 6
```

### Proses Pencarian

Setelah seluruh input dimasukkan, program akan menampilkan:

```text
Sedang mencari solusi...
```

Algoritma kemudian melakukan pencarian berdasarkan batasan yang telah ditentukan.

### Output

Apabila solusi ditemukan, program menampilkan susunan grid dan status keberhasilan.

Contoh format output:

```text
========== HASIL PUZZLE ==========

[Grid hasil pencarian]

Solusi ditemukan!
Jumlah state dieksplorasi: [jumlah state]
```

Apabila tidak ditemukan solusi:

```text
========== HASIL PUZZLE ==========

Tidak ditemukan solusi yang memenuhi aturan.
Jumlah state dieksplorasi: [jumlah state]
```

Jumlah state menunjukkan banyaknya pemanggilan proses pencarian yang dilakukan algoritma.

## 12. Analisis Kompleksitas Algoritma

Analisis kompleksitas digunakan untuk memahami kebutuhan waktu dan ruang selama proses pencarian.

### 12.1. Time Complexity

Backtracking memiliki kemungkinan mengeksplorasi banyak kombinasi jalur.

Jika terdapat N sel pada grid, jumlah kemungkinan jalur sederhana dapat bertambah secara eksponensial terhadap ukuran grid.

Secara umum, batas atas kasar untuk pencarian lintasan sederhana dapat dinyatakan dalam bentuk:

O(N!)

Namun, kompleksitas aktual bergantung pada ukuran grid, posisi hint, dan constraint yang membatasi kemungkinan pencarian.

Pemeriksaan constraint membantu mengurangi jumlah kemungkinan yang perlu dieksplorasi.

### 12.2. Space Complexity

Program menggunakan beberapa struktur data:
- Grid untuk menyimpan susunan rel.
- Set untuk menyimpan sel yang telah dikunjungi.
- Dictionary untuk menyimpan arah sambungan.
- List untuk menyimpan jalur sementara.
- Stack rekursi untuk proses DFS.

Penyimpanan struktur grid dan informasi kunjungan membutuhkan O(N) ruang.

Kedalaman rekursi juga dapat mencapai O(N), karena setiap sel hanya dapat dikunjungi satu kali dalam satu jalur.

Dengan demikian, kebutuhan ruang keseluruhan bersifat linear terhadap jumlah sel grid, yaitu O(N).

### 12.3. Parameter Evaluasi

Beberapa parameter yang dapat digunakan untuk mengevaluasi performa program:

1. Jumlah state yang dieksplorasi.
2. Waktu eksekusi.
3. Ukuran grid.
4. Jumlah hint.
5. Keberhasilan menemukan solusi.

Parameter tersebut dapat digunakan untuk membandingkan performa algoritma pada puzzle dengan tingkat kesulitan berbeda.

## 13. Kelebihan dan Keterbatasan

### Kelebihan

1. Dapat menyelesaikan puzzle secara otomatis berdasarkan input pengguna.
2. Menggunakan Backtracking untuk mengeksplorasi kemungkinan jalur.
3. Memanfaatkan constraint untuk membatasi pencarian.
4. Mempertahankan posisi dan jenis rel yang diberikan sebagai hint.
5. Memeriksa kesesuaian sambungan rel.
6. Menampilkan jumlah state yang dieksplorasi sebagai salah satu indikator proses pencarian.

### Keterbatasan

1. Proses pencarian dapat menjadi lambat pada grid yang lebih besar karena banyaknya kemungkinan jalur.
2. Program menggunakan pencarian rekursif sehingga kedalaman rekursi bergantung pada panjang jalur.
3. Belum menggunakan optimasi heuristik khusus untuk menentukan titik awal atau arah pencarian yang paling menjanjikan.
4. Output masih berupa representasi simbol pada terminal, belum berupa visualisasi grid interaktif.
5. Program saat ini mencari satu solusi yang memenuhi constraint dan belum menyediakan fitur untuk menampilkan seluruh kemungkinan solusi.

## 14. Rencana Pengembangan

Beberapa pengembangan yang dapat dilakukan selanjutnya:

1. **Visualisasi Grid:** menampilkan hasil pencarian dalam bentuk grid yang lebih mudah dipahami.
2. **Optimasi Heuristik:** menentukan urutan pencarian yang lebih efisien.
3. **Analisis Performa:** membandingkan jumlah state dan waktu eksekusi pada berbagai ukuran grid.
4. **Multiple Solutions:** mengembangkan program agar dapat menemukan lebih dari satu solusi apabila tersedia.
5. **Antarmuka Pengguna:** membuat GUI agar pengguna dapat memasukkan puzzle tanpa melalui terminal.

## 15. Kesimpulan

Railway Puzzle Solver merupakan implementasi algoritma Backtracking dengan pendekatan Constraint Satisfaction Problem untuk menyelesaikan permasalahan penyusunan jalur kereta.

Permasalahan dimodelkan sebagai pencarian state dari kondisi awal menuju kondisi tujuan dengan memperhatikan berbagai constraint, seperti jumlah rel pada setiap baris dan kolom, posisi hint, serta konektivitas antarpotongan rel.

Melalui penerapan Backtracking, program dapat mencoba berbagai kemungkinan susunan jalur dan membatalkan pilihan yang tidak memenuhi batasan.

Proyek ini juga memberikan kesempatan untuk menganalisis bagaimana ukuran grid dan jumlah constraint memengaruhi proses pencarian serta performa algoritma.