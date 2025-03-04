
from subprocess import run
import requests
import os

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')

H = "DEV:"

sif = render(f'{H}', colors=['white', 'green'], align='center')
print(sif)

M = "Mr.Hackenz"
sif = render(f'{M}', colors=['white', 'green'], align='center')
print(sif)

while True:
  command = input("Kroch~*")
  if command.lower( )   ==  "خروج ":
   	exit()
  try:
  	   run(command)
  except:
  	   print("error <It's wrong>هناك خطاء في هاذا الامر الرجاء كتابه الامر بشكل صحيح")
  	   