# PA_A3_Sistem-Penjualan-Merchandise-Komunitas

# Anggota dan Peran :
| Anggota | Peran |
| --- | --- |
| Salwa Annisa Nur Fadhila	(2609116010) | --- |
| Muhammad Favian Daffa	(2609116021) | --- |
| Mutiara Zyahra Al Gazali (2609116026) | --- |
| Fahry Alfisyahr Razak (2609116028) | --- |

# Sistem Penjualan Komunitas

Program Sistem Penjualan Merchandise BEM FT merupakan aplikasi berbasis Python yang dirancang untuk mempermudah pengelolaan dan penjualan merchandise. Program ini memiliki dua jenis pengguna, yaitu admin dan user, dengan hak akses yang berbeda. Admin dapat mengelola data barang melalui fitur tambah, lihat, ubah, dan hapus (CRUD), melihat data pengguna, memeriksa riwayat transaksi, serta melihat laporan penjualan. Sementara itu, user dapat melihat barang, melakukan top up saldo, membeli merchandise, dan melihat riwayat transaksi pribadi.

Proses pembelian dilakukan menggunakan saldo pengguna. Program akan memeriksa ketersediaan stok dan kecukupan saldo sebelum memproses pembayaran. Jika transaksi berhasil, saldo dan stok barang akan diperbarui, data transaksi disimpan, dan invoice ditampilkan sebagai bukti pembayaran. Program menggunakan Python dan file JSON untuk mengolah serta menyimpan data pengguna, barang, dan transaksi. Selain itu, program menerapkan fungsi, percabangan, perulangan, validasi input, dan penanganan kesalahan agar proses penjualan berjalan secara terstruktur.

# Flowchart

## Registrasi dan Login
   
   <img width="1732" height="1484" alt="FlowchartPAKel3-REGIS DAN LOGIN (1)" src="https://github.com/user-attachments/assets/cf1ab9a8-b744-4972-ab1e-928772321608" />

Flowchart registrasi dan login menjelaskan proses awal penggunaan program. Sistem menampilkan menu utama yang menyediakan pilihan registrasi, login, dan keluar. Pada proses registrasi, user memasukkan username dan kata sandi, kemudian sistem memeriksa kelengkapan serta kesesuaian data sebelum menyimpan akun ke dalam user.json.

Pada proses login, sistem mencocokkan data yang dimasukkan dengan data user yang tersimpan. Jika data sesuai, user diarahkan ke halaman berdasarkan perannya. Jika data tidak sesuai, sistem menampilkan pesan kesalahan dan memberikan kesempatan untuk mencoba kembali hingga batas percobaan yang ditentukan.

## CRUD

   <img width="2232" height="1090" alt="_FlowchartPAKel3-CRUD" src="https://github.com/user-attachments/assets/38b53588-e73f-4977-9974-8940de97173c" />

Flowchart pengelolaan barang menggambarkan proses yang dapat dilakukan admin untuk melihat, menambah, mengubah, dan menghapus data barang. Sistem membaca data dari barang.json sebelum menjalankan proses yang dipilih. Ketika admin melakukan perubahan, sistem menyimpan data terbaru ke dalam berkas tersebut.

Program juga melakukan pemeriksaan terhadap data yang dimasukkan, seperti ID barang dan informasi barang lainnya. Jika barang tidak ditemukan atau data tidak sesuai, sistem menampilkan pesan yang relevan.

## Halaman Admin

   <img width="1772" height="887" alt="_FlowchartPAKel3-Halaman Admin" src="https://github.com/user-attachments/assets/0d0094b0-af69-4197-8117-dd6c1041c926" />

Flowchart halaman admin menjelaskan pilihan menu yang tersedia setelah administrator berhasil login. Admin dapat mengelola barang, melihat data barang, memeriksa seluruh transaksi, menampilkan laporan penjualan, dan keluar dari akun.

Pada fitur laporan penjualan, sistem membaca data transaksi dari transaksi.json, kemudian menghitung informasi penjualan yang tersedia. Hasilnya ditampilkan agar admin dapat memantau pendapatan, jumlah transaksi pembelian, dan barang yang paling banyak terjual.

## Halaman User

<img width="2031" height="957" alt="FlowchartPAKel3-Halaman User (1)" src="https://github.com/user-attachments/assets/c778759f-8581-456f-9f21-e9b32d4c0a1e" />

