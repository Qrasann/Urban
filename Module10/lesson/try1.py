import requests
from datetime import datetime
time_start = datetime.now()

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

res = []

for i in range(3):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
print(res)