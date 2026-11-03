# PA_A3_Sistem-Penjualan-Merchandise-Komunitas

# Anggota dan Peran :
| Anggota | Peran |
| --- | --- |
| Salwa Annisa Nur Fadhila	(2609116010) | Konsep, Laporan, Pengecekan |
| Muhammad Favian Daffa	(2609116021) | Program, Coding, Flowchart, Pengembangan |
| Mutiara Zyahra Al Gazali (2609116026) | Konsep, Laporan, Program  |
| Fahry Alfisyahr Razak (2609116028) | Program, Flowchart, Konsep |

# Sistem Penjualan Komunitas

Program Sistem Penjualan Merchandise BEM FT merupakan aplikasi berbasis Python yang dirancang untuk mempermudah pengelolaan dan penjualan merchandise. Program ini memiliki dua jenis pengguna, yaitu admin dan user, dengan hak akses yang berbeda. Admin dapat mengelola data barang melalui fitur tambah, lihat, ubah, dan hapus (CRUD), melihat data user, memeriksa riwayat transaksi, serta melihat laporan penjualan. Sementara itu, user dapat melihat barang, melakukan top up saldo, membeli merchandise, dan melihat riwayat transaksi pribadi.

Proses pembelian dilakukan menggunakan saldo user. Program akan memeriksa ketersediaan stok dan kecukupan saldo sebelum memproses pembayaran. Jika transaksi berhasil, saldo dan stok barang akan diperbarui, data transaksi disimpan, dan invoice ditampilkan sebagai bukti pembayaran. Program menggunakan Python dan file JSON untuk mengolah serta menyimpan data user, barang, dan transaksi. Selain itu, program menerapkan fungsi, percabangan, perulangan, validasi input, dan penanganan kesalahan agar proses penjualan berjalan secara terstruktur.

# Flowchart

## 1. Registrasi dan Login
   
   <img width="1732" height="1484" alt="FlowchartPAKel3-REGIS DAN LOGIN (1)" src="https://github.com/user-attachments/assets/cf1ab9a8-b744-4972-ab1e-928772321608" />

Flowchart registrasi dan login menjelaskan proses awal penggunaan program. Sistem menampilkan menu utama yang menyediakan pilihan registrasi, login, dan keluar. Pada proses registrasi, user memasukkan username dan kata sandi, kemudian sistem memeriksa kelengkapan serta kesesuaian data sebelum menyimpan akun ke dalam user.json.

Pada proses login, sistem mencocokkan data yang dimasukkan dengan data user yang tersimpan. Jika data sesuai, user diarahkan ke halaman berdasarkan perannya. Jika data tidak sesuai, sistem menampilkan pesan kesalahan dan memberikan kesempatan untuk mencoba kembali hingga batas percobaan yang ditentukan.

## 2. CRUD

  <img width="2232" height="1090" alt="FlowchartPAKel3-CRUD (1)" src="https://github.com/user-attachments/assets/1e24ff25-d4b8-4a3b-a3f0-cce967950475" />


Flowchart pengelolaan barang menggambarkan proses yang dapat dilakukan admin untuk melihat, menambah, mengubah, dan menghapus data barang. Sistem membaca data dari barang.json sebelum menjalankan proses yang dipilih. Ketika admin melakukan perubahan, sistem menyimpan data terbaru ke dalam berkas tersebut.

Program juga melakukan pemeriksaan terhadap data yang dimasukkan, seperti ID barang dan informasi barang lainnya. Jika barang tidak ditemukan atau data tidak sesuai, sistem menampilkan pesan yang relevan.

## 3. Halaman Admin

   <img width="1772" height="887" alt="_FlowchartPAKel3-Halaman Admin" src="https://github.com/user-attachments/assets/0d0094b0-af69-4197-8117-dd6c1041c926" />

Flowchart halaman admin menjelaskan pilihan menu yang tersedia setelah administrator berhasil login. Admin dapat mengelola barang, melihat data barang, memeriksa seluruh transaksi, menampilkan laporan penjualan, dan keluar dari akun.

Pada fitur laporan penjualan, sistem membaca data transaksi dari transaksi.json, kemudian menghitung informasi penjualan yang tersedia. Hasilnya ditampilkan agar admin dapat memantau pendapatan, jumlah transaksi pembelian, dan barang yang paling banyak terjual.

## 4. Halaman User

<img width="2031" height="957" alt="FlowchartPAKel3-Halaman User (1)" src="https://github.com/user-attachments/assets/c778759f-8581-456f-9f21-e9b32d4c0a1e" />

Flowchart halaman user menjelaskan fitur yang dapat digunakan oleh user biasa. User dapat mengisi saldo, melihat daftar barang, membeli barang, melihat riwayat transaksi pribadi, dan keluar dari akun.

Dalam proses pembelian, sistem memeriksa ketersediaan stok dan kecukupan saldo. Jika persyaratan terpenuhi dan pembelian berhasil, sistem memperbarui saldo user, mengurangi stok barang, serta menyimpan transaksi. Jika stok atau saldo tidak mencukupi, sistem menampilkan pesan yang sesuai.


# Program

