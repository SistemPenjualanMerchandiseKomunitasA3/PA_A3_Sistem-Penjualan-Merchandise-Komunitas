# PA_A3_Sistem-Penjualan-Merchandise-Komunitas

Program Sistem Penjualan Merchandise BEM FT merupakan aplikasi berbasis Python yang dirancang untuk mempermudah pengelolaan dan penjualan merchandise. Program ini memiliki dua jenis pengguna, yaitu admin dan user, dengan hak akses yang berbeda. Admin dapat mengelola data barang melalui fitur tambah, lihat, ubah, dan hapus (CRUD), melihat data pengguna, memeriksa riwayat transaksi, serta melihat laporan penjualan. Sementara itu, user dapat melihat barang, melakukan top up saldo, membeli merchandise, dan melihat riwayat transaksi pribadi.

Proses pembelian dilakukan menggunakan saldo pengguna. Program akan memeriksa ketersediaan stok dan kecukupan saldo sebelum memproses pembayaran. Jika transaksi berhasil, saldo dan stok barang akan diperbarui, data transaksi disimpan, dan invoice ditampilkan sebagai bukti pembayaran. Program menggunakan Python dan file JSON untuk mengolah serta menyimpan data pengguna, barang, dan transaksi. Selain itu, program menerapkan fungsi, percabangan, perulangan, validasi input, dan penanganan kesalahan agar proses penjualan berjalan secara terstruktur.


# Anggota dan Peran :
1. Salwa Annisa Nur Fadhila	(2609116010) :
2. Muhammad Favian Daffa	(2609116021) :
3. Mutiara Zyahra Al Gazali (2609116026) :
4. Fahry Alfisyahr Razak (2609116028) :

# Deskripsi dan Tujuan

Program Sistem Penjualan Merchandise BEM FT merupakan program berbasis Python yang digunakan untuk mengelola penjualan merchandise secara sederhana. Program ini memiliki beberapa fitur, seperti registrasi akun, login, pengelolaan barang, pembelian barang, pengisian saldo, pencatatan transaksi, dan pembuatan laporan penjualan. Untuk membuat program ini, diperlukan beberapa library, fungsi, struktur data, dan file penyimpanan agar setiap fitur dapat berjalan sesuai dengan kebutuhan.

**Fitur**
- Menu utama yang menampilkan pilihan login, registrasi, dan keluar. Program memproses pilihan pengguna dan menampilkan pesan jika pilihan tidak valid.

- Registrasi akun baru dengan validasi nama pengguna dan kata sandi. Nama pengguna tidak boleh kosong, harus memenuhi panjang minimum, dan tidak boleh sama dengan nama pengguna yang sudah terdaftar. Kata sandi juga harus memenuhi ketentuan program.

- Login dengan batas tiga kali percobaan. Pengguna memasukkan nama pengguna dan kata sandi. Jika data sesuai, sistem mengarahkan pengguna ke menu berdasarkan perannya, yaitu admin atau user. Jika login gagal hingga tiga kali, sistem mengembalikan pengguna ke menu utama.

- Menampilkan daftar merchandise menggunakan PrettyTable. Informasi yang ditampilkan meliputi ID barang, nama merchandise, harga, dan stok yang tersedia.

- CRUD barang untuk admin. Admin dapat menambah, melihat, mengubah, dan menghapus data merchandise. Setiap perubahan data barang disimpan ke dalam berkas barang.json agar dapat digunakan kembali ketika program dijalankan.

- Menambah barang baru. Admin memasukkan ID, nama barang, harga, dan stok. Sistem memeriksa data yang dimasukkan sebelum menyimpan barang baru.

- Mengubah data barang. Admin memilih barang berdasarkan ID, kemudian mengubah informasi yang diperlukan, seperti nama, harga, atau stok. Data yang telah diperbarui disimpan kembali ke barang.json.

- Menghapus barang dengan konfirmasi. Admin memilih barang yang akan dihapus. Sistem meminta konfirmasi sebelum menghapus data agar admin dapat memastikan bahwa barang yang dipilih memang ingin dihapus.

- Melihat daftar pengguna. Admin dapat melihat informasi pengguna yang telah terdaftar dalam sistem. Data tersebut dibaca dari berkas user.json dan ditampilkan dalam bentuk tabel.

- Pengisian saldo (top up). User memasukkan nominal saldo yang ingin ditambahkan. Sistem memvalidasi nominal tersebut, memperbarui saldo pengguna, lalu menyimpan perubahan data ke dalam user.json.

