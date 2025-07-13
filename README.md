# LLM-Assisted Computational Grounded Theory 

## Project Overview

This project implements a multi-stage pipeline for conducting Grounded Theory analysis with the assistance of Large Language Models (LLMs) and Natural Language Processing (NLP). It draws inspiration from Grounded Theory methodology, LLM Grounded Theory frameworks (Zhou et al., 2024) and Computational Grounded Theory frameworks (Nelson, 2020).

The process is broken down into distinct stages, allowing for human review and intervention at each step to ensure the quality and validity of the generated theoretical constructs.


> 🚀 **Citation Requirement**
>
> This code replicates the analysis done in the article (coming soon). If this toolkit accelerates your research, please help advance open science by citing our paper, “Computational Grounded Theory with Large Language Models” (Hong et al., 2025).
>
> APA 7th edition:
>
> > Hong, M., Hong, Z., Liu, P. (2025). *Strategic Imperatives in Openness: Unveiling Vendor Motivations for Open-Sourcing Large Language Models via a Systematic LLM-Assisted Grounded Theory*. *XXXXX, xx*(x), xxx–xxx. https://doi.org/10.xxxx/xxxxx.2025.xxx



------

## Directory Structure

```text
llm_computational_gt/
├── common_utils/                # Shared utility functions (config, API calls, file I/O)
│   ├── __init__.py
│   ├── config.py
│   ├── llm_api.py
│   └── file_handler.py
├── input_data/                  # Raw input files (e.g., interview transcripts, reports in .xlsx or .csv)
├── prompts/                     # System prompts for the LLM for each stage
│   ├── system_prompt_stage1.txt
│   └── ...
├── stage0_pattern_discovery/    # Initial computational pattern discovery (e.g., topic modeling)
│   ├── run_stage0.py
│   └── output/                  # Outputs from Stage 0
├── stage1_extraction/           # LLM-assisted information extraction
│   ├── run_stage1.py
│   └── output/
├── stage2_open_coding/          # LLM-assisted open coding
│   ├── run_stage2.py
│   └── output/
├── stage3_axial_coding/         # LLM-assisted axial coding
│   ├── run_stage3.py
│   └── output/
├── stage4_selective_coding/     # LLM-assisted selective coding
│   ├── run_stage4.py
│   └── output/
└── stage5_saturation_test/      # LLM-assisted data saturation testing
    ├── run_stage5.py
    └── output/
├── main_orchestrator.py         # Optional: Script to run all stages sequentially
├── requirements.txt
└── README.md                    # This file
```


------

## Stages

#### Stage-Specific Processing Loops and Logic involves:

- Reading the correct input files (often the output of the previous stage).
- Iterating through data items (e.g., files, then rows for Stage 1; excerpts for Stage 2; subcategories for Stage 3).
- Calling the LLM API with the appropriate system and user prompts.
- Processing the LLM's response.
- Accumulating results.
- Saving the results in JSON and Excel formats.
- Specific checks and print statements relevant to that stage.

This stage-specific logic is not "reusable" in the sense of being a common utility function shared across *different* stages, but rather it's the unique implementation *of* each stage.

Therefore, I believe we have now extracted the main reusable Python components. The next step would be to start populating the individual `run_stageX.py` scripts, adapting the logic from your original script for each specific stage, and ensuring they use the functions and configurations from `common_utils`.

1. **Stage 0: Pattern Discovery:**
   - **Script:** `stage0_pattern_discovery/run_stage0.py`
   - **Purpose:** Applies computational text analysis techniques (e.g., topic modeling, keyword extraction) to the raw input data to identify broad patterns and themes. This stage does not typically involve LLM calls.
   - **Output:** Topic models, keyword lists, etc., saved in `stage0_pattern_discovery/output/`.
   - **Human Review:** Review computational outputs to gain an initial understanding of the data landscape and inform prompts for subsequent LLM-driven stages.
2. **Stage 1: Information Extraction:**
   - **Script:** `stage1_extraction/run_stage1.py`
   - **Purpose:** Uses an LLM to extract relevant segments (excerpts) from the input texts based on predefined criteria (see `prompts/system_prompt_stage1.txt`).
   - **Input:** Raw data from `input_data/`.
   - **Output:** JSON and Excel files containing extracted excerpts, saved in `stage1_extraction/output/`.
   - **Human Review:** Review extracted excerpts for relevance and accuracy. Cleaned/validated data can be saved as a `_reviewed` version to be used by the next stage.
3. **Stage 2: Open Coding:**
   - **Script:** `stage2_open_coding/run_stage2.py`
   - **Purpose:** Assigns "Concepts" and "SubCategories" to each excerpt using an LLM (see `prompts/system_prompt_stage2.txt`), maintaining consistency with previously generated codes.
   - **Input:** (Reviewed) excerpts from Stage 1.
   - **Output:** JSON and Excel files with coded excerpts, saved in `stage2_open_coding/output/`.
   - **Human Review:** Review and refine LLM-generated codes and subcategories.
4. **Stage 3: Axial Coding:**
   - **Script:** `stage3_axial_coding/run_stage3.py`
   - **Purpose:** Clusters subcategories (from Stage 2) into broader "Main Categories" using an LLM (see `prompts/system_prompt_stage3.txt`).
   - **Input:** (Reviewed) unique subcategories from Stage 2.
   - **Output:** JSON and Excel files defining main categories, saved in `stage3_axial_coding/output/`.
   - **Human Review:** Review and refine main categories and their relationships.
