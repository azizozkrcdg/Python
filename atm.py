_password = "377266"
rightToTry = 3
balance = 500
isLogin = False

while True:

    if not isLogin:
        password = input("Kart şifresini giriniz : ")

    if _password == password:
        isLogin = True
        print("*** Banka Hoşgeldiniz")
        print("""
        1 - Para Çekme
        2 - Para Yatırma
        3 - Bakiye Sorgulama
        4 - Kart İade
        """)
        
        selected = int(input("Lütfen yapmak istediğiniz işlemi seçin : "))

        if selected == 1:
            amountOfMoney = int(input("Çekmek istediğiniz para miktarını giriniz : "))
            if balance >= amountOfMoney:
                balance -= amountOfMoney
                print("{} TL çekme işlemi başarıyla gerçekleştirildi. Güncel bakiyeniz {} TL".format(amountOfMoney, balance))
                print()
            else:
                print("Yetersiz bakiye!")
                print()
                
        elif selected == 2:
            depositAmount = int(input("Yatırmak istediğiniz para miktarını giriniz : "))
            balance += depositAmount
            print("{} TL yatırma işleminiz başarıyla gerçekleştirildi. Güncel bakiyeniz {} TL".format(depositAmount, balance))
            print()
        elif selected == 3:
            print("Güncel bakiyeniz : {} TL".format(balance))
            print()
        elif selected == 4:
            print("Görüşmek üzere!")
            break
    
    else:
        rightToTry -= 1
        print("Lütfen şirfenizi kontrol ediniz \n kalan deneme hakkı {}".format(rightToTry))
        if rightToTry == 0:
            print("Kartınız bloke edilmiştir! Lütfen bankanızla iletişime geçiniz.")
            break