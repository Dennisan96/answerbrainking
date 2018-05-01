import request_answer
import request_question


search_engine_numdict = {
    1:'baidu',
    2:'google'
}


def main():
    query = request_question.get_question_from_prompt()

    ans = request_answer.get_answer_by_wordscount(query)

    print(query, 'is', ans)

if __name__ == '__main__':
    main()