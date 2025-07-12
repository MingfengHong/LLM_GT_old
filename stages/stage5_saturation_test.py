# project_directory/stages/stage5_saturation_test.py

import pandas as pd
from project_directory.api.deepseek_client import call_deepseek_api

def stage5_saturation_test(input_file, output_file):
    """
    阶段5：数据饱和度检验
    从 step2.xlsx 和 step3.xlsx 中获取子类别与主范畴，对所有子类别进行验证，写入 step5.xlsx
    """
    print("=== Stage 5: Data Saturation Test ===")
    df = pd.read_excel("step2.xlsx")
    subcategories = set(df['cause_subcategory'].tolist() + df['effect_subcategory'].tolist())
    subcategories_list = "\n".join(list(subcategories))

    df_main = pd.read_excel("step3.xlsx")
    main_categories = df_main['main_category'].tolist()
    main_categories_list = "\n".join(main_categories)

    system_prompt = """
You are an expert in grounded theory. 
We have a set of main categories from previous steps. 
Now, we also have subcategories that need to be tested for data saturation. 
For each subcategory, determine if it can be labeled under any existing main category. 
If no appropriate label, output "No appropriate label" and propose a new main category.
# 格式示例（数组）：
# [
#   {
#     "subcategory": "...",
#     "label": "某个已存在的主范畴 或 'No appropriate label'",
#     "new_main_category_proposal": "若使用 No appropriate label 时，给出一个新的主范畴，否则为空"
#   }
# ]
# 只输出 JSON，不要包含多余文本。
"""
    user_prompt = f"""
Existing main categories:
{main_categories_list}

Subcategories to be tested:
{subcategories_list}

Please perform the data saturation test.
"""
    result = call_deepseek_api(system_prompt, user_prompt)
    df_out = pd.DataFrame(result)
    df_out.to_excel(output_file, index=False)
    print(f"Stage 5 completed. Output saved to {output_file}\n")
