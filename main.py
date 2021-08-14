from bs4 import BeautifulSoup
import os







path=input('Write the path to the fb data folder: ')
name=input('Write in your name: ')
class Conversation:
    def __init__(self,users,conv_name):
        self.users=users
        self.conv_name=conv_name
class User:
    def __init__(self,name='',mes=0,char=0):
        self.name=name
        self.mes=mes
        self.char=char
def counter(file, usr_name,group):
    page = open(file)
    try:

        html=BeautifulSoup(page)
        if group:
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
                    con_m += 1
                    con_char += len(conv[i].select_one('div._2let > div:nth-child(1) > div:nth-child(2)'))
        else:
            """
            CODE FOR GROUP CONVERSTIONS
            """
            #TODO napisz kod do liczenia rozmów grupowych

        return ['',0]
    finally:
        page.close()
def conv_maker(files,usr_name):
    conv_members={}
    conv_members[usr_name]=User(usr_name, 0, 0)
    with open(files[0]) as file:
        html = BeautifulSoup(file)
        chat=Conversation([],html.select_one('._3b0d').text)

        if html.select('div.pam:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)'):

            conv_members[html.select_one('._3b0d').text]=User(html.select_one('._3b0d').text,0,0)
            switch=True
        else:
           """ string=html.select_one('div.pam:nth-child(1) > div:nth-child(1)').text
            stringstring.strip()
            names=string.split(', ')
            names.pop(usr_name)
            for name in names:
                conv_members.append(User)"""
            #TODO ogarnij coś z grupami bo to masakra jakaś




os.chdir(path+'/messages/inbox')
path=os.getcwd()
conversations=os.listdir()

for conv in conversations:
    temp1=[]
    os.chdir(path+'/'+conv)
    mypath=os.getcwd()
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]




#TODO zrób sortowanie folderów i wywoływanie funkcji do plików
#TODO wymyśl w jaki sposób podawać obliczenia końcowe (może excel)

