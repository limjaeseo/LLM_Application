from chat_service import answer_question

while True:

    question = input("질문: ")
    answer = answer_question(question)

    print("답변:", answer)

    i = input("그만할거면 0, 더 물어볼거면 아무거나 누르세요")
    if i == "0":
        break