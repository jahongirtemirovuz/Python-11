# 1. Sizga bo'shliqlar (bir bo'shliq) bilan ajratilgan so'zlar va raqamlardan iborat qator beriladi. So'zlar faqat harflardan iborat. Satrda ketma- ket uchta so'z borligini tekshirishingiz kerak . Masalan, “5 one two three 7” qatorida ketma-ket uchta so‘z bor.

# Kirish: so'zlardan iborat qator.
# Natija: mantiqiy javob. (True yoki False)

# Misol:
# assert uchta("Salom dunyoga salom") == True
# assert uchta("U 123 kishi") == False  
# assert uchta("1 2 3 4") == False  
# assert uchta("bla bla bla bla") == False

# U qanday ishlatiladi: Bu sizga satrlar bilan ishlashni o'rgatadi va ba'zi foydali funktsiyalarni taqdim etadi.

# Old shart: Kiritilgan so'zlar va/yoki raqamlar mavjud. Aralash so'zlar yo'q (harflar va raqamlar birlashtirilgan).
# 0 < len (so'zlar) < 100

# Yechilishi




# 2. Raqamni so'zga aylantirish funksiyasi yaratilinishi kerak!

# Misol:
# assert numtotext(1) == "bir"
# assert numtotext(2) == "ikki"  
# assert numtotext(3) == "uch"  
# assert numtotext(20) == "yigirma"

# Sonlar sharti: 0 dan 20 gacha bo'lishi kerak!

# Yechilishi
def int_to_string(number):
    num_dict = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    num_str = str(number)
    result = ""
    for digit in num_str:
        result += num_dict[int(digit)] + ""
        return result.rstrip()
    
print(int_to_string(7))


# 3. So'zni CamelCase ga aylantirish! Ichida berilgan so'zni  "my_func" dan MyFunc ga aylantirishi kerak!

# Misol:
# assert tocamel("zero_coding") == "ZeroCoding"
# assert tocamel("most_wanted_word") == "MostWantedWord"  
# assert tocamel("most_popular_programming_language") == "MostPopularProgrammingLanguage"  

# Yechilishi
def capitalize_first_letter(string):
    return string.capitalize()

print(capitalize_first_letter("zero coding"))
