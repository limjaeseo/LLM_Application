from dotenv import load_dotenv
from google import genai


load_dotenv()
client = genai.Client() # 여기에는 우리의 api 키를 숨기면서 llm 을 쓸 수 있게 하는 부분이 숨어 있다.
# 그리고 그 호출한 값을 client 라는 변수로 만들어서 정보를 넣어놓았다.



interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="Git commit을 한 문장으로 설명해 줘",
)
# interaction은 우리의 질문을 보내주는 것이다.



print(interaction.output_text)