## 1. Data Penyimpanan

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | user.json | Data akun user, password, peran, dan saldo |
| 2 | barang.json | Data merchandise yang mencakup ID, nama barang, harga, dan stok |
| 3 | transaksi.json | Riwayat transaksi, kode transaksi, username, jenis transaksi, detail, total pembayaran, waktu, dan sisa saldo |


## 2. Library

| No | Library | Kegunaan |
| :--- | :---: | :---: |
| 1 | os | Digunakan untuk membersihkan tampilan terminal melalui fungsi os.system("cls") agar menu program terlihat lebih rapi |
| 2 | time | Digunakan untuk memberikan jeda tampilan menggunakan time.sleep() dan mencatat waktu transaksi menggunakan time.strftime() |
| 3 | json | Digunakan untuk membaca dan menyimpan data user, barang, serta transaksi ke dalam file JSON agar data tetap tersimpan meskipun program ditutup |
| 4 | PrettyTable | Digunakan untuk menampilkan data barang, user, transaksi, dan invoice dalam bentuk tabel sehingga lebih mudah dibaca |
| 5 | pwinput | Digunakan untuk menyembunyikan karakter password ketika user melakukan registrasi atau login |
| 6 | random | Digunakan untuk menghasilkan nilai secara acak, misalnya untuk membuat kode atau nomor transaksi. |


## 3. Funcion

| No | Fungsi | Kegunaan |
| :--- | :---: | :---: |
| 1 | bersih() | Membersihkan tampilan terminal sebelum menu atau informasi baru ditampilkan |
| 2 | asalpicik() | Menangani kesalahan input ketika user menekan tombol Ctrl+C atau terjadi error. Fungsi ini menampilkan pesan "No No Yaa!" dan mengulangi proses input tanpa menghentikan program
| 3 | menu_utama() | Menampilkan menu utama yang berisi pilihan registrasi, login, dan keluar dari aplikasi |
| 4 | registrasi() | Memproses pembuatan akun baru dan menyimpan data user ke file user.json |
| 5 | login() | Memeriksa username dan password serta mengarahkan user ke menu sesuai dengan perannya |
| 6 | tampilkan_barang() | Menampilkan daftar merchandise beserta ID, nama, harga, dan stok barang |
| 7 | tambah_barang() | Menambahkan merchandise baru ke dalam daftar barang |
| 8 | ubah_barang() | Memperbarui nama, harga, atau stok barang yang sudah tersimpan |
| 9 | hapus_barang() | Menghapus barang berdasarkan ID yang dipilih setelah user mengonfirmasi penghapusan |
| 10 | menu_crud_barang() | Menampilkan menu pengelolaan barang yang mencakup tambah, lihat, ubah, dan hapus data |
| 11 | cetak_invoice() | Menampilkan bukti transaksi yang berisi kode transaksi, waktu, username, jenis transaksi, total pembayaran, dan sisa saldo |
| 12 | top_up() | Menambahkan saldo user dan mencatat transaksi pengisian saldo |
| 13 | beli_barang() | Memproses pembelian merchandise, menghitung total harga, memeriksa saldo, mengurangi stok, dan menyimpan transaksi |
| 14 | riwayat_transaksi() | Menampilkan riwayat transaksi, baik seluruh transaksi maupun transaksi milik user tertentu |
| 15 | laporan_admin() | Menghitung total pendapatan, jumlah transaksi pembelian, dan produk terlaris |
| 16 | tampilkan_users() | Menampilkan daftar user beserta peran dan saldo yang dimiliki |
| 17 | menu_admin() | Menampilkan menu khusus Admin untuk mengelola barang, melihat user, memeriksa transaksi, dan melihat laporan penjualan |
| 18 | menu_user() | Menampilkan menu user untuk melihat barang, mengisi saldo, membeli barang, dan melihat riwayat transaksi |



# Alur Program

## 1. Library

<img width="613" height="89" alt="image" src="https://github.com/user-attachments/assets/78fe4e04-be6e-4932-9243-1adae0a8bb33" /><br>


Di awal program ini kami menggunakan beberapa library dan modul seperti os, time, json, PrettyTable, pwinput, dan random. Os sendiri berfungsi untuk membersihkan tampilan layar terminal agar lebih bersih dan rapi. Time digunakan untuk memberikan jeda waktu pada program serta mendapatkan informasi tanggal transaksi. Json digunakan untuk membaca dan menyimpan data dalam format JSON. PrettyTable digunakan untuk menampilkan data dalam bentuk tabel agar lebih terstruktur. Pwinput digunakan untuk menyembunyikan karakter password ketika pengguna melakukan input. Terakhir, Random digunakan untuk menghasilkan angka secara acak yang nantinya digunakan sebagai bagian dari kode transaksi.

---

## 2. Fungsi Membersihkan Terminal

<img width="613" height="41" alt="image" src="https://github.com/user-attachments/assets/fea68457-409c-4b75-8d82-4b7bc2dd1fab" /><br>

Pada function ini kami menggunakan os.system("cls") yang berfungsi untuk membersihkan tampilan layar terminal. Tujuannya agar setiap kali pengguna berpindah dari satu menu ke menu lainnya, tampilan sebelumnya tidak menumpuk sehingga program terlihat lebih rapi. Contohnya, ketika pengguna selesai melakukan login dan masuk ke menu admin, layar terminal akan dibersihkan terlebih dahulu sebelum menu admin ditampilkan.

---

