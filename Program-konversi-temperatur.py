# Program konversi celsius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# Input suhu dalam celcius
celcius = float(input('masukan suhu dalam celcius: '))
print('suhu dalam celcius: ', celcius, 'C')

# Reamur
reamur = (4/5) * celcius
print('suhu dalam reamur: ', reamur, 'R')

# Fahrenheit
fahrenheit = (9/5) * celcius + 32
print('suhu dalam fahrenheit: ', fahrenheit, 'F')

# Kelvin
kelvin = celcius + 273.15
print('suhu dalam kelvin: ', kelvin, 'K')






print("\nPR PROGRAM KONVERSI TEMPERATUR\n")

# PR Program Fahrenheit ke kelvin
f_input = float(input('masukan suhu dalam fahrenheit: '))
f_to_c = 5 / 9 * (f_input - 32)
cH_to_k = f_to_c + 273.15
print('suhu fahrenheit ke celcius: ', f_to_c, 'C')
print('suhu fahrenheit ke kelvin: ', cH_to_k, 'K')

# PR Program kelvin ke fahrenheit
k_input = float(input('\nmasukan suhhu dalam kelvin: '))
k_to_c = k_input - 273.15
cH_to_f = (9 / 5) * k_to_c + 32
print('suhu kelvin ke celcius: ', k_to_c, 'C')
print('suhu kelvin ke fahrenheit: ', cH_to_f, 'F')
