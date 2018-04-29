from bs4 import BeautifulSoup
import requests
import urllib.parse

serach_engine_dict = {
    'baidu': 'https://www.baidu.com/s?',
    'google': 'https://www.google.com.au/search?'
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}


def get_answer(question, possible_answer_list, search_engine=None):

    if search_engine is None or search_engine == 'google':
        url = serach_engine_dict['google']
        question_encode = {'q': question}
    else:
        url = serach_engine_dict['baidu']
        question_encode = {'wd': question}

    url = url + urllib.parse.urlencode(question_encode)
    print("Search on URL: "+url);

    rh = requests.get(url, headers=headers)
    soup = BeautifulSoup(rh.text, 'html.parser')

    #print(soup.prettify())

    choice_counts = []

    for i in range(len(possible_answer_list)):
        choice_counts.append(rh.text.lower().count(possible_answer_list[i]))

    choice_counts = list(map(int, choice_counts))

    index_max = choice_counts.index(max(choice_counts))
    if choice_counts[index_max] == 0:
        #there is no corrent answer
        return index_max, 'No correct answer'

    print('Here is choice count:', choice_counts)


    return index_max, possible_answer_list[index_max]





