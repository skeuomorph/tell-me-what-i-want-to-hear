<h1>Tell Me What I Want To Hear</h1>
<h2>Project Overview</h2>
This project aims to identify relationships between an LLM's moral standpoint, and its tendency towards sycophancy across the 10 most common topics people seek therapy / advice for.

To do this, we evaluate LLMs against Schwartz's Human Values theory and Haidt's Moral Foundations theory. Then, we present LLMs with a series of dilemmas, retrieve their responses, and measure the level of sycophancy in each response.

<h2>Files and Folders</h2>

```
.
├── moral_evaluation/
│   ├── prompts/
|   |   ├── mfq1_system_prompt.md         # System prompt for Moral Foundations Questionnaire (MFQ) part 1.
|   |   ├── mfq1_questions.csv            # Questions for MFQ part 1.
|   |   ├── mfq2_system_prompt.md         # System prompt for MFQ part 2.
|   |   ├── mfq2_questions.csv            # Questions for MFQ part 2.
|   |   ├── pvq_rr_system_prompt.md       # System prompt for Portrait Values Questionnaire (PVQ-RR).
|   |   └── pvq_rr_questions.csv          # Questions for PVQ-RR.
│   ├── evaluation/
│   │   ├── mfq_evaluation_logic.py       # Logic for evaluating MFQ responses.
│   │   └── pvq_rr_evaluation_logic.py    # Logic for evaluating PVQ-RR responses.
│   ├── human_responses/
|   |   ├── mfq_human_responses.csv       # Human responses to MFQ for comparison.
|   |   └── pvq_rr_human_responses.csv    # Human responses to PVQ-RR for comparison.
├── dilemmas/                             # Contains dilemmas and evaluation logic used to test sycophancy in LLMs.
├── moral_sycophancy_evaluation/          # Analysis to evaluate how morals relate to sycophancy.
├── README.md                             # This page ^-^
```