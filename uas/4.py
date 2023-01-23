import mysql.connnector

# Koneksi ke database
db = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = '',
)
if is_connected():
  print("berhasil")