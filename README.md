# info-mata-kuliah-deo
## Setup
**Database**<br>
Terlebih dahulu, import sql ke MySQL, pada pengujian mengunakan XAMPP. Jika MySQL nya default dari XAMPP tidak ada perubahan, tanpa mengubah kodingan, sudah bisa terhubung, namun bila ada setting khusus, bisa diubah di baris ke 7 file app.py <br>
```'mysql+pymysql://root:@localhost:3306/info_mata_kuliah'```<br>
dengan format<br>
```'mysql+pymysql://<username>:<password>@localhost: <database port>/<database name>'```<br>
<br>
**Python**<br>
Disarankan menjalankan program di virtual environment python untuk meminimalisir error karena beda versi framework atau library <br>
Di sini dicontohkan menggunakan virtualenvwrapper, pertama, membuat environment baru
```bash
$ mkvirtualenv test
```
test adalah nama environmentnya, bisa diganti sesuai dengan kebutuhan, setelah itu, secara otomatis, akan berjalan environment test di terminal <br>
Jika mau memulai environment yang sudah ada, bisa dengan perintah
```bash
$ workon test
```
Setelah itu, clone repositori github
```bash
$ git clone https://github.com/syarifhilmi/info-mata-kuliah-deo.git
$ cd info-mata-kuliah-deo
```
Install depedensi yang dibutuhkan
```bash
$ pip install -r requirements.txt
```
Untuk menjalankan server di local
```bash
$ flask run
```
Secara default flask akan berjalan di localhost:5000
## Endpoint API
Mengambil data info mata kuliah (kode,nama mata kuliah, sks,) per semester berdasarkan tahun dan prodi <br>
**GET** ```localhost:5000/info-mata-kuliah/<prodi>/<tahun> ```<br>
contoh penggunaan<br>
**GET** ```localhost:5000/info-mata-kuliah/informatika/2016 ```<br>
