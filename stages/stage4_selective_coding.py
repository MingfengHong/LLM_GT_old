# project_directory/stages/stage4_selective_coding.py

import pandas as pd
from project_directory.api.deepseek_client import call_deepseek_api

def stage4_selective_coding(input_file, output_file):
    """
    阶段4：选择性编码
    读取 step3.xlsx 中的主范畴，确定核心范畴，写入 step4.xlsx
    """
    print("=== Stage 4: Selective Coding ===")
    df = pd.read_excel(input_file)
    main_categories_json = df.to_json(orient="records", force_ascii=False, indent=2)

    system_prompt = """
You are an expert in grounded theory. 
Based on the main categories identified in the previous axial coding stage, please perform selective coding. 
Find out the core category (or categories) and explain its relationship with the main categories.
# 格式示例：
# {
#   "core_category": "......",
#   "core_category_explanation": "......",
#   "relationship_with_main_categories": "......"
# }
# 只输出 JSON，不要包含多余文本。
"""
    user_prompt = f"""
Below are the main categories derived from the axial coding stage:
{main_categories_json}
Please identify the core category and explain its relationship with these main categories.
"""
    result = call_deepseek_api(system_prompt, user_prompt)
    df_out = pd.DataFrame([result])
    df_out.to_excel(output_file, index=False)
    print(f"Stage 4 completed. Output saved to {output_file}\n")
