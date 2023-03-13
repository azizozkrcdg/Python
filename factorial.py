number = int(input("Bir doğal sayı giriniz : "))
originalNumber = number
if number >= 0:
    total = 1

    while number > 0:
        total *= number
        number -= 1
    print("{}! = {}".format(originalNumber,total))
else:
    print("Lütfen doğal bir sayı girin!")