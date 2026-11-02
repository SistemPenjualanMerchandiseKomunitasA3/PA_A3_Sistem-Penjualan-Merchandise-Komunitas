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



# Penjelasan Per Kode

<img width="227" height="95" alt="image" src="https://github.com/user-attachments/assets/0c83eb96-3007-48a6-bc4d-c5ac3c26d05b" />

Di awal program ini kami menggunakan beberapa library dan modul seperti os, time, json, PrettyTable, pwinput, dan random. Os sendiri berfungsi untuk membersihkan tampilan layar terminal agar lebih bersih dan rapi. Time digunakan untuk memberikan jeda waktu pada program serta mendapatkan informasi tanggal transaksi. Json digunakan untuk membaca dan menyimpan data dalam format JSON. PrettyTable digunakan untuk menampilkan data dalam bentuk tabel agar lebih terstruktur. Pwinput digunakan untuk menyembunyikan karakter password ketika pengguna melakukan input. Terakhir, Random digunakan untuk menghasilkan angka secara acak yang nantinya digunakan sebagai bagian dari kode transaksi.

<img width="149" height="40" alt="image" src="https://github.com/user-attachments/assets/d85bb076-9fbd-44ea-ab63-b873d9799db1" />

Pada function ini kami menggunakan os.system("cls") yang berfungsi untuk membersihkan tampilan layar terminal. Tujuannya agar setiap kali pengguna berpindah dari satu menu ke menu lainnya, tampilan sebelumnya tidak menumpuk sehingga program terlihat lebih rapi. Contohnya, ketika pengguna selesai melakukan login dan masuk ke menu admin, layar terminal akan dibersihkan terlebih dahulu sebelum menu admin ditampilkan.

<img width="225" height="127" alt="image" src="https://github.com/user-attachments/assets/8961ead8-7941-4b1a-a750-300f90a7d707" />

Pada function ini kami membuat sebuah function khusus untuk menangani input dari pengguna. Di dalamnya terdapat perulangan while True serta percabangan try-except yang digunakan untuk menangani error ketika pengguna menekan tombol Ctrl+C atau terjadi EOFError. Jika salah satu kondisi tersebut terjadi, program akan menampilkan pesan "No No Yaa!" tanpa langsung menghentikan program. Contohnya, ketika program meminta pengguna memasukkan username kemudian pengguna menekan Ctrl+C, program akan menampilkan pesan tersebut dan kembali meminta input. Dengan adanya function ini, penanganan input dapat digunakan secara berulang di berbagai bagian program.

<img width="488" height="332" alt="image" src="https://github.com/user-attachments/assets/3a5d3a05-f107-4dc3-82ef-506eefec45e9" />

Pada function ini, program akan menampilkan halaman menu utama dengan memberikan tiga pilihan, yaitu registrasi, login, dan keluar aplikasi. Di sini kami menggunakan perulangan while True agar menu dapat terus ditampilkan sampai pengguna memilih opsi keluar. Kemudian, terdapat percabangan if, elif, dan else untuk menentukan tindakan berdasarkan pilihan pengguna. Jika pengguna memilih angka 1, program akan menjalankan function registrasi(). Jika memilih angka 2, program akan menjalankan function login(). Sementara itu, jika memilih angka 3, program akan menampilkan pesan bahwa program selesai dan menghentikan perulangan menggunakan break. Apabila pengguna memasukkan pilihan selain ketiga opsi tersebut, program akan menampilkan pesan bahwa pilihan tidak tersedia.

<img width="500" height="563" alt="image" src="https://github.com/user-attachments/assets/905ff3d4-bc26-4519-ab0d-9490c5dd4fa4" />
<br>
<img width="398" height="130" alt="image" src="https://github.com/user-attachments/assets/3c395444-6476-485d-b4b3-b6d89c73e887" />