## 3. Fungsi Keyboard Interrupt
<img width="613" height="114" alt="image" src="https://github.com/user-attachments/assets/7a04f79e-a0c7-497a-b6ad-ebc468767acd" /><br>

Pada function ini kami membuat sebuah function khusus untuk menangani input dari pengguna. Di dalamnya terdapat perulangan while True serta percabangan try-except yang digunakan untuk menangani error ketika pengguna menekan tombol Ctrl+C atau terjadi EOFError. Jika salah satu kondisi tersebut terjadi, program akan menampilkan pesan "No No Yaa!" tanpa langsung menghentikan program. Contohnya, ketika program meminta pengguna memasukkan username kemudian pengguna menekan Ctrl+C, program akan menampilkan pesan tersebut dan kembali meminta input. Dengan adanya function ini, penanganan input dapat digunakan secara berulang di berbagai bagian program.

---

## 4. Menu Utama

<img width="613" height="329" alt="image" src="https://github.com/user-attachments/assets/e11732b5-fae1-4569-a2ca-ec522ed2b41a" /><br>

Pada function ini, program akan menampilkan halaman menu utama dengan memberikan tiga pilihan, yaitu registrasi, login, dan keluar aplikasi. Di sini kami menggunakan perulangan while True agar menu dapat terus ditampilkan sampai pengguna memilih opsi keluar. Kemudian, terdapat percabangan if, elif, dan else untuk menentukan tindakan berdasarkan pilihan pengguna. Jika pengguna memilih angka 1, program akan menjalankan function registrasi(). Jika memilih angka 2, program akan menjalankan function login(). Sementara itu, jika memilih angka 3, program akan menampilkan pesan bahwa program selesai dan menghentikan perulangan menggunakan break. Apabila pengguna memasukkan pilihan selain ketiga opsi tersebut, program akan menampilkan pesan bahwa pilihan tidak tersedia.

---

# 5. Menu Registrasi
<img width="613" height="653" alt="Screenshot 2026-11-03 221538" src="https://github.com/user-attachments/assets/5cdbeea2-a93d-4865-8c21-98210dcd051a" />
<img width="613" height="126" alt="Screenshot 2026-11-03 221613" src="https://github.com/user-attachments/assets/fa4a1e39-2424-469e-b7fa-68c92f9a180a" /><br>


Function ini digunakan untuk melakukan pendaftaran akun baru. Pada awal function, program akan membersihkan layar dan menampilkan halaman registrasi. Selanjutnya, program akan membaca data pengguna dari file user.json menggunakan json.load(). Setelah itu, program akan meminta pengguna memasukkan username dan password dengan beberapa validasi. Pada bagian username, program memastikan bahwa username tidak boleh kosong, memiliki minimal lima karakter, dan belum digunakan oleh akun lain. Pengecekan username dilakukan menggunakan perulangan for dengan membandingkan username yang dimasukkan dengan data pengguna yang sudah tersimpan. Kemudian, pada bagian password, program memastikan bahwa password tidak boleh kosong dan memiliki minimal lima karakter. Jika seluruh persyaratan sudah terpenuhi, program akan membuat data akun baru yang berisi username, password, role sebagai user, dan saldo awal sebesar nol. Terakhir, data akun akan dimasukkan ke dalam daftar pengguna menggunakan append() dan disimpan kembali ke file user.json menggunakan json.dump().

---

# 6. Menu Login
<img width="613" height="554" alt="image" src="https://github.com/user-attachments/assets/02d601e7-ee6b-40b7-87ac-e3b0a5299993" /><br>

Function ini digunakan untuk melakukan proses autentikasi atau pemeriksaan akun pengguna sebelum masuk ke dalam sistem. Pertama, program akan membaca data akun dari file user.json. Di sini juga terdapat penanganan error menggunakan try-except, yaitu FileNotFoundError jika file tidak ditemukan dan json.JSONDecodeError jika isi file JSON tidak valid. Selanjutnya, program memberikan kesempatan login sebanyak tiga kali menggunakan variabel kesempatan = 3. Pengguna diminta memasukkan username dan password, kemudian program akan mencocokkan data tersebut dengan akun yang tersimpan di dalam file JSON. Jika username dan password sesuai, program akan menampilkan pesan login berhasil. Setelah itu, program akan memeriksa nilai role akun tersebut. Jika role adalah admin, pengguna akan diarahkan ke function menu_admin(), sedangkan jika role adalah user, pengguna akan diarahkan ke function menu_user(). Sebaliknya, jika username atau password salah, kesempatan login akan dikurangi satu. Apabila kesempatan sudah habis, program akan menampilkan pesan bahwa batas percobaan login telah tercapai. Contohnya, ketika admin memasukkan username dan password yang benar, program akan langsung mengarahkannya ke menu admin, sedangkan pengguna biasa akan diarahkan ke menu user.

---

# 7. Tampilkan Barang
<img width="613" height="415" alt="image" src="https://github.com/user-attachments/assets/cc0579f8-5ada-4e61-a7e2-6838c971e2f0" /><br>

