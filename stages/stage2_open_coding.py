# project_directory/stages/stage2_open_coding.py

import pandas as pd
from project_directory.api.deepseek_client import call_deepseek_api

def stage2_open_coding(input_file, output_file):
    """
    阶段2：开放编码
    从 step1.xlsx 中读取因果对，对 cause 和 effect 进行开放编码，写入 step2.xlsx
    """
    print("=== Stage 2: Open Coding ===")
    df = pd.read_excel(input_file)
    results = []

    for index, row in df.iterrows():
        system_prompt = """
You are an expert in grounded theory. 
You have a table that contains cause-effect pairs extracted from AI model open-sourcing cases. 
Now, you need to conduct open coding for each cause and effect. Please output the coding result in pure JSON format only.

# 现有字段：
#   number_of_cases
#   number_of_cause_effect_pair
#   cause_original
#   effect_original
#
# 需要新增以下字段：
#   cause_concept
#   effect_concept
#   cause_subcategory
#   effect_subcategory
#
# 格式示例（数组）：
# [
#   {
#     "number_of_cases": "...",
#     "number_of_cause_effect_pair": "...",
#     "cause_original": "...",
#     "effect_original": "...",
#     "cause_concept": "...",
#     "effect_concept": "...",
#     "cause_subcategory": "...",
#     "effect_subcategory": "..."
#   }
# ]
# 请仅输出 JSON，不要包含多余文本。
"""
        user_prompt = f"""
Below is a cause-effect pair extracted from an AI model open-sourcing case.
number_of_cases: {row['number_of_cases']}
number_of_cause_effect_pair: {row['number_of_cause_effect_pair']}
cause_original: {row['cause_original']}
effect_original: {row['effect_original']}
Please conduct open coding for the above cause and effect.
"""
        result = call_deepseek_api(system_prompt, user_prompt)
        if isinstance(result, list):
            results.extend(result)
        else:
            results.append(result)

    df_out = pd.DataFrame(results)
    df_out.to_excel(output_file, index=False)
    print(f"Stage 2 completed. Output saved to {output_file}\n")