Function ini digunakan untuk melakukan pendaftaran akun baru. Pada awal function, program akan membersihkan layar dan menampilkan halaman registrasi. Selanjutnya, program akan membaca data pengguna dari file user.json menggunakan json.load(). Setelah itu, program akan meminta pengguna memasukkan username dan password dengan beberapa validasi. Pada bagian username, program memastikan bahwa username tidak boleh kosong, memiliki minimal lima karakter, dan belum digunakan oleh akun lain. Pengecekan username dilakukan menggunakan perulangan for dengan membandingkan username yang dimasukkan dengan data pengguna yang sudah tersimpan. Kemudian, pada bagian password, program memastikan bahwa password tidak boleh kosong dan memiliki minimal lima karakter. Jika seluruh persyaratan sudah terpenuhi, program akan membuat data akun baru yang berisi username, password, role sebagai user, dan saldo awal sebesar nol. Terakhir, data akun akan dimasukkan ke dalam daftar pengguna menggunakan append() dan disimpan kembali ke file user.json menggunakan json.dump().

<img width="518" height="560" alt="image" src="https://github.com/user-attachments/assets/cee136c4-e968-48ef-afaa-b8689b175e3e" />

Function ini digunakan untuk melakukan proses autentikasi atau pemeriksaan akun pengguna sebelum masuk ke dalam sistem. Pertama, program akan membaca data akun dari file user.json. Di sini juga terdapat penanganan error menggunakan try-except, yaitu FileNotFoundError jika file tidak ditemukan dan json.JSONDecodeError jika isi file JSON tidak valid. Selanjutnya, program memberikan kesempatan login sebanyak tiga kali menggunakan variabel kesempatan = 3. Pengguna diminta memasukkan username dan password, kemudian program akan mencocokkan data tersebut dengan akun yang tersimpan di dalam file JSON. Jika username dan password sesuai, program akan menampilkan pesan login berhasil. Setelah itu, program akan memeriksa nilai role akun tersebut. Jika role adalah admin, pengguna akan diarahkan ke function menu_admin(), sedangkan jika role adalah user, pengguna akan diarahkan ke function menu_user(). Sebaliknya, jika username atau password salah, kesempatan login akan dikurangi satu. Apabila kesempatan sudah habis, program akan menampilkan pesan bahwa batas percobaan login telah tercapai. Contohnya, ketika admin memasukkan username dan password yang benar, program akan langsung mengarahkannya ke menu admin, sedangkan pengguna biasa akan diarahkan ke menu user.

<img width="497" height="433" alt="image" src="https://github.com/user-attachments/assets/99e83eb1-5101-4291-a9f3-90e2b442e9c0" />

Function ini digunakan untuk menampilkan seluruh daftar barang yang tersedia di dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Jika file tidak ditemukan, program akan menggunakan daftar kosong. Namun, jika file tidak valid, program akan menampilkan pesan error. Selanjutnya, program akan memeriksa apakah terdapat barang di dalam file tersebut. Jika terdapat barang, program akan menggunakan PrettyTable untuk membuat tabel dengan empat kolom, yaitu nomor barang, nama barang, harga, dan stok. Kemudian, program menggunakan perulangan for untuk memasukkan setiap data barang ke dalam tabel.

<img width="489" height="409" alt="image" src="https://github.com/user-attachments/assets/a85ae1f3-186b-4d11-901d-bbb3aa77fab4" />
<br>
<img width="413" height="574" alt="image" src="https://github.com/user-attachments/assets/87795a47-6380-4477-9a05-062c4c4c91e3" />

Function ini digunakan oleh admin untuk menambahkan barang baru ke dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Setelah itu, admin diminta memasukkan nomor barang dan nama barang. Program akan melakukan validasi untuk memastikan nomor barang dan nama barang tidak kosong serta nomor barang belum pernah digunakan. Selanjutnya, admin diminta memasukkan harga dan stok barang. Pada bagian ini digunakan try-except untuk memastikan harga dan stok yang dimasukkan berupa angka bulat. Harga harus lebih dari nol, sedangkan stok tidak boleh bernilai negatif. Jika seluruh data sudah sesuai, program akan menambahkan barang baru menggunakan append() dan menyimpan perubahan tersebut ke dalam file barang.json. Contohnya, admin ingin menambahkan barang baru dengan nomor KBMFT6, nama Topi FT, harga Rp75.000, dan stok 20. Setelah semua data valid, barang tersebut akan tersimpan dan masuk ke dalam daftar barang.

<img width="477" height="586" alt="image" src="https://github.com/user-attachments/assets/285d64f4-b5be-4d37-b52b-60a2bc44cb7b" />
<br>
<img width="355" height="467" alt="image" src="https://github.com/user-attachments/assets/926d3772-165c-477a-a851-c3de35afa1c3" />
<br>
<img width="354" height="269" alt="image" src="https://github.com/user-attachments/assets/a8400aca-e0f2-4fff-a57c-9f04ef279b8e" />

