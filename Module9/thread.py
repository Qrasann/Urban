import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)
        time.sleep(1)

number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

number_thread.start()
letter_thread.start()

number_thread.join()
letter_thread.join()
