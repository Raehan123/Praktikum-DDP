print('''
   silahkan pilih tools dibawah ini dengan mengirimkan nomornya
      =============================================
      tools yang tersedia
      =============================================
      1. Menghitung luas persegi
      2. Menghitung luas lingkaran
      3. Menghitung luas segetiga
      =============================================   
''')

a = int(input("Apa Pilihanmu???"))

match a:
    case 1:
        luaspersegi = int(input("masukan nilai sisi : "))
        hasilluas = luaspersegi * luaspersegi
        print("luas persegi adalah : ", hasilluas )
    case 2:
        nilaiphi = float(input("masukan nilai phi : "))
        nilaijari = int(input("masukan nilai jari jari : "))
        jarijari = nilaijari * nilaijari
        luaslingkaran = nilaiphi * jarijari
        print("luas lingkaran adalah : ", luaslingkaran)
    case 3:
        rumus = float(0.5)
        alas = int(input("masukan nilai alas : "))
        tinggi = int(input("masukan nilai tinngi : "))
        hasilluas = rumus * alas * tinggi
        print("luas segitiga adalah : ", hasilluas)
    case _:
        print("wrong number")