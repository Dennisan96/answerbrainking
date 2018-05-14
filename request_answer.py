from bs4 import BeautifulSoup
from bs4.element import Comment
from itertools import groupby
import requests
import urllib.parse
import jieba


serach_engine_dict = {
    'baidu': 'https://www.baidu.com/s?',
    'google': 'https://www.google.com.au/search?'
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

def open_query_url(question, search_engine=None):
    if search_engine is None or search_engine == 'google':
        url = serach_engine_dict['google']
        question_encode = {'q': question}
    else:
        url = serach_engine_dict['baidu']
        question_encode = {'wd': question}

    url = url + urllib.parse.urlencode(question_encode)
    print("Search on URL: " + url);
    urlh = requests.get(url, headers=headers)
    return urlh


def get_answer_by_choices(question, search_engine=None):

    possible_answer_list = []
    while True:
        possible_answer = input('Enter possible answer or finish with an ENTER： ')
        if len(possible_answer) < 1: break
        possible_answer_list.append(possible_answer)

    rh = open_query_url(question)

    choice_counts = []
    for i in range(len(possible_answer_list)):
        choice_counts.append(rh.text.lower().count(possible_answer_list[i]))

    choice_counts = list(map(int, choice_counts))

    index_max = choice_counts.index(max(choice_counts))
    if choice_counts[index_max] == 0:
        #there is no corrent answer
        return index_max, 'No correct answer'

    print('Here is choice count:', choice_counts)


    return possible_answer_list[index_max]


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def seg_list_handler(list):
    #do nothing at this time
    return list


def get_answer_by_wordscount(question, search_engine=None):
    rh = open_query_url(question)
    soup = BeautifulSoup(rh.text, 'lxml')
    words_list = []

    text = soup.find_all(class_='g')
    for t in text:
        temp_seg_list = jieba.cut(t)
        temp_seg_list = seg_list_handler(temp_seg_list)
        words_list.extend(temp_seg_list)
    words_counts_list = [len(list(group)) for key, group in groupby(words_list)]


