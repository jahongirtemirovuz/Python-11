###############################################--FizzBuzz GAME--############################################
a = int(input("Son kiriting: "))
if (a % 3 == 0 and a % 5 == 0):
    print("FIZZBUZZ")
elif (a % 3 == 0):
    print("FIZZ")
elif (a % 5 == 0):
    print("BUZZ")
else:
    print("XATOLIK!")




###############################################--ADMIN DASTURI--############################################
name = input("Ism va familiyani kiriting: ")
login = input("Loginni kiriting: ")
password = input("Parolni kiriting: ")
email = input("E-pochtani kiriting: ")

login=="2007"
password=="12345"
email=="jahongiruz@gmail.com"

if login=="2007" and password=="12345" and email=="jahongiruz@gmail.com":
    print(f"Xush kelibsiz! {name}")
else:
    print("Qayta urining!")



###############################################---So'z yasash---############################################
print("MEXANIZATSIYALASHTIRISHMOQCHILIGINIAYTGANINIBILIBQOLDIM" [0:13])
print("MEXANIZATSIYALASHTIRISHMOQCHILIGINIAYTGANINIBILIBQOLDIM" [45:49])



#############################################----Calculator----#############################################
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
opt = input("Amal kiriting (+, -, /, *, %): ")

if opt=="+":
    print(a + b)
elif opt=="-":
    print(a - b)
elif opt=="/":
    print(a / b)
elif opt=="*":
    print(a * b)
elif opt=="%":
    print(a % b)
else:
    print("Wrong!")


# ###############################################----Kvadratga oshirish----#################################
print("\t\t\t\tDarajaga ko'taruvchi dastur")
a = int(input("Sonni kiriting: "))
b = int(input("Darajani kiriting: "))
print(a ** b)

