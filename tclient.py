from telethon import TelegramClient, sync, events
from datetime import datetime, date, time 
import urllib.request as urq
import re
#import slnm
import ocr
import config as cfg

def durl (line):
    return re.search("(?P<url>https?://[^\s]+)", line).group("url")

def curnamef ():
    return datetime.now().strftime("%Y_%m_%d-%H_%M_%S_promo.png")

def picload (url, file_name):
    print(url)
    urq.urlretrieve(url, file_name)
    return file_name


if __name__ == '__main__':
    print(cfg.API_ID)
    print(cfg.API_HASH)
    print(cfg.TGROUP)
    api_id = cfg.API_ID 
    api_hash = cfg.API_HASH 
    tgroup = cfg.TGROUP
    
    client = TelegramClient('WatchPromo', api_id, api_hash)

    @client.on(events.NewMessage(chats=(tgroup)))
    async def normal_handler(event):
        sender = await event.get_sender()
        usname = sender.username
        msg = event.message
        line = msg.message
        lline = line.strip().split()
        #f.write('----------------------------------\n')
        f.write(str(usname)+'\n')
        f.write(str(line)+'\n')
        print('------------------------------------')
        print(usname)
        print(line) 
        if ('промокод' in lline) and ('15$' in lline):
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            #url = durl(line)
            #name_image = curnamef()
            #picload(url, name_image)
            f.write(ocr.img_to_str(picload(durl(line), curnamef()))+'\n')
            print(ocr.img_to_str(picload(durl(line), curnamef())))
        #f.write(msg)
        f.write('----------------------------------\n')
        #print('------------------------------------')
        #print(msg)

        #print(event.message.from_id)



    client.start()
    f = open('data_from_group', 'a')
    client.run_until_disconnected()
    f.close()
