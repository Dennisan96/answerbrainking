from bs4 import BeautifulSoup
import requests
import urllib.parse

serach_engine_dict = {
    'baidu': 'https://www.baidu.com/s?',
    'google': 'https://www.google.com.au/search?'
}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}


def get_answer(serach_engine, question, possible_answer_list):
    #record all possible answer
    #possible_answer_list = [possible_answer for possible_answer in args]

    if serach_engine == 'baidu':
        question_encode = {'wd': question}
    else:
        #assume 'google'
        question_encode =  {'q': question}

    url = serach_engine_dict[serach_engine] + urllib.parse.urlencode(question_encode)
    print("Search on URL: "+url);

    rh = requests.get(url, headers=headers)
    soup = BeautifulSoup(rh.text, 'html.parser')

    #print(soup.prettify())

    choice_counts = []

    for i in range(len(possible_answer_list)):
        choice_counts.append(rh.text.lower().count(possible_answer_list[i]))

    choice_counts = list(map(int, choice_counts))

    index_max = choice_counts.index(max(choice_counts))

    print('Here is choice count:', choice_counts)

    print(question, 'is ', possible_answer_list[index_max])





