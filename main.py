import requests
from bs4 import BeautifulSoup
import json

from word import Word

# todo: use lxml on parsing
base_url = 'https://www.oxfordlearnersdictionaries.com'

def file_dump(file_name, object):
    if not file_name.endswith('.json'):
        file_name += '.json'
    with open(file_name, 'w') as file:
        json.dump(object, file)
        print(f'dumped file "{file_name}"')

def file_load(file_name):
    if not file_name.endswith('.json'):
        file_name += '.json'
    with open(file_name, 'r') as file:
        object = json.load(file)
        print(f'loaded file "{file_name}"')
        return object

def get_content(list_url: str):
    url = base_url + '/wordlists/' + list_url
    print(f'getting content from {url}')
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    response = requests.get(url, headers=headers)
    return response.content

def save_content(content, file_name):
    print('saving content')
    if not file_name.endswith('.save'):
        file_name += '.save'
    with open(file_name, 'wb') as file:
        file.write(content)

def read_content(file_name):
    print('reading content')
    if not file_name.endswith('.save'):
        file_name += '.save'
    response_content = None
    with open(file_name, 'rb') as file:
        response_content = file.read()
    return response_content

def get_list(response_content):
    soup = BeautifulSoup(response_content, 'html.parser')
    ul = soup.find('ul', class_='top-g')
    li_list = ul.find_all('li')
    print(f'got list size of {len(li_list)}')
    res_list = parse_list(li_list)
    return res_list

def parse_list(list):
    print('parsing list')
    res_list = []
    for li in list:
        # skip opal phrases
        if li.get('data-opal_written_phrases') is not None:
            continue
        if li.get('data-opal_spoken_phrases') is not None:
            continue

        name = li.get('data-hw')
        if name is None:
            print('name not found')
            input()

        type = None
        if li.span is not None:
            type = li.span.string
        if type is None or len(type) == 0 or type.isspace():
            # print('type not found')
            pass

        link = None
        if li.a is not None:
            link = li.a.get('href')
        if link is None or len(link) == 0 or link.isspace():
            print('link not found')

        span_lvl = li.select('span.belong-to')
        lvl = None
        if len(span_lvl) != 0:
            lvl = span_lvl[0].string

        word = {'name': name, 'type': type, 'link': link, 'lvl': lvl}
        res_list.append(word)
    return res_list


def main():
    # list_url = 'oxford3000-5000'
    # list_url = 'opal'
    list_url = 'oxford-phrase-list'
    content_file_name = 'content-' + list_url
    content = get_content(list_url)
    save_content(content, content_file_name)

    # content = read_content(content_file_name)
    res_list = get_list(content)
    file_dump(list_url, res_list)
    

if __name__ == '__main__':
    main()
