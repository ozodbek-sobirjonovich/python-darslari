""" BROWSERLARNI OCHISH. CLI ARGUMENTLAR BILAN ISHLASH. TASHQI KUTUBXONALAR BILAN ISHLASHNI BOSHLASH! """

#####################################################################
# """ BROWSERLARNI OCHISH """

# """ Kutubxonalarni import qilish! """
# import webbrowser
# import time
# import os

# """ Foydalanuvchidan URL ni so'rab olish! """
# # website_url = input("Enter website url: ")

# """ Saytni oldindan kiritib qo'yish! """
# website_url = "https://sensorika.uz/kompyuter-savodxonligi/page/"

# """ Biroz kutish! """
# timer = 3
# while timer > 0:
#     print(timer)
#     timer -= 1
#     time.sleep(1)
#     os.system("cls")

# """ Web Browserni ochish! """
# # webbrowser.open(website_url)

# """ Bir necha marotaba ochish! """
# for i in range(1, 10):
#     webbrowser.open(website_url + str(i))
#     time.sleep(1)
#####################################################################

#####################################################################
""" CLI ARGUMENTLAR BILAN ISHLASH """

#########################################################
# """ Standart kutubxona yordamida argumentlarni olish! """
# import sys

# """ CLI argumentlarni olish! """
# print(sys.argv)

# """ CLI argumentlarni indeksi bo'ylab olish! """
# print(sys.argv[0])
#########################################################

#########################################################
# import os

# """ Kompyuterimizdagi barcha o'zgaruvchilarni olish! """
# print(os.environ)

# """ Kompyuterimizdagi maxsus o'zgaruvchini olish! """
# print(os.environ.get("USERNAME"))
# print(os.environ.get("USERDOMAIN"))
# print(os.getenv("USERNAME"))

# """ .env faylini o'qish """
# """ .env fayli bizga tashqi o'zgaruvchilardan qiymatlarni olishga yordam beradi! """
# """ .env faylidan o'zgaruvchilarni olish! """
# """ Tashqi kutubxonadan foydalanamiz! """

# from dotenv import load_dotenv  # pip install python-dotenv

# """ .env faylini o'qish! """
# load_dotenv()

# """ .env faylidan o'zgaruvchilarni olish! """
# print(os.getenv("MAXSUS_KALIT"))
# print(os.getenv("MAXSUS_PAROL"))
#########################################################

#########################################################
""" CLI argumentlar bilan ishlash uchun biz "tashqi kutubxonalardan birini" o'rnatib olishimiz kerak! """

# https://pypi.org/project/typer/ - pip install "typer[all]"

# """ Tashqi kutubxonalarni chaqirish! """
# import typer

# def main(name: str, age: int, is_married: bool):
#     print(f"My name is {name}, I'm {age} years old. I'm married: {is_married}")

# if __name__ == "__main__":
#     typer.run(main)

# Ishlatish uchun: python main.py Ozodbek 22 False

# """ CLI argumentlarni olish! Standart kutubxona yordamida! """
# import argparse

# """ Argumentlarni olish! """
# parser = argparse.ArgumentParser(description="CLI argumentlarni olish!")

# """ Argumentlarni qo'shish! """
# parser.add_argument("--name", type=str, help="Foydalanuvchi ismini kiriting!")
# parser.add_argument("--age", type=int, help="Foydalanuvchi yoshini kiriting!")
# parser.add_argument("--is_married", type=bool, help="Foydalanuvchi turmush o'rtog'ini kiriting!")

# """ Argumentlarni olish! """
# args = parser.parse_args()

# """ Argumentlarni olish! """
# print(args.name)
# print(args.age)
# print(args.is_married)

""" Topshiriq! """

# Misol uchun 1: python browser.py --url https://www.google.com --open 5
# Misol uchun 2: python browser.py --url https://www.google.com --open 5 --sleep 3

# Shartlari:
# 1. --url argumenti majburiy bo'lishi kerak!
# 2. --open argumenti majburiy bo'lishi kerak!
# 3. --sleep argumenti majburiy bo'lmasligi kerak!
# 4. --sleep argumenti berilmasa, default qiymati 1 bo'lishi kerak!
# 5. --open argumenti berilgan qiymatni int ga o'tkazib olishi kerak!