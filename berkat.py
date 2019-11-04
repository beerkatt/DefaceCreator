#!/usr/bin/python
import os

os.system ('pkg install figlet -y')
os.system ('clear && sleep 3')
os.system ('figlet BerkaTools')
print ("Gretz : Rabbit Cyber Team")
nick = input("Nick : ")
brkt = open("berkat.html","w")

brk1 = """<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=Windows-1254" /> 
<link href='https://fonts.googleapis.com/css?family=Shadows+Into+Light' rel='stylesheet' type='text/css'>
<title>[+]~HaCKeD By """
brk2 = nick
brk3 = """</title>
<link rel="icon" type="image/png" href="http://185.122.201.106/i.ico" />
</head>
 <body bgcolor=black><table width=100% height=100%><td align=center><span style='font: 55px tahoma;size:55px;color:#ffffff;text-shadow: 10px 10px 10px;'><font style="font-family: 'Shadows Into Light', cursive;">Hacked By """
brk4 = nick
brk5 = """</span></font></center>
</body></html>"""

brkt.write(brk1)
brkt.write(brk2)
brkt.write(brk3)
brkt.write(brk4)
brkt.write(brk5)
brkt.close()
