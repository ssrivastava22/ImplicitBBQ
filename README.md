# ImplicitBBQ

This repository contains all code, data, and prompts for the **ImplicitBBQ** project, which explores implicit bias in language models using the BBQ Bias Benchmark. The project includes the ImplicitBBQ dataset, scripts for dataset expansion, evaluation tools, and the exact prompts used for model interaction.

---

## Repository Structure

- **data/**  
  Contains the ImplicitBBQ dataset.

- **code/**  
  - `dataset_expansion.py` — Script for expanding the original BBQ dataset with implicit attribute cues.
  - `llm_evaluation.py` — Script for evaluating model outputs on the  Implicit BBQ dataset.
  - `prompts.txt` — The exact prompts used for dataset expansion.

- **bbq_implicit_evaluation/**  
  Stores model predictions on the Implicit BBQ dataset for downstream comparative analysis with the original BBQ dataset.

- **bbq_evaluation/**  
  Stores model predictions on the original BBQ dataset for downstream comparative analysis.

---

## Contents

### 1. ImplicitBBQ Dataset

A version of the BBQ Bias Benchmark where explicit identity references (e.g., "a Black man") are rewritten to be implicit (e.g., using names, clothing, or context). See `data/` for the dataset files.

### 2. Dataset Expansion Scripts

Python scripts that take the original BBQ dataset and rewrite contexts and answer choices to make identity cues implicit, following the instructions in `code/prompts.txt`.

### 3. Evaluation Scripts

Tools for running language models on the (implicit) BBQ dataset and evaluating their predictions. See `code/evaluation/`.

### 4. Prompts

The exact prompts used for dataset expansion and model evaluation are provided in `code/prompts.txt`. These ensure full transparency and reproducibility.

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ImplicitBBQ.git
   cd ImplicitBBQ