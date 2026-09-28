def convert_temperature (value, unit):
    if (unit == 'c'):
        return (value * 9 / 5) + 32
    elif (unit == 'f'):
        return (value - 32) * 5 / 9
    else:
        return None

input_value = float(input("masukkan value: "))
input_unit = input("masukkan unit (c/f): ")

konversi = convert_temperature(input_value, input_unit)
if (input_unit == 'c'):
    print(f"{input_value} derajat Celsius = {konversi} derajat Fahrenheit")
elif (input_unit == 'f'):
    print(f"{input_value} derajat Fahrenheit = {konversi} derajat Celsius")

#soal2
r = float(input("Masukkan jari-jari lingkaran: "))
def luas_lingkaran(r):
    return 3.14 * r ** 2

luas = luas_lingkaran(r)
print(f"Luas lingkaran: {luas}")