import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



# --- PENAMBAHAN 1: FUNGSI DATABASE ---
# Fungsi ini untuk memastikan database dan tabel 'pengguna' tersedia
def init_db():
    conn = sqlite3.connect('data_user.db')
    cursor = conn.cursor()
    # Membuat tabel jika belum ada. Kita simpan id (otomatis) dan nama.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengguna (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Jalankan inisialisasi database saat aplikasi dimulai
init_db()

@app.route('/')
def index():
    # --- PENAMBAHAN: AMBIL DATA UNTUK DITAMPILKAN ---
    conn = sqlite3.connect( 'data_user.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nama FROM pengguna ORDER BY id DESC') # Urutkan dari yang terbaru
    semua_nama = cursor.fetchall() 
    conn.close()
    
    # Kirim data 'semua_nama' ke login.html dengan variabel 'daftar_nama'
    return render_template('login.html', daftar_nama=semua_nama)



# --- PENAMBAHAN 2: LOGIKA LOGIN & SIMPAN DATA ---
# Route ini menyesuaikan atribut ACTION di HTML Anda (/login)
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Mengambil input berdasarkan atribut NAME di HTML Anda ("nm")
        user_name = request.form['nm']
        
        # PROSES SIMPAN KE SQLITE
        if user_name:
            conn = sqlite3.connect('data_user.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO pengguna (nama) VALUES (?)', (user_name,))
            conn.commit()
            conn.close()
        
        # Menggunakan render_template untuk menampilkan hasil ke halaman sukses
        # Sesuai permintaan Anda "ganti ke render_template"
        return render_template('success.html', name=user_name)
    
    # Jika diakses lewat GET, kita kembalikan ke form awal
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    # Route ini tetap ada sesuai struktur lama Anda, tapi menggunakan render_template
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)