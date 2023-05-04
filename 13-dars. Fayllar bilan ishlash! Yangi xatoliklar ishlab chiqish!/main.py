""" FAYLLAR BILAN ISHLASH. YANGI XATOLIKLARNI ISHLAB CHIQISH! """

################################################################################
""" FAYLLAR BILAN ISHLASH """

""" open() funksiyasi yordamida fayllarni yaratish va ma'lumot yozish! """
file = open("test.txt", "w")
file.write("Hello, world!")
file.close()

""" open() funksiyasi yordamida fayllarni o'qish! """
file = open("test.txt", "r")
print(file.read())
file.close()

""" open() funksiyasi yordamida fayllarga ma'lumot qo'shib qo'yish! """
file = open("test.txt", "a")
file.write("\nHello, world!")
file.close()

""" open() funksiyasi yordamida (boshqa turdagi fayllarni) ochish! """
""" Bu yerda rasmni o'qib, uni byte'larini chiqarib beramiz! """
try:
    with open("unnamed.png", "rb") as f:
        byte = f.read(1)
        while byte:
            byte = f.read(1)
            print(byte)

# """ Xatolik yuzaga kelganda """
except IOError:
    print('Error While Opening the file!')

""" open() funksiyasi yordamida (boshqa turdagi fayllarga) yozish! """
""" Bu yerda rasmni o'qib, uni byte'larini chiqarib beramiz! """
with open("unnamed.png", "rb") as f:
    binary_data = f.read()

""" Byte'larni qayta rasm (PNG) fayliga yozamiz! """
with open("image_name.png", "wb") as img:
    img.write(binary_data)
################################################################################

################################################################################
""" YANGI XATOLIKLARNI ISHLAB CHIQISH! """

""" raise yordamida xatolikni o'zimiz yaratamiz! """
a = int(input("Istalgan son kiriting: "))
if a < 0:
    raise ValueError("Siz manfiy son kiritdingiz!")
else:
    print(a)

""" raise yordamida yana bitta xatolik yaratamiz! """
def daraja(number, exponent):
    if exponent < 0:
        raise ValueError("Musbat son kiriting!")
    return number ** exponent
print(daraja(5, 2))
print(daraja(5, -2))
################################################################################