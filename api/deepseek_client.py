# project_directory/api/deepseek_client.py

import json
from openai import OpenAI

# 初始化 DeepSeek 客户端
client = OpenAI(
    api_key="sk-xxx",  # 请替换为您的 API Key
    base_url="https://api.deepseek.com",
)

def clean_response_text(text):
    """
    如果返回的文本中包含 Markdown 代码块标识（例如 ```json），则将其去除。
    """
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text

def call_deepseek_api(system_prompt, user_prompt, max_tokens=8192):
    """
    调用 DeepSeek API，并返回解析后的 JSON 结果，同时打印请求和响应内容
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    print("----- API Request -----")
    print("System Prompt:")
    print(system_prompt)
    print("User Prompt:")
    print(user_prompt)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={'type': 'json_object'},
        max_tokens=max_tokens
    )

    raw_text = response.choices[0].message.content
    print("----- Raw API Response -----")
    print(raw_text)

    cleaned_text = clean_response_text(raw_text)
    try:
        result = json.loads(cleaned_text)
    except json.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Cleaned text that failed to parse:")
        print(cleaned_text)
        raise e
    return result
