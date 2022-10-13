# Rangkuman sesi 4
Penjelasan Pernyataan Penyeleksian IF
IF adalah salah satu pernyataan penyeleksian yang memungkinkan kita memanipulasi aliran jalannya program berdasarkan conditional expression. Hal ini dapat memungkinkan kita membuat program yang berjalan secara fleksibel sesuai keadaan dari pengguna dan mesin.
Penyeleksian if adalah pernyataan penyeleksian yang mencari kebenaran dari conditional expression yang disebutkan. conditional expression harus berupa bilangan Boolean atau operasi yang menghasilkan bilangan Boolean dan menyatakan benar atau salah atas expression tersebut.
Ketika mesin eksekusi bertemu dengan penyeleksian if maka CPU akan memeriksa kebenaran dari conditional expression yang disebutkan, jika benar (true) maka perintah yang ada di dalamnya akan dijalankan, jika salah (false) maka akan memeriksa pernyataan else if (jika ada), hal itu dilakukan berulang satu demi satu hingga menemukan kondisi yang bernilai benar (true). Jika tidak ditemukan maka akan melakukan perintah pernyataan else.

Nested IF
Merupakan hal yang dimungkinkan dalam bahasa pemrograman C++ yaitu membuat pernyataan IF di dalam pernyataan IF. hal ini dapat memungkinkan anda untuk membuat tahapan penyeleksian yang berlipat-lipat.
Contoh Program :
Pernyataan percabangan digunakan untuk memecahkan persoalan untuk
mengambil suatu keputusan diantara sekian pernyataan yang ada
Dalam bahasa C++ terdapat beberapa perintah, diantaranya adalah :
1. Pernyataan IF
2. Pernyataan IF – ELSE
3. Pernyataan NESTED IF
4. Pernyataan IF – ELSE Majemuk
5. Pernyataan SWITCH - CASE

PERBEDAAN IF DAN SWITCH]
Flow Control ( IF Dan Switch)
Flow control (struktur kendali) dapat dibagi menjadi dua jenis yaitu , Struktur percabangan dan pengulangan (looping). Namun kali ini akan membahas struktus percabangan. Percabangan adalah perintah yang memungkinkan pemilihan atas perintah yang akan dijalankan sesuai dengan kondisi tertentu yang menentukan alur perjalanan program. Percabangan bertujuan untuk memilih atau mengkondisikan apakah statement tersebut akan dijalankan atau tidak. Percabangan seperti operasi logika, jika diberi sebuah pernyataan, dan pernyataan tersebut benar, maka program akan menjalankan statement-statement yang telah ditentukan.

Ada tiga macam perintah percabangan, yaitu if, if … else, dan switch.
1. IF
If digunakan untuk satu kondisi saja. Jika pernyataan benar (terpenuhi) maka akan dijalankan, jika salah (tidak terpenuhi) maka diabaikan.

2. IF … ELSE
Perintah ini digunakan untuk lebih dari satu kondisi. Seperti biasa, perintah1 dan perintah2 bisa berbentuk blok yang terdiri dari beberapa perintah. Pernyataan if merupakan bentuk percabangan 2 arah, jika kondisi yang diuji tersebut terpenuhi, maka program akan menjalankan pernyataan-pernyataan tertentu. Jika kondisi yang diuji salah, program akan menjalankan pernyataan yang lain.

3. SWITCH
Perintah ini digunakan sebagai alternatif pengganti dari sintaks if … else dengan else lebih dari satu. Switch, kondisi hanya dinyatakan dengan bilangan bulat atau karakter/string. Dengan perintah ini program percabangan akan semakin mudah dibuat dan dipelajari. Perintah switch akan menyeleksi kondisi yang diberikan dan kemudian membandingkan hasilnya dengan konstanta-konstanta yang berada di case. Pembandingan akan dimulai dari konstanta 1 sampai konstanta terakhir. Jika hasil dari kondisi terpenuhi dengan nilai konstanta tertentu, misalnya konstanta 1 , maka pernyataan 1 akan dijalankan sampai ditemukan break. Pernyataan break akan membawa proses keluar dari perintah switch, agar eksekusi dilakukan pada kondisi yang terpenuhi saja, jika telah terpenuhi maka dihentikan. Jika hasil dari kondisi tidak terpenuhi dengan konstanta-konstanta yang diberikan, maka pernyataan pada default akan dijalankan.