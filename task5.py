def main():
    List = [] 

    print("Input angka (ketik -1 untuk jalankan program):")

    while True:
        angka = int(input()) 
        if angka == -1:
            break  
        List.append(angka)  

 
    total = sum(List)

    print("Jumalh semua angka adalah :", total)


main()