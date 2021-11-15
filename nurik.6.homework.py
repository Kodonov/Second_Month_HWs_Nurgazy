import re


file_path = "mock_data.txt"
result_file_path = "@mail.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
mail = open(result_file_path, mode="w", encoding="Latin-1")
my_text_1 = file_reader.read()

searching_mail = r'[\w+_-]+@[\w_-].+[\w.]+'
results_all_mail = re.findall(searching_mail, my_text_1)

for i in results_all_mail:
    print(i)
    mail.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "fullname.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
fullname = open(result_file_path, mode="w", encoding="Latin-1")
my_text_2 = file_reader.read()

searching_fullname = r'[A-Z]+[\w+-]+[a-z A-Z]+[\s]+[A-Z)\s+O\s+[A-Z]+[A-Z}+[\w+-]\w+'


results_all_fullname = re.findall(searching_fullname, my_text_2)

for i in results_all_fullname:
    print(i)
    fullname.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "прочее.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
прочее = open(result_file_path, mode="w", encoding="Latin-1")
my_text_3 = file_reader.read()

searching_прочее = r'[A-Z]\w+[.]+[a-z 0-9 a-z]\w+'


results_all_прочее = re.findall(searching_прочее, my_text_3)

for i in results_all_прочее:
    print(i)
    прочее.write(i + "\n")




file_path = "mock_data.txt"
result_file_path = "Хэштег.txt"
file_reader = open(file_path, mode='r', encoding='Latin-1')
Хэштег = open(result_file_path, mode="w", encoding="Latin-1")
my_text_4 = file_reader.read()

searching_Хэштег = r'#[\w]+[\d]+'
results_all_Хэштег = re.findall(searching_Хэштег, my_text_4)

for i in results_all_Хэштег:
    print(i)
    Хэштег.write(i + "\n")