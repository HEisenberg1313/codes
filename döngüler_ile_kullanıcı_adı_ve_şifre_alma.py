print("""*********************
SİSTEME GİRİŞ SAYFASI 
*********************
""")

sys_ad = "halit"
sys_sifre = "12345"
deneme = 2

while True:
    ad = input("adınız:")
    sifre = input("şifreniz:")
    if ad != sys_ad and sifre != sys_sifre:
        print("AD VE ŞİFRE HATALIDIR....")
        deneme -= 1
    elif ad == sys_ad and sifre != sys_sifre:
        print("ŞİFRENİZ HATALI!!!!")
        deneme -= 1
    elif ad != sys_ad and sifre == sys_sifre:
        print("ADINIZ HATALIDIR!!!!")
        deneme -= 1
    else:
        print("SİSTEME GİRİŞ YAPILIYOR!!!!")
        break
    if deneme == 0:
        print("deneme hakkınız bitmştir.Ad ve şifrenizi değiştirmek için q'ya basınız.çıkmak için herhangi bir harfe basın.")
        q = input("yapmak istediğiniz işlem:")
        if q == q:
            yeni_ad = input("yeni adınızı giriniz:")
            yeni_şifre = input("yeni şifrenizi giriniz:")
            while True:
                if yeni_ad == sys_ad and yeni_şifre == sys_sifre:
                    print("yeni ad ve şifre eskisi ile aynı olamaz.")
                    continue
                elif yeni_ad == sys_ad and yeni_şifre != sys_sifre:
                    print("yeni ad eskisi ile aynı olamaz.")
                    continue
                elif yeni_ad != sys_ad and yeni_şifre == sys_sifre:
                    print("yeni şifre eskisi ile aynı olamaz.")
                    continue
                else:
                    print("yeni ad ve şifre kaydediliyor....")
                    sys_ad = yeni_ad
                    sys_sifre = yeni_şifre
                    print("yeni ad:",sys_ad,"yeni şifre:",sys_sifre)
                    break
            continue
        else:
            print("ÇIKIÇ YAPILIYOR!!!!!!!!!!!!!!!!!")
            break