- Pembelian merchandise dengan validasi stok dan saldo. User memilih barang berdasarkan ID dan memasukkan jumlah pembelian. Sistem memeriksa ketersediaan stok serta kecukupan saldo sebelum memproses transaksi.

- Pencatatan transaksi ke berkas JSON. Transaksi yang berhasil dicatat ke dalam transaksi.json. Data transaksi digunakan untuk menyimpan informasi pembelian atau pengisian saldo dan mendukung fitur riwayat transaksi.

- Menampilkan invoice transaksi. Setelah transaksi berhasil, sistem menampilkan ringkasan transaksi yang berisi informasi pengguna, detail transaksi, total pembayaran, dan saldo setelah transaksi sesuai data yang tersedia pada program.

- Riwayat transaksi pengguna. User dapat melihat catatan transaksi miliknya sendiri. Sistem membaca data dari transaksi.json, kemudian menampilkan transaksi yang sesuai dengan nama pengguna yang sedang login.

- Laporan penjualan untuk admin. Admin dapat melihat ringkasan penjualan berdasarkan data transaksi yang tersimpan. Laporan mencakup total pendapatan dari pembelian, jumlah transaksi pembelian, dan barang terlaris sesuai perhitungan dalam program.

- Error handling menggunakan try-except. Program menangani kesalahan tertentu, seperti input yang tidak sesuai dan masalah ketika membaca atau menyimpan data. Penanganan kesalahan membantu program memberikan pesan yang lebih jelas kepada pengguna.

- Logout dan keluar program. Logout mengakhiri sesi pengguna dan mengembalikannya ke halaman login atau menu utama sesuai alur program. Sementara itu, pilihan keluar digunakan untuk menghentikan program.

**Penyimpanan Data**

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | user.json | Data akun pengguna, password, peran pengguna, dan saldo |
| 2 | barang.json | Data merchandise yang mencakup ID, nama barang, harga, dan stok |
| 3 | transaksi.json | Riwayat transaksi, kode transaksi, username, jenis transaksi, detail, total pembayaran, waktu, dan sisa saldo |


**Library**

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | os | Digunakan untuk membersihkan tampilan terminal melalui fungsi os.system("cls") agar menu program terlihat lebih rapi |
| 2 | time | Digunakan untuk memberikan jeda tampilan menggunakan time.sleep() dan mencatat waktu transaksi menggunakan time.strftime() |
| 3 | json | Digunakan untuk membaca dan menyimpan data pengguna, barang, serta transaksi ke dalam file JSON agar data tetap tersimpan meskipun program ditutup |
| 4 | PrettyTable | Digunakan untuk menampilkan data barang, pengguna, transaksi, dan invoice dalam bentuk tabel sehingga lebih mudah dibaca |
| 5 | pwinput | Digunakan untuk menyembunyikan karakter password ketika pengguna melakukan registrasi atau login |
| 6 | random | Merupakan library yang diimpor dalam program, tetapi belum digunakan pada fungsi yang tersedia |


**Funcion**

| No | Fungsi | Kegunaan |
| :--- | :---: | :---: |
| 1 | bersih() | Membersihkan tampilan terminal sebelum menu atau informasi baru ditampilkan |
| 2 | menu_utama() | Menampilkan menu utama yang berisi pilihan registrasi, login, dan keluar dari aplikasi |
| 3 | registrasi() | Memproses pembuatan akun baru dan menyimpan data pengguna ke file user.json |
| 4 | login() | Memeriksa username dan password serta mengarahkan pengguna ke menu sesuai dengan perannya |
| 5 | tampilkan_barang() | Menampilkan daftar merchandise beserta ID, nama, harga, dan stok barang |
| 6 | tambah_barang() | Menambahkan merchandise baru ke dalam daftar barang |
| 7 | ubah_barang() | Memperbarui nama, harga, atau stok barang yang sudah tersimpan |
| 8 | hapus_barang() | Menghapus barang berdasarkan ID yang dipilih setelah pengguna mengonfirmasi penghapusan |
| 9 | menu_crud_barang() | Menampilkan menu pengelolaan barang yang mencakup tambah, lihat, ubah, dan hapus data |
| 10 | cetak_invoice() | Menampilkan bukti transaksi yang berisi kode transaksi, waktu, username, jenis transaksi, total pembayaran, dan sisa saldo |
| 11 | top_up() | Menambahkan saldo pengguna dan mencatat transaksi pengisian saldo |
| 12 | beli_barang() | Memproses pembelian merchandise, menghitung total harga, memeriksa saldo, mengurangi stok, dan menyimpan transaksi |
| 13 | riwayat_transaksi() | Menampilkan riwayat transaksi, baik seluruh transaksi maupun transaksi milik pengguna tertentu |
| 14 | laporan_admin() | Menghitung total pendapatan, jumlah transaksi pembelian, dan produk terlaris |
| 15 | tampilkan_users() | Menampilkan daftar pengguna beserta peran dan saldo yang dimiliki |
| 16 | menu_admin() | Menampilkan menu khusus Admin untuk mengelola barang, melihat pengguna, memeriksa transaksi, dan melihat laporan penjualan |
| 17 | menu_user() | Menampilkan menu pengguna untuk melihat barang, mengisi saldo, membeli barang, dan melihat riwayat transaksi |