Function ini digunakan untuk menampilkan seluruh daftar barang yang tersedia di dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Jika file tidak ditemukan, program akan menggunakan daftar kosong. Namun, jika file tidak valid, program akan menampilkan pesan error. Selanjutnya, program akan memeriksa apakah terdapat barang di dalam file tersebut. Jika terdapat barang, program akan menggunakan PrettyTable untuk membuat tabel dengan empat kolom, yaitu nomor barang, nama barang, harga, dan stok. Kemudian, program menggunakan perulangan for untuk memasukkan setiap data barang ke dalam tabel.

---

# 8. Tambah Barang
<img width="613" height="625" alt="Screenshot 2026-11-03 221944" src="https://github.com/user-attachments/assets/8dca76c2-f91e-4369-a97b-894e7c3053de" />
<img width="613" height="341" alt="Screenshot 2026-11-03 222003" src="https://github.com/user-attachments/assets/a7cfab2e-3c4d-490e-9c8d-e11d6d3473f3" /><br>


Function ini digunakan oleh admin untuk menambahkan barang baru ke dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Setelah itu, admin diminta memasukkan nomor barang dan nama barang. Program akan melakukan validasi untuk memastikan nomor barang dan nama barang tidak kosong serta nomor barang belum pernah digunakan. Selanjutnya, admin diminta memasukkan harga dan stok barang. Pada bagian ini digunakan try-except untuk memastikan harga dan stok yang dimasukkan berupa angka bulat. Harga harus lebih dari nol, sedangkan stok tidak boleh bernilai negatif. Jika seluruh data sudah sesuai, program akan menambahkan barang baru menggunakan append() dan menyimpan perubahan tersebut ke dalam file barang.json. Contohnya, admin ingin menambahkan barang baru dengan nomor KBMFT6, nama Topi FT, harga Rp75.000, dan stok 20. Setelah semua data valid, barang tersebut akan tersimpan dan masuk ke dalam daftar barang.

---

# 9. Ubah Barang

<img width="613" height="670" alt="image" src="https://github.com/user-attachments/assets/f5d1f570-747e-4821-814c-2371b85790dd" />
<img width="613" height="653" alt="image" src="https://github.com/user-attachments/assets/773af347-2c53-438b-bcad-401177ad1526" /><br>


Function ini digunakan oleh admin untuk mengubah informasi barang yang sudah tersimpan di dalam sistem. Pertama, program akan membaca data dari file barang.json, kemudian menampilkan seluruh daftar barang menggunakan PrettyTable. Setelah itu, admin diminta memasukkan nomor barang yang ingin diubah. Program akan mencari barang tersebut menggunakan perulangan for. Jika barang tidak ditemukan, program akan menampilkan pesan bahwa barang tidak tersedia. Namun, jika barang ditemukan, admin diberikan pilihan untuk mengubah nama, harga, dan stok barang. Pada bagian nama, admin cukup memasukkan nama baru. Jika input dikosongkan, nama barang akan tetap menggunakan data sebelumnya. Kemudian, untuk harga dan stok, program memberikan pilihan menggunakan input y atau n. Jika admin memilih y, program akan meminta data baru dan melakukan validasi angka. Terakhir, seluruh perubahan akan disimpan kembali ke file barang.json. Contohnya, admin ingin mengubah harga Kaos FT dari Rp100.000 menjadi Rp120.000. Admin cukup memilih barang tersebut, kemudian memilih y pada bagian ubah harga dan memasukkan harga baru.

---

# 10. Hapus Barang
<img width="613" height="299" alt="Screenshot 2026-11-03 220605" src="https://github.com/user-attachments/assets/90d2b430-e84b-4523-8fc2-12071ffc6d58" />
<img width="613" height="625" alt="Screenshot 2026-11-03 220551" src="https://github.com/user-attachments/assets/de323b59-bb39-445f-81e8-5921f3fa54d6" /><br>


Function ini digunakan oleh admin untuk menghapus barang yang sudah tersimpan di dalam sistem. Pertama, program akan membaca data barang dari file barang.json. Jika data tersedia, program akan menampilkan daftar barang menggunakan PrettyTable. Kemudian, admin diminta memasukkan nomor barang yang ingin dihapus. Program akan mencari barang berdasarkan nomor yang dimasukkan. Jika barang ditemukan, program akan meminta konfirmasi penghapusan menggunakan pilihan y atau n. Jika admin memilih y, barang akan dihapus menggunakan perintah remove(). Namun, jika admin memilih n, proses penghapusan akan dibatalkan. Setelah penghapusan berhasil, data terbaru akan disimpan kembali ke file barang.json. Contohnya, admin ingin menghapus barang dengan nomor KBMFT6. Setelah memilih barang tersebut dan memberikan konfirmasi y/n, barang akan dihapus dari daftar barang.

---

# 11. Menu Kelola Barang
<img width="613" height="515" alt="image" src="https://github.com/user-attachments/assets/57e55b24-c6ab-43d8-a870-9bdbf37e6895" /><br>

Function ini merupakan menu khusus untuk mengelola data barang atau yang biasa disebut CRUD, yaitu Create, Read, Update, dan Delete. Pada menu ini, program memberikan lima pilihan, yaitu menampilkan barang, menambahkan barang, mengubah barang, menghapus barang, dan kembali ke menu sebelumnya. Setiap pilihan akan menjalankan function yang sesuai dengan kebutuhan admin. Di sini juga digunakan perulangan while True agar admin dapat melakukan pengelolaan barang secara berulang kali tanpa harus kembali ke menu utama. Contohnya, jika admin memilih opsi nomor 2, program akan menjalankan function tambah_barang(). Setelah selesai, admin dapat kembali ke menu pengelolaan barang dan memilih opsi lainnya.

