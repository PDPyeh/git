#memanggil libray tkinter ,ini digunakan untuk membuat GUI di Python.
import tkinter as tk
#messagebox Digunakan untuk menampilkan pesan berbentuk box gitu biasanya untuk memunculkan error.
from tkinter import messagebox
#saya menggunakan library PIL untuk bisa import image di background GUInya.
from PIL import Image, ImageTk

#Membuat fungsi prediksi prodi pilihan
def show_prediction():
    try:
        
        for entry in entries:
            #Mengambil nilai dari setiap Entry dan mengkonversi nilainya menjadi integer.
            nilai = int(entry.get())
            #Memeriksa apakah nilai berada dalam rentang 0 hingga 100. Jika tidak, sebuah pengecualian (ValueError) akan dilempar.
            if not (0 <= nilai <= 100):
                raise ValueError(f"Nilai mata pelajaran {i+1} harus berupa angka antara 0 - 100.")
        #Jika tidak ada kesalahan, sistem akan menampilkan hasil prediksi "Prodi Pilihan: Teknologi Informasi".
        hasilprediksi.config(text="Prodi Pilihan: Teknologi Informasi")
    #Menampilkan pesan kesalahan jika nilai yang dimasukkan tidak valid.
    except ValueError as ve:
        messagebox.showerror("Error bang", f"eror: {ve}")

#Membuat Window utama untuk menjalankan program dengan tkinter
root = tk.Tk()
#title untuk judul dari window tersebut
root.title("Aplikasi Prediksi Prodi Pilihan")
#geometry untuk menetapkan ukuran window 
root.geometry("1920x1080")

#membuat background image untuk aplikasi tkinternya *custom sendiri
background_image = Image.open(r"D:\Editing\RENDERS\Text WAlLpaper (0-00-00-06).png") 
background_image = background_image.resize((1920, 1080)) 
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1) 

#membuat judul besar di window aplikasi
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Bodo Amat", 16))
title_label.pack(pady=10)


entry_labels = []
entries = []

#membuat loop untuk input nilai (10 nilai jadi {i+1})
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", font=("Archivo",12))
    label.pack(pady=5)
    entry_labels.append(label)

    #membuat kotak input untuk dimasukan nilai
    entry = tk.Entry(root)
    entry.pack(pady=5)
    entries.append(entry)

#membuat button untuk menampilkan hasil prediksi
predict_button = tk.Button(root, text="Hasil Prediksi", font=("Archivo",8), command=show_prediction)
predict_button.pack(pady=20)

#menampilkan hasil prediksi
hasilprediksi = tk.Label(root, text="", font=("Archivo", 14, "bold"))
hasilprediksi.pack(pady=10)

# Menjalankan GUI
root.mainloop()

#---------------

