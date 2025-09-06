from utils import konversi_suhu

print ("=== KONVERSI SUHU ===")
nilai = float(input("Masukkan nilai suhu:"))
dari = input ("Dari satuan (C/F/K): ").strip()
ke = input ("Ke satuan (C/F/K): ").strip()

hasil = konversi_suhu(nilai, dari, ke)

if isinstance(hasil, str):
    print (hasil)
else:
    print (f"Hasil: {nilai}°{dari.upper()} = {hasil:.2f}°{ke.upper()}")