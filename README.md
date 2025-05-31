<h1>Tell Me What I Want To Hear</h1>
<h2>Project Overview</h2>
This repo contains work that contributed towards our project proposal for the Apart Research fellowship.

The probe_experiments folder contains the results of our work, where the extreme-crises experiment proved to have the most interesting results, and is what we will be focusing on for our project.

<h2>Files and Folders</h2>

```
.
├── moral_evaluation/
│   ├── prompts/
|   |   ├── mfq1_system_prompt.md         # System prompt for Moral Foundations Questionnaire (MFQ) part 1.
|   |   ├── mfq1_questions.csv            # Questions for MFQ part 1.
|   |   ├── mfq2_system_prompt.md         # System prompt for MFQ part 2.
|   |   ├── mfq2_questions.csv            # Questions for MFQ part 2.
|   |   ├── prompts_and_questions.py      # All prompts and questions for both questionnaires.
|   |   ├── pvq_rr_system_prompt.md       # System prompt for Portrait Values Questionnaire (PVQ-RR).
|   |   └── pvq_rr_questions.csv          # Questions for PVQ-RR.
│   ├── evaluation/
│   │   ├── data/
│   │   │   ├── mfq1_results.csv          # Results for MFQ part 1.
│   │   │   ├── mfq1_results.csv          # Results for MFQ part 2.
│   │   │   └── pvq_rr_results.csv        # Results for PVQ-RR.
│   │   ├── notebooks/
│   │   │   ├── moral_analytics.ipynb     # Analytics of the results for the questionnaires.
│   │   │   └── moral_inference.ipynb     # Used to get the results from the models for the questionnaires.
│   │   ├── visualizations/
│   │   │   ├── MFQ.png                   # Visual graph of MFQ scores for the models.
│   │   │   └── PVQ_RR.png                # Visual graph of PVQ-RR scores for the models.
│   │   ├── mfq_evaluation_logic.py       # Logic for evaluating MFQ responses.
│   │   └── pvq_rr_evaluation_logic.py    # Logic for evaluating PVQ-RR responses.
│   ├── human_responses/
|   |   ├── mfq_human_responses.csv       # Human responses to MFQ for comparison.
|   |   └── pvq_rr_human_responses.csv    # Human responses to PVQ-RR for comparison.
├── probe_experiments/                    # Probe experiments for Apart Research project proposal
│   ├── counseller-exams/
|   |   ├── exp_1_analysis.ipynb          # Scoring of models on NCE and MFT exam.
|   |   ├── experiment_1_results_mft.csv  # Models' responses for MFT exam.
|   |   ├── experiment_1_results_nce.csv  # Models' responses for NCE.
|   |   └── probe_experiment_1.ipynb      # Used to get the responses from the models on the exams.
│   ├── extreme-crises/
|   |   ├── exp_5_analysis.ipynb          # Used to check models' responses against three criteria, and create graphs.
|   |   ├── experiment_5_results.csv      # Raw responses from the models.
|   |   ├── experiment_5_rubric_split.csv # Responses split into boolean columns.
|   |   └── probe_experiment_5.ipynb      # Used to get the responses from the models.
│   ├── follow-up-questions/
|   |   ├── experiment_2_results.csv      # Responses from models.
|   |   └── probe_experiment_2.ipynb      # Used to get the responses from the models.
│   ├── general-comparison/
|   |   ├── experiment_4_results.csv      # Responses from models.
|   |   └── probe_experiment_4.ipynb      # Used to get the responses from the models.
│   ├── moral-values-sycophancy/
|   |   ├── exp_3_analysis.ipynb          # Analysis on the relationship between moral biases and sycophancy.
|   |   ├── experiment_3_results.csv      # Responses from the models on their agreement with decision, and LLM-as-judge evaluation of sycophancy.
|   |   └── probe_experiment_3.ipynb      # Used to get the responses from the models.
├── README.md                             # This page ^-^
```