5. **Stage 4: Selective Coding:**
   - **Script:** `stage4_selective_coding/run_stage4.py`
   - **Purpose:** Identifies a "Core Category" that integrates the main categories using an LLM (see `prompts/system_prompt_stage4.txt`).
   - **Input:** (Reviewed) main categories from Stage 3.
   - **Output:** JSON and Excel file describing the core category, saved in `stage4_selective_coding/output/`.
   - **Human Review:** Evaluate the core category and its explanatory power.
6. **Stage 5: Data Saturation Test:**
   - **Script:** `stage5_saturation_test/run_stage5.py`
   - **Purpose:** Tests whether the existing main categories can accommodate all identified subcategories, or if new main categories emerge (see `prompts/system_prompt_stage5.txt`).
   - **Input:** Main categories (from Stage 3) and unique subcategories (from Stage 2).
   - **Output:** JSON and Excel file with saturation test results, saved in `stage5_saturation_test/output/`.
   - **Human Review:** Analyze results to assess theoretical saturation.

------

## Setup

#### 1. Clone the repository (if applicable)

```bash
git clone https://github.com/SweetDumplingBall/llm_computational_gt.git
cd llm_computational_gt
```


#### 2. Create a Python environment (choose one)

##### 2-A. Lightweight **venv**

###### **macOS / Linux**

```bash
python3.12 -m venv venv
source venv/bin/activate
```

###### **Windows**

```powershell
python -m venv venv
.\venv\Scripts\activate
```


##### 2-B. Full-featured **conda** (recommended for research or complex deps)

###### **macOS / Linux**

```bash
conda create -n myenv python=3.12
conda activate myenv
```

###### **Windows**

```powershell
conda create -n myenv python=3.12
conda activate myenv
```


#### 3. Install dependencies

###### **macOS / Linux**

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # or en_core_web_md / en_core_web_lg
```

###### **Windows**

```powershell
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # or en_core_web_md / en_core_web_lg
```

> ⚠️You may need to install `spacy` and `en_core_web_sm` separately if you encounter issues.
> 
> ⚠️You may need to run `check_nltk.py` if you have not installed NLTK data before.

#### 4. Configure your API key

1. Open `common_utils/config.py`.

2. Replace the `API_KEY` placeholder with your real DeepSeek (or OpenAI) key.

3. Adjust `BASE_URL` if you use a custom endpoint.

4. **Security tip:** In production, load the key from an environment variable, e.g.

   ```bash
   export DEEPSEEK_API_KEY=sk-xxxx
   ```

#### 5. Prepare input data

- Place your `.xlsx` or `.csv` files inside the `input_data/` folder.
- Make sure the column names match `COLUMN_NAME_CASE_NUMBER` and `COLUMN_NAME_REPORT_TEXT` in `common_utils/config.py`.


#### 6. Review / customise system prompts

- Open the files in `prompts/` and tweak them to match your research context.


> ✅ With the environment activated (venv or conda), you can now run the project’s scripts and process your data.

------

## Running the Stages

It is recommended to run each stage sequentially and perform human review of the outputs before proceeding to the next stage.

Example:

```bash
python stage0_pattern_discovery/run_stage0.py
# (Perform human review of files in stage0_pattern_discovery/output/)
python stage1_extraction/run_stage1.py
# (Perform human review of files in stage1_extraction/output/)
# ... and so on for subsequent stages.
```

Alternatively, the `main_orchestrator.py` script can be used to run all stages in sequence (human review steps would need to be manually inserted or the script modified for interactive pauses).

------

## Key Files for Configuration and Utilities

- `common_utils/config.py`: Central configuration for API keys, paths, filenames, etc.
- `common_utils/llm_api.py`: Handles LLM client initialization and API calls.
- `common_utils/file_handler.py`: Provides utility functions for reading/writing JSON, Excel, and text files.

------

## Customization
> ✨ With these knobs, you can swap models, run synchronous or asynchronous pipelines, and adapt every step—from preprocessing to human validation—to fit your project.

| Area                         | What you can tweak                                           | How to do it                                                 |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Model choice**             | Swap in any LLM—OpenAI ChatGPT, DeepSeek, Qwen, Google Gemini, etc. | Open `llm_api.py` and change the client instantiation / `model=` field. Import the appropriate SDK (OpenAI, DeepSeek, Qwen, Google Generative AI) and set the correct `BASE_URL` or credentials. |
| **Async option**             | Run Stage 1 calls concurrently for higher throughput         | In **`llm_api.py`** locate the *Asynchronous OpenAI Client* block and **uncomment** it. Then execute **`run_async_stage1.py`** instead of `run_stage1.py`. Adjust concurrency limits there (e.g., `max_connections`) to suit your rate-limit budget. |
| **Prompts**                  | Direct the model’s behaviour and tone                        | Edit the system/user prompt files in `prompts/` to reflect your research questions, domain jargon, or annotation scheme. |
| **Stage 0 methods**          | Pre-LLM computational text analyses                          | Extend **`run_stage0.py`** with topic modelling, clustering, sentiment analysis, or any bespoke NLP preprocessing before handing data to the LLM. |
| **Human-in-the-loop review** | Workflow, criteria, and artefacts for manual validation      | Adapt the checklist, rubric, or spreadsheet templates inside the *Human Review* folder—or integrate your own UI—to match your team’s quality-control process and IRB requirements. |

------

## **Data Availability & Copyright Notice**

The corpus underlying Computational Grounded Theory with Large Language Models was obtained through web-scraping and still contains passages protected by copyright. To respect those rights, we release only a public domain sample dataset. Although smaller than the full corpus, this sample is sufficient to run every major step of the preprocessing, feature extraction, and modelling pipeline described in the paper.
> 📧 Researchers who need the complete, unredacted dataset for non-commercial academic purposes may email Hong Mingfeng at hongmingfeng24@mails.ucas.ac.cn to request access under a research-only agreement.

