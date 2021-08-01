#2021 Kakos lkişselleştirilmiş lisans © Zoda
#Bu kodu kişsel kullanım için modifiye edip yayımlayabilirsiniz

import json
import os
import sys

def add_conf_file(filename):
  file = open(filename, "r")
  filedata = json.load(file)

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
    "php": "apt install php"
  }
  
  
  try:
    if filedata["install_package"] in package_list:
      os.system(filedata["install_package"])
  except KeyError:
    print("İnirilecek paket bulunamadı")

if __name__ == "__main__":
  add_conf_file(sys.argv[1])
