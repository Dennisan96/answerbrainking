import request_answer

search_engine_numdict = {
    1:'baidu',
    2:'google'
}

def main():
    query = input('Enter your question: ')
    try:
        serach_eng = search_engine_numdict[int(input('Enter search eng: 1 for baidu, 2 for google： '))]
    except:
        print("invalid")
        exit()

    possible_answer_list = []
    while True:
        possible_answer = input('Enter possible answer or finish with an ENTER： ')
        if len(possible_answer) < 1: break
        possible_answer_list.append(possible_answer)

    request_answer.get_answer(serach_eng, query, possible_answer_list)

if __name__ == '__main__':
    main()