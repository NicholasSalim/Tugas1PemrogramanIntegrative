import math

def main():
    
    salary = float(input("Gaji per tahun : "))

    gajibulanan = math.ceil(salary / 12)

    print("Gaji per bulanmu adalah : ", gajibulanan)


main()
