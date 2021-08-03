#2021 Kakos lkişselleştirilmiş lisans © Zoda
#Bu kodu kişsel kullanım için modifiye edip yayımlayabilirsiniz

#TODO: install message
import json
import os
import sys

def add_conf_file(filename):
  file = open(filename, "r")
  filedata = json.load(file)

  try:
    print(filedata["message"])
  except KeyError:
    pass
  
  
  try:
    if filedata["install_path"] =="current_path":
      os.chdir(os.getcwd())
    else:
      os.chdir(filedata["install_path"])
  except KeyError:
    print(f"{filename} dosyasında install_path bulunamadı.")
  except FileNotFoundError:
    print(f"{filename} dosyasında belirtilen {filedata['install_path']} klasörü bulunamadı.")
  

  package_list = {
    "Python": "apt install python",
    "python": "apt install python",
    "c": "apt install clang",
    "ruby": "apt install ruby",
    "php": "apt install php",
    "git": "apt install git"
  }
  
  
  try:
    if filedata["install_package"] in package_list:
      os.system(filedata["install_package"])
  except KeyError:
    print("İnirilecek paket bulunamadı")

if __name__ == "__main__":
  try:
    if sys.argv[1] == "run-standart":
      try:
        add_conf_file("install_package.json")
      except FileNotFoundError:
        print("install_package.json dosyası bulunamadı")
    elif sys.argv[1] =="control":
      print("Yakında")
    elif sys.argv[1] == "-h":
      print("Packpy yardım\n\n-h bu mesaj\nrun-standart install_package.json çalıştırılır\n<json dosyayıs> json dosyası çalıştırılır\ncontrol kontrol versiyon")
    else:
      add_conf_file(sys.argv[1])
  except IndexError:
    print("Argüman girilmedi\nyardım için python packpy -h")
