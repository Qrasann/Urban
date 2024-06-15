from pprint import pprint

file_name = "poem.txt"
file = open(file_name, "r", encoding="utf-8")
print(file.read())
file.close()