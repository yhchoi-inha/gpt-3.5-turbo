import openai

# API 키 설정
api_key = 'temp'

# OpenAI API 클라이언트 초기화
openai.api_key = api_key

# AI 모델 초기화
model_1 = "gpt-3.5-turbo"
model_2 = "gpt-3.5-turbo"

# 대화 시작
conversation = [
    {"role": "system", "content": "AI_1_SPEAKS"},
    {"role": "assistant", "content": "안녕, 나는 승호1이야."},
    {"role": "system", "content": "AI_2_SPEAKS"},
    {"role": "assistant", "content": "안녕, 나는 동현2야."}
]

while True:
    # AI 모델 1이 말함
    response_1 = openai.ChatCompletion.create(
        model=model_1,
        messages=conversation
    )
    
    # 모델 1의 답변 출력
    print("나는승호111: " + response_1['choices'][0]['message']['content'])

    # 대화 업데이트
    conversation.append({"role": "system", "content": "AI_1_SPEAKS"})
    conversation.append({"role": "assistant", "content": response_1['choices'][0]['message']['content']})

    # AI 모델 2이 말함
    response_2 = openai.ChatCompletion.create(
        model=model_2,
        messages=conversation
    )

    # 모델 2의 답변 출력
    print("나는동현22: " + response_2['choices'][0]['message']['content'])

    # 대화 업데이트
    conversation.append({"role": "system", "content": "AI_2_SPEAKS"})
    conversation.append({"role": "assistant", "content": response_2['choices'][0]['message']['content']})