Function ini digunakan oleh admin untuk mengubah informasi barang yang sudah tersimpan di dalam sistem. Pertama, program akan membaca data dari file barang.json, kemudian menampilkan seluruh daftar barang menggunakan PrettyTable. Setelah itu, admin diminta memasukkan nomor barang yang ingin diubah. Program akan mencari barang tersebut menggunakan perulangan for. Jika barang tidak ditemukan, program akan menampilkan pesan bahwa barang tidak tersedia. Namun, jika barang ditemukan, admin diberikan pilihan untuk mengubah nama, harga, dan stok barang. Pada bagian nama, admin cukup memasukkan nama baru. Jika input dikosongkan, nama barang akan tetap menggunakan data sebelumnya. Kemudian, untuk harga dan stok, program memberikan pilihan menggunakan input y atau n. Jika admin memilih y, program akan meminta data baru dan melakukan validasi angka. Terakhir, seluruh perubahan akan disimpan kembali ke file barang.json. Contohnya, admin ingin mengubah harga Kaos FT dari Rp100.000 menjadi Rp120.000. Admin cukup memilih barang tersebut, kemudian memilih y pada bagian ubah harga dan memasukkan harga baru.

<img width="450" height="424" alt="image" src="https://github.com/user-attachments/assets/038fcfc0-3ebf-4af3-922d-25e03a2cd000" />
<br>
<img width="446" height="473" alt="image" src="https://github.com/user-attachments/assets/608e3575-42b8-40f7-941c-daca3273359c" />

Function ini digunakan oleh admin untuk menghapus barang yang sudah tersimpan di dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Jika data tersedia, program akan menampilkan daftar barang menggunakan PrettyTable. Kemudian, admin diminta memasukkan nomor barang yang ingin dihapus. Program akan mencari barang berdasarkan nomor yang dimasukkan. Jika barang ditemukan, program akan meminta konfirmasi penghapusan menggunakan pilihan y atau n. Jika admin memilih y, barang akan dihapus menggunakan perintah remove(). Namun, jika admin memilih n, proses penghapusan akan dibatalkan. Setelah penghapusan berhasil, data terbaru akan disimpan kembali ke file barang.json. Contohnya, admin ingin menghapus barang dengan nomor KBMFT6. Setelah memilih barang tersebut dan memberikan konfirmasi y, barang akan dihapus dari daftar barang.

<img width="515" height="533" alt="image" src="https://github.com/user-attachments/assets/ee75d123-a93e-4314-b022-e17589888421" />

Function ini merupakan menu khusus untuk mengelola data barang atau yang biasa disebut CRUD, yaitu Create, Read, Update, dan Delete. Pada menu ini, program memberikan lima pilihan, yaitu menampilkan barang, menambahkan barang, mengubah barang, menghapus barang, dan kembali ke menu sebelumnya. Setiap pilihan akan menjalankan function yang sesuai dengan kebutuhan admin. Di sini juga digunakan perulangan while True agar admin dapat melakukan pengelolaan barang secara berulang kali tanpa harus kembali ke menu utama. Contohnya, jika admin memilih opsi nomor 2, program akan menjalankan function tambah_barang(). Setelah selesai, admin dapat kembali ke menu pengelolaan barang dan memilih opsi lainnya.

<img width="350" height="311" alt="image" src="https://github.com/user-attachments/assets/6c72c03b-6bc3-4f70-90af-3a1dc1396091" />

Function ini digunakan untuk menampilkan invoice sebagai bukti transaksi yang dilakukan oleh pengguna. Di dalam function ini, kami menggunakan PrettyTable dengan dua kolom, yaitu keterangan dan detail. Informasi yang ditampilkan meliputi kode transaksi, waktu transaksi, username, jenis transaksi, detail transaksi, total pembayaran, dan sisa saldo setelah transaksi. Seluruh informasi tersebut diambil dari parameter data yang dikirimkan oleh function pemanggil. Contohnya, setelah pengguna berhasil melakukan pembelian Kaos FT sebanyak dua buah, program akan menampilkan invoice yang berisi total pembayaran sebesar Rp200.000 beserta sisa saldo pengguna.

# Screenshot Output
