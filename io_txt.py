#print("hello")

from pathlib import Path


# GEMINI_API_KEY = "sfsdfsfsdfsdfsdfsdfsdfsd"
# 이거 하드코딩이다. 이러면 이 소스코드를 받으면 남들이 다 알아버리지 않나.
# 이 코드에서 큰따옴표만 빼고 그대로 .env 파일에 집어넣는다. 소프트코딩 형태로 해 주고 .env 파일을 깃허브에 안올리면 된다. 



def read_document():
    return Path("./data/git_기초.txt").read_text(encoding="utf-8")

def save_preview(preview):
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    (output_dir/"output.txt").write_text(preview, encoding="utf-8")


text = read_document() 
preview = text[:100]
print(preview)
save_preview(preview)



