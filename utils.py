def konversi_suhu (nilai, dari, ke):
  #nilai: angka suhu yang akan dikonversi
  #dari: satuan asal ("c", "f", "k")
  #ke: satuan tujuan ("c", "f", "k")

  def celcius_ke_fahrenheit (c):
    return (c * 9/5) + 32

  def celcius_ke_kelvin (c):
    return (c + 273.15)

  def fahrenheit_ke_celcius (f):
    return (f - 32) * 5/9

  def fahrenheit_ke_kelvin (f):
    return (f - 32) * 5/9 + 273.15

  def kelvin_ke_celcius (k):
    return (k - 273.15)

  def kelvin_ke_fahrenheit (k):
    return (k - 273.15) * 9/5 + 32

  dari = dari.lower()
  ke = ke.lower()

  if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
      return "Error: Satuan harus 'C', 'F', atau 'K'."

  if dari == "k" and nilai < 0:
      return "Error: Suhu Kelvin tidak boleh negatif."

  if dari == ke:
      return nilai

  if dari == "c" and ke == "f":
      return celcius_ke_fahrenheit(nilai)
  elif dari == "c" and ke == "k":
      return celcius_ke_kelvin(nilai)
  elif dari == "f" and ke == "c":
      return fahrenheit_ke_celcius(nilai)
  elif dari == "f" and ke == "k":
      return fahrenheit_ke_kelvin(nilai)
  elif dari == "k" and ke == "c":
      return kelvin_ke_celcius(nilai)
  elif dari == "k" and ke == "f":
      return kelvin_ke_fahrenheit(nilai)

  return "Error: Konversi tidak tersedia."