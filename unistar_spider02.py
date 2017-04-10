#######################################################################################################################
#                                                                                                                     #
#                                                                                                                     #
#                                           unistar шерше-ля-фам                                                      #
#           (c) 2016 by Sergey Streltsov aka Mantikor ver. 0.0.2b support: mantikor@tut.by                            #
#                                                                                                                     #
#                                                                                                                     #
#######################################################################################################################

import time
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool
import webbrowser
from datetime import datetime


def check_url(target):
    try:
        urllib.request.urlopen(target)
        webbrowser.open(target)
    except:
        pass
    return 0

old_pic = {'044', '140', '703', 'a56', 'bb1', 'd3b', 'e56', '663'}

fuck_unistar = {'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
#fuck_unistar = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
urls = []

start_time = datetime.now().strftime('%d-%B-%Y-%H:%M:%S')

for x in fuck_unistar:
    for y in fuck_unistar:
        for z in fuck_unistar:
            fold_name = str(x) + str(y) + str(z)
            if fold_name not in old_pic:
                url = 'http://unistar.by/upload/medialibrary/' + fold_name + '/camp-craze-event-ticket4.png'
                pic_name = fold_name + '_' + 'camp-craze-event-ticket4.png'
                urls.append(url)

# print(len(urls))

pool = ThreadPool(16)

# Open the urls in their own threads
# and return the results
results = pool.map(check_url, urls)

#close the pool and wait for the work to finish
pool.close()
pool.join()

print(start_time)
print(datetime.now().strftime('%d-%B-%Y-%H:%M:%S'))
