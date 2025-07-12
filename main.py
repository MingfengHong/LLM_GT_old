# project_directory/main.py

from project_directory.stages.stage1_information_extraction import stage1_information_extraction
from project_directory.stages.stage2_open_coding import stage2_open_coding
from project_directory.stages.stage3_axial_coding import stage3_axial_coding
from project_directory.stages.stage4_selective_coding import stage4_selective_coding
from project_directory.stages.stage5_saturation_test import stage5_saturation_test

def main():
    # 所有文件均位于项目同一目录下
    stage1_information_extraction("data/input_data/test.xlsx", "data/output_data/step1.xlsx")
    stage2_open_coding("data/output_data/step1.xlsx", "data/output_data/step2.xlsx")
    stage3_axial_coding("data/output_data/step2.xlsx", "data/output_data/step3.xlsx")
    stage4_selective_coding("data/output_data/step3.xlsx", "data/output_data/step4.xlsx")
    stage5_saturation_test("data/output_data/step4.xlsx", "data/output_data/step5.xlsx")

if __name__ == "__main__":
    main()