---

# 12. Cetak Invoice

<img width="613" height="302" alt="image" src="https://github.com/user-attachments/assets/941c8169-60e3-4428-b6f9-89df226a68dc" /><br>


Function ini digunakan untuk menampilkan invoice sebagai bukti transaksi yang dilakukan oleh pengguna. Di dalam function ini, kami menggunakan PrettyTable dengan dua kolom, yaitu keterangan dan detail. Informasi yang ditampilkan meliputi kode transaksi, waktu transaksi, username, jenis transaksi, detail transaksi, total pembayaran, dan sisa saldo setelah transaksi. Seluruh informasi tersebut diambil dari parameter data yang dikirimkan oleh function pemanggil. Contohnya, setelah pengguna berhasil melakukan pembelian Kaos FT sebanyak dua buah, program akan menampilkan invoice yang berisi total pembayaran sebesar Rp200.000 beserta sisa saldo pengguna.

---

# 13. Top Up Saldo
<img width="613" height="656" alt="Screenshot 2026-11-03 220126" src="https://github.com/user-attachments/assets/68832910-020d-48f1-a95a-8cecb88af883" />
<img width="613" height="470" alt="Screenshot 2026-11-03 220147" src="https://github.com/user-attachments/assets/10aa5687-b166-454c-9565-5c0fae8ee601" /><br>

Function ini digunakan untuk melakukan pengisian saldo akun pengguna. Pertama, program akan membaca data pengguna dari file user.json dan data transaksi dari file transaksi.json. Setelah itu, program akan mencari akun berdasarkan username yang sedang login. Jika akun ditemukan, program akan menampilkan saldo saat ini. Kemudian, pengguna diminta memasukkan nominal top up. Pada bagian ini terdapat validasi menggunakan try-except untuk memastikan nominal yang dimasukkan berupa angka bulat, minimal Rp1, dan maksimal Rp10.000.000. Setelah nominal sesuai, program akan meminta konfirmasi kepada pengguna. Jika pengguna menyetujui, saldo akan ditambahkan dan data akun disimpan kembali ke user.json. Selanjutnya, program akan membuat kode transaksi yang terdiri dari awalan TRX, tiga angka acak, dan nomor urut transaksi. Data transaksi kemudian disimpan ke dalam transaksi.json dan ditampilkan melalui function cetak_invoice(). Contohnya, pengguna memiliki saldo Rp50.000 dan melakukan top up sebesar Rp100.000. Setelah berhasil, saldo pengguna akan menjadi Rp150.000 dan sistem akan menampilkan invoice top up.

---

# 14. Beli Barang

<img width="613" height="611" alt="Screenshot 2026-11-03 214849" src="https://github.com/user-attachments/assets/8e91c8bf-d23e-431a-8d77-4f26e91c135b" />
<img width="613" height="599" alt="Screenshot 2026-11-03 214911" src="https://github.com/user-attachments/assets/4369c5ff-9be6-4300-9d53-e5821304f128" />
<img width="613" height="525" alt="WhatsApp Image 2026-11-03 at 21 54 54" src="https://github.com/user-attachments/assets/93fd610a-6706-4df6-b6bc-e9182ef4a17f" />
<img width="613" height="258" alt="Screenshot 2026-11-03 215000" src="https://github.com/user-attachments/assets/258e9f35-c795-4e37-b108-cb226bc5e6ff" /><br>


Function ini digunakan oleh pengguna untuk melakukan pembelian barang yang tersedia di dalam sistem. Pertama, program akan membaca data pengguna, barang, dan transaksi dari masing-masing file JSON. Kemudian, program akan mencari akun pengguna berdasarkan username yang sedang login dan menampilkan daftar barang menggunakan PrettyTable. Setelah itu, pengguna diminta memasukkan nomor barang yang ingin dibeli. Program akan memeriksa apakah barang ditemukan, apakah stok masih tersedia, dan apakah jumlah pembelian tidak melebihi stok yang tersedia. Selanjutnya, program menghitung total pembayaran dengan mengalikan harga barang dan jumlah pembelian. Sebelum pembayaran dilakukan, program akan memeriksa apakah saldo pengguna mencukupi. Jika saldo mencukupi, pengguna akan diminta memberikan konfirmasi pembayaran. Apabila pengguna menyetujui, saldo akan dikurangi sesuai total pembelian dan stok barang juga akan berkurang sesuai jumlah yang dibeli. Terakhir, perubahan data pengguna dan barang akan disimpan ke dalam file JSON. Program juga akan membuat data transaksi baru dan menampilkan invoice sebagai bukti pembelian. Contohnya, pengguna membeli dua Kaos FT dengan harga masing-masing Rp100.000. Maka total pembayaran adalah Rp200.000. Jika saldo mencukupi dan pengguna menyetujui pembayaran, saldo akan berkurang Rp200.000 dan stok barang berkurang sebanyak dua buah.

---

# 15. Riwayat Transaksi
<img width="613" height="487" alt="image" src="https://github.com/user-attachments/assets/e5b32106-6715-407b-859e-abd65267a4ae" /><br>
 <br>

