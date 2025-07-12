# project_directory/stages/stage1_information_extraction.py

import pandas as pd
from project_directory.api.deepseek_client import call_deepseek_api

def stage1_information_extraction(input_file, output_file):
    """
    阶段1：信息抽取
    读取 test.xlsx 中的案例，提取因果关系对，写入 step1.xlsx。
    注意：这里检测 API 返回结果是否为字典，若包含 "cause_effect_pairs" 键，则提取该列表。
    """
    print("=== Stage 1: Information Extraction ===")
    df = pd.read_excel(input_file)
    results = []

    for index, row in df.iterrows():
        case_number = row['Number of Cases']  # Excel 中的案例编号列
        case_text = row['Case text']  # 案例文本列

        system_prompt = """
You are an information extraction expert. 
You will receive a user prompt that contains one or multiple case reports about “AI 模型开源案例” (why and how an organization open-sourced an AI model). 
Your task is to extract all cause-effect pairs from each case’s text, and present the result in JSON format only.

# 重要：下面约定 JSON 的键名请保持一致
# JSON字段示例（数组形式，每个元素代表一个因果关系对）： 
# [
#   {
#     "number_of_cases": "...",
#     "number_of_cause_effect_pair": "...",
#     "cause_original": "...",
#     "effect_original": "...",
#     "source_text_snippet": "..."
#   }
# ]
# 要求： 
# 1. 每个因果关系对单独形成一个 JSON 对象，并输出在同一个 JSON 数组中。
# 2. "number_of_cases" 对应案例编号。
# 3. "number_of_cause_effect_pair" 从1开始为该案例中的每对因果关系编号。
# 4. "cause_original"、"effect_original" 分别填写该因果对中原因和结果的原文短语或简要描述。
# 5. "source_text_snippet" 可选，如有需要可填写原始句子或片段。
# 6. 只输出纯粹的 JSON，不包含多余文本。
"""
        user_prompt = f"""
Below are the reports of AI model open-sourcing cases. 
For each case, please extract all cause-effect pairs and output in the required JSON structure.

Case Number: {case_number}
Case Text:
{case_text}
"""
        result = call_deepseek_api(system_prompt, user_prompt)
        # 检查返回结果类型，若为字典且包含 "cause_effect_pairs"，则提取该列表
        if isinstance(result, dict) and "cause_effect_pairs" in result:
            pairs = result["cause_effect_pairs"]
        elif isinstance(result, list):
            pairs = result
        else:
            pairs = [result]
        results.extend(pairs)

    # 构造 DataFrame 时，确保列名称与预期一致
    expected_columns = ["number_of_cases", "number_of_cause_effect_pair", "cause_original", "effect_original",
                        "source_text_snippet"]
    df_out = pd.DataFrame(results)
    # 若某些列不存在，可进行补充，避免后续处理出错
    for col in expected_columns:
        if col not in df_out.columns:
            df_out[col] = None
    df_out = df_out[expected_columns]  # 调整列顺序
    df_out.to_excel(output_file, index=False)
    print(f"Stage 1 completed. Output saved to {output_file}\n")
