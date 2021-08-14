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
def counter(file,group):
    global conv_members
    page = open(file)
    try:

        html=BeautifulSoup(page)
        if group:
            """
            CODE FOR ONE PERSON CONVERSATION
            """

            conv=html.select('div.pam')
            for i in range(len(conv)):
                username=conv[i].select_one('div._2pio').text
                if username not in conv_members.keys():
                    conv_members[username]=User(username,0,0)
                conv_members[username].mes += 1
                conv_members[username].char += len(
                    conv[i].select_one('div._2let > div:nth-child(1) > div:nth-child(2)').text)

        #else:
            """
            for i in conv_members.keys():
    print(f'{conv_members[i].name}:\n\tmessages: {conv_members[i].mes}\n\tcharacters: {conv_members[i].char}')
            CODE FOR GROUP CONVERSTIONS
            """
            #TODO napisz kod do liczenia rozmów grupowych

    finally:
        page.close()
def conv_maker(files,usr_name):
    global conv_members
    conv_members={}

    conv_members[usr_name]=User(usr_name, 0, 0)
    with open(files[0]) as file:
        html = BeautifulSoup(file)
        chat=Conversation([],html.select_one('._3b0d').text)

        if html.select('div.pam:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)'):
            conv_members[html.select_one('._3b0d').text]=User(html.select_one('._3b0d').text,0,0)
            switch=True


            """ string=html.select_one('div.pam:nth-child(1) > div:nth-child(1)').text
            stringstring.strip()
            names=string.split(', ')
            names.pop(usr_name)
            for name in names:
                conv_members.append(User)"""
            #TODO ogarnij coś z grupami bo to masakra
    for file in files:
        counter(file,switch)





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

