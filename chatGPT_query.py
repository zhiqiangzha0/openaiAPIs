import openai

openai.api_key="your openai API Key"

def Ans_ChatGPT(q):
    req = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user",
             "content":q},
        ]
    )

    res = req.choices[0].message.content
    return res

# 質問を記載
q="地球はなぜまるいでしょうか？"

# ChatGPT　API を呼び出して回答が戻ってくる
answer =Ans_ChatGPT(q)

# 回答内容を出力
print(answer)