from bs4 import BeautifulSoup
import os
import concurrent.futures
import numpy as np
from itertools import repeat

#,bar,label,signal
fulldir=''
processed=0
length=0
def main(path,name,signal,label,bar,finished_signal):
    global fulldir, processed, length

    class Conversation:
        def __init__(self, users, conv_name):
            self.users = users
            self.conv_name = conv_name


    class User:
        def __init__(self, name='', mes=0, char=0):
            self.name = name
            self.mes = mes
            self.char = char


    def counter(file,name,signal):
        global fulldir, processed, length
        with open(file) as page:

            html = BeautifulSoup(page)

            conv = html.select('div.pam')
            conv = np.asarray(conv + [None], dtype=object)[:-1]
            conv_name = html.select_one('._3b0d').text
            fulldir[conv_name] = Conversation({}, conv_name)
            fulldir[conv_name].users[name] = User(name, 0, 0)
            for i in range(2):
                if (not conv[0].select_one('div._2pio')) or (
                not conv[0].select_one('div._2let > div:nth-child(1) > div:nth-child(2)')):
                    conv=np.delete(conv, 0)
            for i in range(len(conv)):
                username = conv[i].select_one('div._2pio').text
                if username not in fulldir[conv_name].users.keys():
                    fulldir[conv_name].users[username] = User(username, 0, 0)
                fulldir[conv_name].users[username].mes += 1
                fulldir[conv_name].users[username].char += len(
                    conv[i].select_one('div._2let > div:nth-child(1) > div:nth-child(2)').text)
        processed += 1
        signal.emit(processed)

        #print(f'Finished processing{file}\n{round((processed / length) * 100, 2)}% completed')


    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0

        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out


    os.chdir(path + '/messages/inbox')
    path = os.getcwd()
    conversations = os.listdir()
    fulldir = {}
    onlyfiles = []
    print(os.getcwd())

    for conv in conversations:
        mypath = os.path.join(path, conv)
        os.chdir(mypath)
        onlyfiles.extend(
            [os.path.join(os.getcwd(), f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))])
    length = len(onlyfiles)
    chunks = chunkIt(onlyfiles, os.cpu_count())
    bar.setMaximum(len(onlyfiles))

    processed = 0
    for chunk in chunks:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(counter, chunk,repeat(name),repeat(signal))
    bar.setValue(bar.maximum())
    label.setText('Processing complete!')
    label.adjustSize()
    finished_signal.emit(False)
    return fulldir.values()
    # fullist = fulldir.values()
    for i in fullist:
        i.users = i.users.values()
    for i in fullist:
        print(f'{i.conv_name}')
        for k in i.users:
            print(f'\t{k.name}\n\t\tmessages: {k.mes}\n\t\tcharacters:{k.char}')
# stop=time.perf_counter()
# print(f'Finished in {stop-start} second(s)')
#TODO try process pool executor


    # TODO skomentuj kod jak człowiek
    # TODO wymyśl w jaki sposób podawać obliczenia końcowe (może excel)
