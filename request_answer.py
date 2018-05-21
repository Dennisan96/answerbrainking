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
    #print("Search on URL: " + url);
    urlh = requests.get(url, headers=headers)
    return urlh


def get_choices(answers):
    output = dict()
    for a in answers:
        list = jieba.cut(a, cut_all=True)
        l = []
        #print("list", type(list))
        for item in list:
            #print("item: ", type(item))
            if len(item) != 1:
                l.append(item)
        output[a] = l
    #print("output", output)
    return output


def get_answer_by_choices(question, answers):

    rh = open_query_url(question)

    # choices = get_choices(answers)

    #print(choices)

    choice_counts = []

    for a in answers:
        choice_counts.append(rh.text.lower().count(a))

    #for key, value in choices.items():
    #    tmp = 0
     #   for a in value:
     #       tmp = tmp + rh.text.count(a)
     #   choice_counts.append(tmp)

    choice_counts = list(map(int, choice_counts))

    index_max = choice_counts.index(max(choice_counts))
    if choice_counts[index_max] == 0:
        # there is no corrent answer
        return index_max, 'No correct answer'

    # print('Here is choice count:', choice_counts)

    return answers[index_max]


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_answer_by_wordscount(question, search_engine=None):
    rh = open_query_url(question)
    soup = BeautifulSoup(rh.text, 'lxml')
    words_list = []

    texts = soup.find_all(class_='g')
    for t in texts:
        print(t.text)
        print("\n")

    return None