Function ini digunakan untuk menampilkan riwayat transaksi yang telah dilakukan di dalam sistem. Pertama, program akan membaca data transaksi dari file transaksi.json. Jika file belum tersedia, program akan menggunakan daftar kosong. Kemudian, program membuat tabel menggunakan PrettyTable dengan enam kolom, yaitu kode transaksi, username, jenis transaksi, detail, total pembayaran, dan waktu transaksi. Pada bagian ini terdapat parameter username=None yang digunakan untuk membedakan tampilan riwayat transaksi antara admin dan user. Jika parameter username tidak diberikan, program akan menampilkan seluruh transaksi. Namun, jika username diberikan, program hanya akan menampilkan transaksi milik pengguna tersebut. Contohnya, ketika admin memilih menu riwayat transaksi, seluruh transaksi dari semua pengguna akan ditampilkan. Sementara itu, jika user membuka riwayat transaksi, hanya transaksi yang dilakukan oleh akun tersebut yang akan ditampilkan.

---

# 16. Laporan Admin

<img width="613" height="640" alt="image" src="https://github.com/user-attachments/assets/2b16274f-346c-4b03-a871-1bdedd0c7bf3" /> <br>

Function ini digunakan untuk menampilkan laporan penjualan khusus admin. Program akan menghitung total pendapatan, jumlah transaksi pembelian, serta jumlah barang yang terjual. Selain itu, program juga mencari produk dengan penjualan terbanyak untuk mengetahui produk terlaris. Hasil perhitungan tersebut kemudian ditampilkan di terminal.

---

# 17. Tampilkan User

<img width="613" height="286" alt="image" src="https://github.com/user-attachments/assets/78bb4be3-cca9-4b7c-a57e-20c0436d5753" /> <br>


Function ini digunakan oleh admin untuk melihat daftar pengguna yang telah terdaftar. Program membaca data dari user.json, kemudian menampilkan username, role, dan saldo menggunakan PrettyTable. Di sini hanya akun dengan role user yang akan ditampilkan.

---

# 18. Menu Admin

<img width="613" height="402" alt="image" src="https://github.com/user-attachments/assets/850b081a-4402-4c7b-8bc8-8fa470701a00" /> <br>


Function ini merupakan halaman utama khusus admin setelah berhasil login. Terdapat lima pilihan, yaitu kelola barang, lihat pengguna, lihat seluruh transaksi, laporan penjualan, dan logout. Setiap pilihan akan menjalankan function yang sesuai. Jika admin memilih logout, program akan kembali ke menu utama.

---

# 19. Menu User

<img width="613" height="653" alt="image" src="https://github.com/user-attachments/assets/2d57cf3a-5237-4c25-b54c-cd390d028663" /> <br>

Function ini merupakan halaman utama khusus pengguna setelah berhasil login. Menu ini memiliki lima pilihan, yaitu melihat barang, top up saldo, membeli barang, melihat riwayat transaksi, dan logout. Program juga menampilkan username serta saldo pengguna. Setiap pilihan akan diarahkan ke function yang sesuai dengan kebutuhan pengguna.

---

# 20. Main Program

<img width="613" height="115" alt="image" src="https://github.com/user-attachments/assets/dc413889-8039-40f8-bad4-67ce3365cb16" /> <br>

Pada bagian terakhir program, terdapat perulangan while True yang digunakan untuk menjalankan menu_utama(). Selain itu, terdapat try-except untuk menangani KeyboardInterrupt dan EOFError. Jika pengguna menekan Ctrl+C atau terjadi EOFError, program akan menampilkan pesan "No No Yaa!" dan mencoba menjalankan kembali menu utama. Namun, jika pengguna memilih keluar aplikasi secara normal, program akan berhenti menggunakan break.

---


# Screenshot Output

## Login Sebagai Admin
<img width="392" height="116" alt="Screenshot 2026-10-30 000741" src="https://github.com/user-attachments/assets/4a473486-f982-4ffc-be8a-10fd9ad38247" /><br>
<img width="392" height="140" alt="Screenshot 2026-10-30 001754" src="https://github.com/user-attachments/assets/6313236a-bef3-4dea-97ba-49a33c509f3f" /><br>

Proses dimulai dari Menu utama dengan tiga opsi utama: Registrasi, Login, Keluar Aplikasi. 
Setelah pengguna berhasil login sebagai Admin, sistem akan menampilkan Menu Admin yang berisi beberapa fitur utama, yaitu: 
- Kelola barang
- Lihat pengguna
- Lihat seluruh transaksi
- Laporan
- Logout

# 1. Kelola Barang
<img width="392" height="135" alt="Screenshot 2026-10-30 001835" src="https://github.com/user-attachments/assets/94b5833c-c7d6-424c-9e11-2983427a5638" /><br>

Cuplikan ini menampilkan tahapan navigasi setelah Admin memilih opsi “Kelola Barang” dari menu utama Admin. Pada bagian ini, sistem menampilkan lima fitur utama yang berfungsi untuk mengelola data barang, yaitu:

- Tampilkan Barang – Menampilkan daftar barang yang tersedia dalam sistem.
- Tambah Barang – Menambahkan data barang baru ke dalam database.
- Ubah Barang – Mengubah informasi barang yang sudah terdaftar.
- Hapus Barang – Menghapus barang dari sistem.
- Kembali – Mengembalikan pengguna ke menu Admin sebelumnya.

