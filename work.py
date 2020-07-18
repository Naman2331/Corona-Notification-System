# project on corona notification system
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon= "C:\\Users\\NAMAN SINGLA\\Desktop\\new_projects\\corona_notification_system\\icon.ico",
        timeout=10
    )
def getdata(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
    # notifyme('naman','hello')
    myhtml=getdata('https://www.mohfw.gov.in/')
    # print(myhtml)
    datastr=""
    soup = BeautifulSoup(myhtml, 'html.parser')
    for tr in soup.find_all('tbody'):
        datastr+=tr.get_text()
    datastr=datastr[2:]
    itemlist=datastr.split('\n\n\n')

    states=['Haryana']
    for item in itemlist[0:35]:
        datalist=item.split('\n')
        if datalist[1] in states:
            print(datalist)
            ntitle="Cases of Covid-19"
            ntext=f"State:{datalist[1]}\nTotal:{datalist[5]}\nDeaths:{datalist[4]}\nActive Cases:{datalist[2]} & Cured:{datalist[3]}"
            notifyme(ntitle,ntext)
            time.sleep(2)


# Made by Naman Singla
# Project Requirements:-
# 1. Python-3.8.3
# 2.pip install bs4 for web scraping
# 3.pip install plyer for notification
