number = int(input("Bir pozitif tam sayı giriniz : "))
originalNumber = number
digitSum = 0
digit = []

if number >= 0:
    while number > 0:
        digitSum += number % 10
        digit.append(number%10)
        number //= 10
    print("{} sayısının rakamları : ".format(originalNumber),end="")
    digit.reverse()
    print(digit)
    print("{} sayısının rakamları toplamı = {}".format(originalNumber,digitSum))
else:
    print("Lütfen pozitif bir sayı giriniz!")