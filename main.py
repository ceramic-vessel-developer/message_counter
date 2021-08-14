from bs4 import BeautifulSoup
import os

path = input('Write the path to the fb data folder: ')
name = input('Write in your name: ')


class Conversation:
    def __init__(self, users, conv_name):
        self.users = users
        self.conv_name = conv_name


class User:
    def __init__(self, name='', mes=0, char=0):
        self.name = name
        self.mes = mes
        self.char = char


def counter(file):
    global conv_members
    page = open(file)
    try:

        html = BeautifulSoup(page)

        conv = html.select('div.pam')
        for i in range(2):
            if (not conv[0].select_one('div._2pio')) or (not conv[0].select_one('div._2let > div:nth-child(1) > div:nth-child(2)')):
                conv.pop(0)
        for i in range(len(conv)):
            username = conv[i].select_one('div._2pio').text
            if username not in conv_members.keys():
                conv_members[username] = User(username, 0, 0)
            conv_members[username].mes += 1
            conv_members[username].char += len(
                conv[i].select_one('div._2let > div:nth-child(1) > div:nth-child(2)').text)



    finally:
        page.close()


def conv_maker(files, usr_name):
    global conv_members
    conv_members = {}

    conv_members[usr_name] = User(usr_name, 0, 0)
    with open(files[0]) as file:
        html = BeautifulSoup(file)
        chat = Conversation([], html.select_one('._3b0d').text)


    for file in files:
        counter(file)
    chat.users = conv_members.values()
    return chat


os.chdir(path + '/messages/inbox')
path = os.getcwd()
conversations = os.listdir()
fulllist = []
for conv in conversations:
    os.chdir(path + '/' + conv)
    mypath = os.getcwd()
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    try:
        fulllist.append(conv_maker(onlyfiles, name))
    except Exception as e:
        print(os.getcwd())
        print(e)
for i in fulllist:
    print(f'{i.conv_name}')
    for k in i.users:
        print(f'\t{k.name}\n\t\tmessages: {k.mes}\n\t\tcharacters:{k.char}')

# TODO wymyśl w jaki sposób podawać obliczenia końcowe (może excel)
