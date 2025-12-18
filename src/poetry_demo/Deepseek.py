# Please install OpenAI SDK first: `pip3 install openai`
from openai import OpenAI

client = OpenAI(api_key="sk-", base_url="https://api.deepseek.com")

response = client.chat.completions.create(model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Ты - ассистент разработчика на Python. Отвечай коротко и по делу."},
        {"role": "user", "content": """Проанализируй следующий код и объясни, что он делает:
def fibonacci():
    logging.info("Генератор Фибоначчи запущен")
    a, b = 0, 1
    count = 0
    while True:
        logging.debug(f"Сгенерировано число Фибоначчи #{count}: {a}")
        yield a
        a, b = b, a + b
        count += 1
    
    """},
    ],
    stream=False
)

print(response.choices[0].message.content)