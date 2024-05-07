def bmi():
    input_berat = float(input('Masukan Berat Badan (KG) : '))
    input_tinggi = float(input('Masukan Tinggi Badan (M) : '))
    rumus_bmi = input_berat / (input_tinggi**2)
    if rumus_bmi <= 18.5:
        print ("Berat Badan Kurang")
    elif rumus_bmi <= 24.9:
        print ("Berat Badan Normal")
    elif rumus_bmi <= 29.9:
        print ("Kelebihan Berat Badan")
    else:
        print ("Obesitas")