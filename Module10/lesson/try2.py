from threading import Thread
from datetime import datetime
import  requests

time_start = datetime.now()
THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []
args = THE_URL

def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)


first = Thread(target=func, args=(THE_URL,))
second = Thread(target=func, args=(THE_URL,))
third = Thread(target=func, args=(THE_URL,))

first.start()
second.start()
third.start()

first.join()
second.join()
third.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

print(res)