# Flowchart

**1. Registrasi dan Login**
   
   <img width="1732" height="1484" alt="FlowchartPAKel3-REGIS DAN LOGIN (1)" src="https://github.com/user-attachments/assets/cf1ab9a8-b744-4972-ab1e-928772321608" />

Flowchart registrasi dan login menjelaskan proses awal penggunaan program. Sistem menampilkan menu utama yang menyediakan pilihan registrasi, login, dan keluar. Pada proses registrasi, pengguna memasukkan nama pengguna dan kata sandi, kemudian sistem memeriksa kelengkapan serta kesesuaian data sebelum menyimpan akun ke dalam user.json.

Pada proses login, sistem mencocokkan data yang dimasukkan dengan data pengguna yang tersimpan. Jika data sesuai, pengguna diarahkan ke halaman berdasarkan perannya. Jika data tidak sesuai, sistem menampilkan pesan kesalahan dan memberikan kesempatan untuk mencoba kembali hingga batas percobaan yang ditentukan.

**2. CRUD**

   <img width="2232" height="1090" alt="_FlowchartPAKel3-CRUD" src="https://github.com/user-attachments/assets/38b53588-e73f-4977-9974-8940de97173c" />

Flowchart pengelolaan barang menggambarkan proses yang dapat dilakukan admin untuk melihat, menambah, mengubah, dan menghapus data barang. Sistem membaca data dari barang.json sebelum menjalankan proses yang dipilih. Ketika admin melakukan perubahan, sistem menyimpan data terbaru ke dalam berkas tersebut.

Program juga melakukan pemeriksaan terhadap data yang dimasukkan, seperti ID barang dan informasi barang lainnya. Jika barang tidak ditemukan atau data tidak sesuai, sistem menampilkan pesan yang relevan.

**3. Halaman Admin**

   <img width="1772" height="887" alt="_FlowchartPAKel3-Halaman Admin" src="https://github.com/user-attachments/assets/0d0094b0-af69-4197-8117-dd6c1041c926" />

Flowchart halaman admin menjelaskan pilihan menu yang tersedia setelah administrator berhasil login. Admin dapat mengelola barang, melihat data barang, memeriksa seluruh transaksi, menampilkan laporan penjualan, dan keluar dari akun.

Pada fitur laporan penjualan, sistem membaca data transaksi dari transaksi.json, kemudian menghitung informasi penjualan yang tersedia. Hasilnya ditampilkan agar admin dapat memantau pendapatan, jumlah transaksi pembelian, dan barang yang paling banyak terjual.

**4. Halaman User**

<img width="2031" height="957" alt="FlowchartPAKel3-Halaman User (1)" src="https://github.com/user-attachments/assets/c778759f-8581-456f-9f21-e9b32d4c0a1e" />

Flowchart halaman user menjelaskan fitur yang dapat digunakan oleh pengguna biasa. Pengguna dapat mengisi saldo, melihat daftar barang, membeli barang, melihat riwayat transaksi pribadi, dan keluar dari akun.

Dalam proses pembelian, sistem memeriksa ketersediaan stok dan kecukupan saldo. Jika persyaratan terpenuhi dan pembelian berhasil, sistem memperbarui saldo pengguna, mengurangi stok barang, serta menyimpan transaksi. Jika stok atau saldo tidak mencukupi, sistem menampilkan pesan yang sesuai.


# Daftar Fitur per Role

# Screenshot Output
