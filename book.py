import pyautogui as pag
import sys
import time
url = "https://cx.indianoil.in/webcenter/portal/Customer/pages_landingpage"
username='your username'
password = 'your password'

#open browser
pag.PAUSE=2
pag.moveTo(x=510,y=750)
pag.click()

#enter url
time.sleep(5)
pag.moveTo(x=600,y=50)
pag.click()
pag.typewrite(url)
pag.press('enter')

#Enter username
time.sleep(5)
pag.moveTo(x=600,y=390)
pag.click()
pag.typewrite(username)
pag.moveTo(x=575,y=460)
pag.click()

#Enter password
time.sleep(5)
pag.moveTo(x=600,y=385)
pag.click()
pag.typewrite(password)
pag.moveTo(x=520,y=500)
pag.click()
time.sleep(5)
pag.moveTo(x=600,y=580)
pag.click()
time.sleep(5)
pag.moveTo(x=200,y=360)
pag.click()
time.sleep(5)
pag.moveTo(x=175,y=290)
pag.click()
time.sleep(5)
pag.moveTo(x=260,y=560)
pag.click()
time.sleep(5)
pag.moveTo(x=396,y=573)
pag.click()
pag.moveTo(x=215,y=628)
pag.click()
pag.moveTo(x=1358,y=718)
for i in range(7):
    pag.click()
pag.moveTo(x=220,y=370)
pag.click()
time.sleep(10)
pag.moveTo(x=1360,y=115)
for i in range(7):
    pag.click()
pag.moveTo(x=1224,y=170)
pag.click()
pag.moveTo(x=1200,y=253)
pag.click()


