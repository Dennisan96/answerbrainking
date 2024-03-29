from request_question import get_qnc_from_screenshot
from request_answer import get_answer_by_choices
from auto_adb import tap


search_engine_numdict = {
    1:'baidu',
    2:'google'
}


DEGUG = False


def main():

    if DEGUG:
        query, choice = get_qnc_from_screenshot(debug=True)
        answer = get_answer_by_choices(query, choice)
        print("Answer: ", answer)
        exit(1)

    while True:
        signal = input("Enter when you see the question (x for end): ")
        if signal == '':
            # enter answering mode
            query, choice = get_qnc_from_screenshot()
            answer, ans_index = get_answer_by_choices(query, choice)
            print("Answer: ", answer)
            tap(0)
            if answer is 'Error':
                print("Error")
                continue
            elif answer is '':
                print("Error")
                continue
            else:
                tap(0)
        elif signal == 'x':
            print("Program finish")
            exit(1)
        else:
            continue


if __name__ == '__main__':
    main()
