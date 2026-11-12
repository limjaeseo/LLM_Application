from dotenv import load_dotenv
from google import genai


load_dotenv()
client = genai.Client() # 여기에는 우리의 api 키를 숨기면서 llm 을 쓸 수 있게 하는 부분이 숨어 있다.
# 그리고 그 호출한 값을 client 라는 변수로 만들어서 정보를 넣어놓았다.


while True:

    input_text = input("질문을 입력하세요 : ")

    # print(f"질문 : {input_text}")

    interaction = client.interactions.create(
        model = "gemini-3.5-flash-lite",
        input = input_text,
    )
    # interaction은 우리의 질문을 보내주는 것이다.

    output_text = interaction.output_text

    print(f"질문 : {input_text}")
    print(f"답변 : {output_text}")

    i = input("다른 질문 없으면 0, 있으면 다른 거 누르세요")
    if i == "0":
        break
    
print("종료합니다.")