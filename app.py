import win10toast
import requests
import time
from bs4 import BeautifulSoup

def show_notification(map):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('CSGO Current Map Notifier','The map has changed to ' + map,'./steam.ico',duration=5)

def get_map():
    ip_addres = 'ip_addres'
    port = '27015'
    link = 'https://www.gametracker.com/server_info/' + ip_addres +':'+ port + '/'
    r = requests.get(link)
    source = BeautifulSoup(r.content,'html.parser')
    return(source.find("div",attrs={"class":"si_map_header"}).text)

current_map=''
while True:
    if(current_map!=get_map()):
        current_map = get_map()
        show_notification(current_map);
    
    time.sleep(60)

