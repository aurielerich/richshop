### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
step by step yang saya lakukan adalah seagai berikut:
1. buat repo baru digithub
2. membuat virtual environment dan mengaktifkanya
3. membuat file requirements.txt yang berisi dependencies
4. menginstal dependescies yang ada di requirements.txt dengan menjalankan comand
5. mengubah variabel environment dengan membuat file .env dan .env.prod
6. membuat file .gitignore untuk menjaga kerahasiaan data
7. membuat proyek django dengan nama richshop
8. membuat project baru di PWS dan menyamakan environs PWS dengan yang ada di .env.prod
9. mengkonfigurasi variabel environment dengan membuat file .env dan .env.prod
10. membuat aplikasi main didalam proyek
11. mendaftarkan aplikasi main kedalam variable INSTALLED_APPS pada file settings.py
12. membuat template yang berisikan main.html
13. Melengkapi logic pada file models.py,views.py, dan urls.py
14. setelah selesai lakukan migrasi
15. melakukan push ke github dengan git add, commit, push di github dan pws



### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Alur sederhana request dan response pada web aplikasi Django:

<img width="725" height="525" alt="image" src="https://github.com/user-attachments/assets/f1514745-82a5-4bda-b1ab-b70c0317fabb" />

sumber: Forum Diskusi Minggu Kedua - "Alur Django" - Course PBP SCELE


Penjelasan keterkaitan berkas:

urls.py berfungsi sebagai “peta jalan”. Request yang masuk dari client akan diarahkan ke fungsi atau class pada views.py.

views.py berisi logika utama. Ia menerima request, bisa memanggil data dari models.py, lalu meneruskan data tersebut ke template HTML.

models.py menjadi representasi struktur data dalam database. Jika views.py membutuhkan data, ia akan mengakses database melalui models.py.

HTML template adalah tampilan yang diberikan kembali ke client. Data yang diproses di views.py akan dirender ke file HTML.

### 3. Jelaskan peran settings.py dalam proyek Django!

File settings.py memuat seluruh konfigurasi proyek Django, mulai dari koneksi database, daftar aplikasi yang digunakan, middleware, pengaturan keamanan, hingga konfigurasi static file. Dengan adanya file ini, proyek Django dapat dijalankan sesuai dengan environment yang diinginkan tanpa perlu menulis konfigurasi berulang kali.

### 4. Bagaimana cara kerja migrasi database di Django?

Migrasi di Django digunakan untuk menyelaraskan perubahan pada models.py dengan struktur tabel di database. Prosesnya:

Menulis atau mengubah model di models.py.

Menjalankan perintah python manage.py makemigrations untuk membuat berkas migrasi.

Menjalankan python manage.py migrate untuk menerapkan perubahan ke database.

Dengan migrasi, perubahan struktur tabel dapat dikelola secara teratur tanpa harus menulis query SQL manual.

### 5.  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dipilih sebagai framework awal pembelajaran karena sifatnya yang “batteries included”. Django menyediakan banyak fitur bawaan seperti sistem autentikasi, ORM, admin panel, serta arsitektur yang terstruktur. Dengan demikian, pemula dapat fokus memahami alur dasar pengembangan perangkat lunak berbasis web tanpa harus menambahkan terlalu banyak library eksternal.

### 6. Feedback untuk Asisten Dosen Tutorial 1

Tutorial 1 sudah cukup jelas dalam menjelaskan konsep dasar Django, terutama dalam pembuatan proyek dan aplikasi. Penjelasan langkah demi langkah membantu pemahaman peserta. Ke depannya, akan lebih baik jika diberikan contoh konkret bagaimana setiap file (urls.py, views.py, models.py) saling terhubung dalam membentuk sebuah alur request–response yang utuh.