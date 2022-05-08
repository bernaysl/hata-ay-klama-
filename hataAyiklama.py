#hata ayıklama
try:
    sayi=int(input("sayi giriniz: "))
    print(sayi)

except ValueError: #valueError hatasında bu mesaj gösterilecek
    print("geçersiz sayi.")