## 1. Tampilkan Barang

<img width="392" height="249" alt="Screenshot 2026-10-30 001845" src="https://github.com/user-attachments/assets/1ad66c98-d93a-4932-8640-ec3e6baa1bd4" /><br>

Cuplikan ini menampilkan hasil dari pilihan menu “Tampilkan Barang” pada bagian Kelola Barang. Pada tahap ini, sistem menampilkan tabel berisi seluruh data barang yang tersimpan di database, dengan atribut sebagai berikut:

- Nomor – Penomoran untuk setiap barang.
- Nama Barang – Nama item yang dijual.
- Harga – Harga satuan produk.
- Stok – Jumlah produk yang tersedia.

Tampilan berbasis teks ini dibuat untuk memberikan kemudahan dalam memantau data produk secara cepat dan efisien langsung melalui terminal.

## 2. Tambah Barang

<img width="392" height="137" alt="Screenshot 2026-10-30 001854" src="https://github.com/user-attachments/assets/ff607e7b-4ff9-49e8-ae86-c2b062150f63" /><br>
<img width="392" height="140" alt="Screenshot 2026-10-30 001939" src="https://github.com/user-attachments/assets/e2df865e-584e-4eb1-83b3-e06a35434e67" /><br>

Cuplikan ini menunjukkan proses penambahan barang baru ke dalam sistem. Pengguna menginput data seperti nomor barang, nama barang, harga barang, stok barang, kemudian sistem menyimpan data tersebut ke dalam file JSON. Setelah proses berhasil, sistem menampilkan pesan “Barang berhasil ditambahkan.” dan memperbarui daftar barang yang tersedia di terminal.

## 3. Ubah Barang

<img width="392" height="320" alt="Screenshot 2026-10-30 002115" src="https://github.com/user-attachments/assets/6886b043-00ec-46bc-9204-b5512a665fd3" /><br>

Gambar ini memperlihatkan proses pengubahan data barang. Pengguna memasukkan nomor barang yang ingin diperbarui, kemudian sistem menampilkan data barang sebelumnya. Pengguna dapat mengubah nomor barang, nama barang, harga, maupun stok. Jika ada informasi yang tidak ingin diubah, pengguna cukup mengosongkan input atau memilih untuk tidak melakukan perubahan. Setelah proses selesai, sistem menyimpan data terbaru dan menampilkan pesan “Data barang berhasil diperbarui.”

## 4. Hapus Barang

<img width="439" height="152" alt="Screenshot 2026-10-30 002132" src="https://github.com/user-attachments/assets/ad7c7e45-bb36-4df2-bf10-7070fe2bfdef" /><br>
<img width="272" height="254" alt="Screenshot 2026-10-30 002204" src="https://github.com/user-attachments/assets/7d5b204a-f710-4f4d-9cb9-18a5280d7b2a" /><br>

Cuplikan ini menunjukkan proses penghapusan data barang dari sistem. Pengguna memasukkan nomor barang yang ingin dihapus, kemudian sistem meminta konfirmasi sebelum benar-benar menghapus data dari file JSON. Jika pengguna memilih “ya”, maka sistem menampilkan pesan “Barang berhasil dihapus.” dan memperbarui daftar produk yang tersisa

## 5. Kembali

<img width="392" height="193" alt="Screenshot 2026-10-30 002216" src="https://github.com/user-attachments/assets/6b442dd0-174d-47e5-8225-3380ae6ce482" /><br>

Cuplikan ini menunjukan proses untuk kembali ke menu utama admin.

# 2. Lihat Pengguna

<img width="384" height="140" alt="Screenshot 2026-10-30 001754" src="https://github.com/user-attachments/assets/4e4608ba-9803-46db-aa91-f88afaf0a3bf" /><br>
<img width="435" height="267" alt="WhatsApp Image 2026-11-02 at 23 16 43" src="https://github.com/user-attachments/assets/8b741fac-eb19-4f79-b7ef-820afbb87b9e" /><br>

Setelah admin memilih opsi 2 "Lihat Pengguna" pada Menu Admin, program menampilkan tabel daftar seluruh pengguna yang terdaftar. Tabel berisi kolom Username, Role, dan Saldo. Setelah itu program menampilkan pesan “Tekan Enter untuk melanjutkan” untuk kembali ke menu admin.

# 3. Lihat seluruh transaksi
<img width="384" height="140" alt="Screenshot 2026-10-30 001754" src="https://github.com/user-attachments/assets/4e4608ba-9803-46db-aa91-f88afaf0a3bf" /><br>
<img width="470" height="178" alt="WhatsApp Image 2026-11-02 at 23 16 42" src="https://github.com/user-attachments/assets/c8de77af-8ed4-4b80-bfae-12a6d0371a87" /><br>

Setelah admin memilih opsi 3 "Lihat seluruh transaksi", program menampilkan tabel seluruh transaksi dari semua pengguna. Kolom yang ditampilkan adalah Kode, Username, Jenis (TOP UP atau PEMBELIAN), Detail, Total, dan Waktu. Setelah itu program menunggu admin menekan Enter untuk melanjutkan.

