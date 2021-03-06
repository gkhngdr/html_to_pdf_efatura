import re
from bs4 import BeautifulSoup
import os
import time
import pdfkit
from zipfile import ZipFile
from pathlib import Path
sayı = 0
current_dir = os.getcwd()
t=1
while True:
    old_file_1 = input("SÜRÜKLE:")
    old_file = old_file_1.strip("\"")
    all_of_them = old_file.split("\\")
    name_of_folder = all_of_them[-1].split(".")
    if all_of_them[-1] == "DOSYA":
        try:

            for all_zips in os.listdir(rf"{old_file}"):
                if Path(rf"{current_dir}\\ziplenmiş").is_file():
                    os.rmdir(rf"{current_dir}\\ziplenmiş")



                with ZipFile(f'{old_file_1}\\{all_zips}', 'r') as zipObj:
                    # Get a list of all archived file names from the zip
                    listOfFileNames = zipObj.namelist()


                    # Iterate over the file names
                    for fileName in listOfFileNames:
                        # Check filename endswith csv
                        if fileName.endswith('.html'):
                            # Extract a single file from zip

                            zipObj.extract(fileName, 'ziplenmiş')

                for filename in os.listdir(rf"{current_dir}\\ziplenmiş"):
                    print(filename)
                    file = open(f"{current_dir}\\ziplenmiş\\{filename}", encoding="UTF-8").read()
                    soup = BeautifulSoup(file, "html.parser")

                    colum =soup.select("#customerPartyTable > tbody > tr > td > table > tbody > tr:nth-child(2) > td")[0]
                    name_buyer = colum.getText()
                    name_buyer = name_buyer.strip()
                    print(name_buyer)
                    #liste1 = soup(text=re.compile("[A-ZĞŞİÜÖÇ][a-zA-ZğĞşŞıİüÜöÖçÇ]+.[A-ZĞŞİÜÖÇ][a-zA-ZğĞşŞıİüÜöÖçÇ]+"))
                    #a = liste1.index("SAYIN")
                    #real_index = a+1
                    #name_buyer = liste1[real_index]

                    os.rename(rf'{current_dir}\\ziplenmiş\\{filename}', rf'{current_dir}\\{name_buyer}.html')
                    if not os.path.exists(rf'{current_dir}\\PDFS\\{name_buyer}.pdf'):
                        if os.path.exists('PDFS'):
                            pdfkit.from_file(f'{name_buyer}.html', rf'{current_dir}\\PDFS\\{name_buyer}.pdf')
                            os.rmdir("ziplenmiş")
                            os.remove(f"{name_buyer}.html")
                        else:
                            os.mkdir(rf'{current_dir}\\PDFS')
                            pdfkit.from_file(f'{name_buyer}.html', rf'{current_dir}\\PDFS\\{name_buyer}.pdf')
                            os.rmdir("ziplenmiş")
                            os.remove(f"{name_buyer}.html")
                    else:
                        if os.path.exists('PDFS'):
                            t=t+1
                            pdfkit.from_file(f'{name_buyer}.html', rf'{current_dir}\\PDFS\\{t}.sipariş{name_buyer}.pdf')
                            os.rmdir("ziplenmiş")
                            os.remove(f"{name_buyer}.html")
                        else:
                            os.mkdir(rf'{current_dir}\\PDFS')
                            pdfkit.from_file(f'{name_buyer}.html', rf'{current_dir}\\PDFS\\{t}.sipariş{name_buyer}.pdf')
                            os.rmdir("ziplenmiş")
                            os.remove(f"{name_buyer}.html")

        except UnicodeError:
            print("gardaşşş bi sıkıntı var")
            sayı = sayı+1
            time.sleep(1)
            os.rename(rf'ziplenmiş\\{filename}', rf'{current_dir}\\isimde hata{sayı}.html')
            pdfkit.from_file(f'isimde hata{sayı}.html', rf'{current_dir}\\PDFS\isimde hata{sayı}.pdf')
            os.rmdir("ziplenmiş")
            os.remove(f"isimde hata{sayı}.html")

            continue
        except Exception as e:
            print(e)
            time.sleep(2)


    else:
        try:

            first = name_of_folder[0]
            tail = name_of_folder[1]
            #C:\Users\GökhanGider\Desktop\HAKAN\daca5757-6ef6-4328-8051-7d9c4554bb8d_f.zip
            with ZipFile(f'{old_file}', 'r') as zipObj:
                # Get a list of all archived file names from the zip
                listOfFileNames = zipObj.namelist()

                # Iterate over the file names
                for fileName in listOfFileNames:
                    # Check filename endswith csv
                    if fileName.endswith('.html'):
                        # Extract a single file from zip

                        zipObj.extract(fileName, f'{first}')
            for filename in os.listdir(rf"{current_dir}\\{first}"):
                print(filename)
                file = open(f"{first}\\{filename}", encoding="UTF-8").read()
                soup = BeautifulSoup(file, "html.parser")

                colum = soup.select("#customerPartyTable > tbody > tr > td > table > tbody > tr:nth-child(2) > td")[0]
                name_buyer = colum.getText()
                name_buyer = name_buyer.strip()
                print(name_buyer)
                os.rename(rf'{first}\\{filename}', rf'{current_dir}\\{name_buyer}.html')
                print(name_buyer)
                pdfkit.from_file(f'{name_buyer}.html', f'{name_buyer}.pdf')
                os.rmdir(f"{first}")
                os.remove(f"{name_buyer}.html")

        except UnicodeError:
            print("gardaşşş bi sıkıntı var")
            sayı = sayı+1
            time.sleep(1)
            os.rename(rf'{first}\\{filename}', rf'{current_dir}\\{sayı}.html')
            pdfkit.from_file(f'isimde hata{sayı}.html', f'isimde hata{sayı}.pdf')
        except Exception as e:
            print(e)
            time.sleep(2)
#ğĞşŞıİüÜöÖçÇ
#pattern = re.compile(r'[A-Z][a-zA-Z]+.[A-Z][a-zA-Z]+')
#b = pattern.findall(file)
#print(b)
#[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+
