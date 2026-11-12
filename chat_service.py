from pathlib import Path

from dotenv import load_dotenv
from google import genai


load_dotenv()
client = genai.Client() # 여기에는 우리의 api 키를 숨기면서 llm 을 쓸 수 있게 하는 부분이 숨어 있다.
# 그리고 그 호출한 값을 client 라는 변수로 만들어서 정보를 넣어놓았다.


def answer_question(question):
    document = Path("data/git_기초.txt").read_text(encoding="utf-8")
    

    prompt = f"""아래 자료를 바탕으로 질문에 답하세요. 자료에 없으면 찾을 수 없다고 말하세요.
                자료: {document}

                질문: {question}"""


    interaction = client.interactions.create(
        model = "gemini-3.5-flash-lite",
        input = prompt,
    )
    return interaction.output_text


if __name__ == "__main__":
    input_text = input("질문을 입력하세요 : ")
    print(f"질문 : {input_text}")

    output_text = answer_question(input_text)

    print(f"질문 : {input_text}")
    print(f"답변 : {output_text}")


