# project_directory/stages/stage3_axial_coding.py

import pandas as pd
from project_directory.api.deepseek_client import call_deepseek_api

def stage3_axial_coding(input_file, output_file):
    """
    阶段3：主轴编码
    从 step2.xlsx 中提取子类别，进行聚类，写入 step3.xlsx
    """
    print("=== Stage 3: Axial Coding ===")
    df = pd.read_excel(input_file)
    subcategories = set(df['cause_subcategory'].tolist() + df['effect_subcategory'].tolist())
    subcategories_list = "\n".join(list(subcategories))

    system_prompt = """
You are an expert in grounded theory. 
You have a list of subcategories from the open coding of AI model open-sourcing cases. 
Please conduct axial coding, cluster these subcategories into main categories, and provide explanations in JSON format only.

# 格式示例（数组）：
# [
#   {
#     "main_category": "...",
#     "main_category_explanation": "...",
#     "subcategories_in_this_main_category": [
#       "...", 
#       "...",
#       ...
#     ]
#   }
# ]
# 只输出 JSON，不要包含多余文本。
"""
    user_prompt = f"""
Below are the subcategories generated from the open coding stage:
{subcategories_list}
Please group them into main categories and provide explanations.
"""
    result = call_deepseek_api(system_prompt, user_prompt)
    df_out = pd.DataFrame(result)
    df_out.to_excel(output_file, index=False)
    print(f"Stage 3 completed. Output saved to {output_file}\n")