# 4. Laporan Penjualan
<img width="392" height="140" alt="Screenshot 2026-10-30 001754" src="https://github.com/user-attachments/assets/4e4608ba-9803-46db-aa91-f88afaf0a3bf" /><br>
<img width="392" height="132" alt="Screenshot 2026-10-30 002336" src="https://github.com/user-attachments/assets/9aefbd80-42a1-4bbe-bddb-940a63955cf3" /><br>

Setelah admin memilih opsi 4 "Laporan Penjualan", program akan menampilkan laporan penjualan, Laporan ini dihitung dari seluruh transaksi berjenis pembelian. Setelah itu program menunggu admin menekan Enter untuk melanjutkan.

# 5. Logout

<img width="380" height="192" alt="WhatsApp Image 2026-11-02 at 23 16 43 (1)" src="https://github.com/user-attachments/assets/ffc24b14-b8c6-4975-8367-52aee4674c3b" /><br>

Setelah admin memilih opsi ke 5 "Logout", program menampilkan pesan “Logout berhasil.” dan admin keluar dari akun. Program lalu meminta menekan Enter untuk kembali ke menu utama.

## LOGIN SEBAGAI USER

<img width="417" height="208" alt="Screenshot 2026-10-30 000741" src="https://github.com/user-attachments/assets/9264bd49-ee1e-481b-85e1-a798826feee1" /><br>
<img width="417" height="208" alt="Screenshot 2026-10-30 001221" src="https://github.com/user-attachments/assets/e1c9cb1b-bd65-4ce9-a9d6-e02939ee493a" /><br>

Pada Menu Utama, pengguna memilih opsi yang pertama "Registrasi". Program meminta pengisian username dan password ditampilkan sebagai tanda bintang demi keamanan. Jika data valid, program menampilkan pesan “Registrasi berhasil!” lalu menunggu Enter untuk melanjutkan.

<br>
<img width="417" height="208" alt="Screenshot 2026-10-30 001235" src="https://github.com/user-attachments/assets/60a3e244-b005-491b-8022-95e33b440566" /><br>
<img width="417" height="208" alt="Screenshot 2026-10-30 001417" src="https://github.com/user-attachments/assets/d58146d6-b705-40b0-bce2-99c7ed92a7ec" /><br>

Setelah registrasi, pengguna memilih opsi kedua. Login pada Menu Utama, Jika login berhasil, program menampilkan Menu User dengan sapaan “Halo...” serta informasi saldo (awalnya Rp 0). 

Menu yang tersedia: 
- Lihat barang
- Top up saldo
- Beli barang
- Riwayat transaksi
- Logout.

## 1. Lihat Barang

<img width="415" height="251" alt="Screenshot 2026-10-30 001636" src="https://github.com/user-attachments/assets/74ea26a6-76ce-4c71-8241-bc7be40fcb3b" /><br>

Program menampilkan daftar barang dalam bentuk tabel dengan kolom nomor barang, nama barang, harga, dan stok. Adapun contoh barang yang di masukkan adalah PDH KBM FT, Kaos FT, Gantungan kunci FT, Slayer FT, Sticker FT, Kaos Kaki FT, dan beberapa barang lain nya. Setelah itu program menunggu Enter untuk melanjutkan.

## 2. Top up saldo

<img width="434" height="308" alt="Screenshot 2026-10-30 001505" src="https://github.com/user-attachments/assets/5d031474-456c-42f8-8d38-f8cfbe35dabe" /><br>

Pengguna atau user memasukkan nominal Top Up yang di ingin kan, lalu program meminta konfirmasi "ya/tidak". Setelah menjawab y, program menampilkan "Top up berhasil" beserta invoice yang berisi kode transaksi, waktu, username, jenis (TOP UP), detail, total, dan sisa saldo.

## 3. Beli Barang

<img width="371" height="285" alt="Screenshot 2026-10-30 001543" src="https://github.com/user-attachments/assets/ca1ddb71-96b5-4f44-b9ba-1df653141e0f" /><br>
<img width="291" height="214" alt="Screenshot 2026-10-30 001551" src="https://github.com/user-attachments/assets/8fa2f261-cd37-4dc0-85ff-a225fdf7b0a1" /><br>

Program menampilkan daftar barang, lalu pengguna memasukkan nomor barang dan jumlah pembelian. Setelah pengguna konfirmasi dengan y pada “Lanjutkan pembayaran?”, program menampilkan “Pembelian berhasil!”.Lalu program menampilkan invoice pembelian.

## 4. Riwayat transaksi

<img width="562" height="119" alt="Screenshot 2026-10-30 001610" src="https://github.com/user-attachments/assets/a026fe5e-8c2d-46e7-989b-57c07a0896d2" /><br>

Setelah pengguna konfirmasi dengan y pada “Lanjutkan pembayaran?”, program menampilkan “Pembelian berhasil!”.

## 5. Logout

<img width="371" height="220" alt="WhatsApp Image 2026-11-02 at 23 41 10" src="https://github.com/user-attachments/assets/aaa62e46-0813-4f33-b925-f96c01139c4f" /><br>

Setelah pengguna memilih opsi ke 5, program menampilkan “Logout berhasil.” dan pengguna keluar dari akunnya. Program lalu meminta menekan Enter untuk kembali ke menu utama.
