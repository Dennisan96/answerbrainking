import request_answer
import request_question


search_engine_numdict = {
    1:'baidu',
    2:'google'
}


def main():
    query = request_question.get_question_from_prompt()

    possible_answer_list = []
    while True:
        possible_answer = input('Enter possible answer or finish with an ENTER： ')
        if len(possible_answer) < 1: break
        possible_answer_list.append(possible_answer)

    ans_index, ans = request_answer.get_answer(query, possible_answer_list)
    print(query, 'is', ans)

if __name__ == '__main__':
    main()