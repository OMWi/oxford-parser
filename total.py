from main import file_load, file_dump
import time

def check_size(list1, list2):
    if len(list1) != len(list2):
        print('sizes are not equal')

list_name1 = 'oxford3000-5000.json'
list_name2 = 'opal.json'
list_name3 = 'oxford-phrase-list.json'

list1 = file_load(list_name1)
list2 = file_load(list_name2)
list3 = file_load(list_name3)

print(f'list 1 size {len(list1)}')
print(f'list 2 size {len(list2)}')
print(f'list 3 size {len(list3)}')

total_list = []
total_list.extend(list1)
link_list = [word['link'] for word in total_list]
check_size(total_list, link_list)
time.sleep(2)

new_words_count = 0
for word in list2:
    if word['link'] in link_list:
        continue
    total_list.append(word)
    link_list.append(word['link'])
    new_words_count += 1
print(f'added {new_words_count} words from list 2')
check_size(total_list, link_list)
time.sleep(2)

new_words_count = 0
for word in list3:
    if word['link'] in link_list:
        continue
    total_list.append(word)
    link_list.append(word['link'])
    new_words_count += 1
print(f'added {new_words_count} words from list 3')
check_size(total_list, link_list)
time.sleep(2)

print(f'total size {len(total_list)}')
file_dump('total', total_list)