Flowchart halaman user menjelaskan fitur yang dapat digunakan oleh user biasa. User dapat mengisi saldo, melihat daftar barang, membeli barang, melihat riwayat transaksi pribadi, dan keluar dari akun.

Dalam proses pembelian, sistem memeriksa ketersediaan stok dan kecukupan saldo. Jika persyaratan terpenuhi dan pembelian berhasil, sistem memperbarui saldo user, mengurangi stok barang, serta menyimpan transaksi. Jika stok atau saldo tidak mencukupi, sistem menampilkan pesan yang sesuai.


# Program

## 1. Apalah

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | user.json | Data akun user, password, peran, dan saldo |
| 2 | barang.json | Data merchandise yang mencakup ID, nama barang, harga, dan stok |
| 3 | transaksi.json | Riwayat transaksi, kode transaksi, username, jenis transaksi, detail, total pembayaran, waktu, dan sisa saldo |


## 2. Library

<img width="587" height="86" alt="image" src="https://github.com/user-attachments/assets/1dffd19d-7e9c-472c-9b4b-cc75cf45b9b2" />

<br>

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | os | Digunakan untuk membersihkan tampilan terminal melalui fungsi os.system("cls") agar menu program terlihat lebih rapi |
| 2 | time | Digunakan untuk memberikan jeda tampilan menggunakan time.sleep() dan mencatat waktu transaksi menggunakan time.strftime() |
| 3 | json | Digunakan untuk membaca dan menyimpan data user, barang, serta transaksi ke dalam file JSON agar data tetap tersimpan meskipun program ditutup |
| 4 | PrettyTable | Digunakan untuk menampilkan data barang, user, transaksi, dan invoice dalam bentuk tabel sehingga lebih mudah dibaca |
| 5 | pwinput | Digunakan untuk menyembunyikan karakter password ketika user melakukan registrasi atau login |
| 6 | random | Digunakan untuk menghasilkan nilai secara acak, misalnya untuk membuat kode atau nomor transaksi. |


**Funcion**

| No | Fungsi | Kegunaan |
| :--- | :---: | :---: |
| 1 | bersih() | Membersihkan tampilan terminal sebelum menu atau informasi baru ditampilkan |
| 2 | menu_utama() | Menampilkan menu utama yang berisi pilihan registrasi, login, dan keluar dari aplikasi |
| 3 | registrasi() | Memproses pembuatan akun baru dan menyimpan data user ke file user.json |
| 4 | login() | Memeriksa username dan password serta mengarahkan user ke menu sesuai dengan perannya |
| 5 | tampilkan_barang() | Menampilkan daftar merchandise beserta ID, nama, harga, dan stok barang |
| 6 | tambah_barang() | Menambahkan merchandise baru ke dalam daftar barang |
| 7 | ubah_barang() | Memperbarui nama, harga, atau stok barang yang sudah tersimpan |
| 8 | hapus_barang() | Menghapus barang berdasarkan ID yang dipilih setelah user mengonfirmasi penghapusan |
| 9 | menu_crud_barang() | Menampilkan menu pengelolaan barang yang mencakup tambah, lihat, ubah, dan hapus data |
| 10 | cetak_invoice() | Menampilkan bukti transaksi yang berisi kode transaksi, waktu, username, jenis transaksi, total pembayaran, dan sisa saldo |
| 11 | top_up() | Menambahkan saldo user dan mencatat transaksi pengisian saldo |
| 12 | beli_barang() | Memproses pembelian merchandise, menghitung total harga, memeriksa saldo, mengurangi stok, dan menyimpan transaksi |
| 13 | riwayat_transaksi() | Menampilkan riwayat transaksi, baik seluruh transaksi maupun transaksi milik user tertentu |
| 14 | laporan_admin() | Menghitung total pendapatan, jumlah transaksi pembelian, dan produk terlaris |
| 15 | tampilkan_users() | Menampilkan daftar user beserta peran dan saldo yang dimiliki |
| 16 | menu_admin() | Menampilkan menu khusus Admin untuk mengelola barang, melihat pengguna, memeriksa transaksi, dan melihat laporan penjualan |
| 17 | menu_user() | Menampilkan menu user untuk melihat barang, mengisi saldo, membeli barang, dan melihat riwayat transaksi |



# Daftar Fitur per Role

# Screenshot Output
