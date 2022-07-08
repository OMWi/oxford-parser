from main import file_load, file_dump

total_list = file_load('total')
names = []
repeated_names = []

repeated_count = 0

for word in total_list:
    if word['name'] in names:
        repeated_names.append(word['name'])
        repeated_count += 1
        print(f'word {word["name"]} repeated')
    names.append(word['name'])

print(f'repeated count {repeated_count}')