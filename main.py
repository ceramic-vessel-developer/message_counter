from bs4 import BeautifulSoup
import os

def counter(file, usr_name):
    try:
        page=open(file)
        html=BeautifulSoup(page)
        if html.select('div.pam:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)'):
            """
            CODE FOR ONE PERSON CONVERSATION
            """
            usr_m = 0
            usr_char = 0
            con_m = 0
            con_char = 0
            conv=html.select('div.pam')
            for i in range(len(conv)):
                if conv[i].select_one('div._2pio').text.lower()==usr_name.lower():
                    usr_m+=1
                    usr_char+=len(conv[i].select_one('div._2let > div:nth-child(1) > div:nth-child(2)'))
        else:
            """
            CODE FOR GROUP CONVERSTIONS
            """
            #TODO napisz kod do liczenia rozmów grupowych


    finally:
        page.close()


path=input('Write the path to the fb data folder: ')
name=input('Write in your name: ')
os.chdir(path+'/messages/inbox')
conversations=os.listdir()
print(conversations)
#TODO zrób sortowanie folderów i wywoływanie funkcji do plików
#TODO wymyśl w jaki sposób podawać obliczenia końcowe (może excel)

