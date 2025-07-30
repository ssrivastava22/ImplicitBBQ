# ImplicitBBQ

This repository contains all the data and prompts for the **ImplicitBBQ** project, which explores implicit bias in language models using the BBQ Bias Benchmark. The project includes the ImplicitBBQ dataset and the exact prompts used for model interaction.

---

## Repository Structure

- **data/**  
  Contains the ImplicitBBQ dataset.

- **bbq_implicit_evaluation/**  
  Stores model predictions on the Implicit BBQ dataset for downstream comparative analysis with the original BBQ dataset.

- **bbq_evaluation/**  
  Stores model predictions on the original BBQ dataset for downstream comparative analysis.

- **prompts.txt**  
  The exact prompts used for dataset expansion.

---

## Contents

### 1. ImplicitBBQ Dataset

A version of the BBQ Bias Benchmark where explicit identity references (e.g., "a Black man") are rewritten to be implicit (e.g., using names, clothing, or context). See `data/` for the dataset files.

### 2. Prompts

The exact prompts used for dataset expansion and model evaluation are provided in `prompts.txt`. These ensure full transparency and reproducibility.

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anonymous/ImplicitBBQ.git
   cd ImplicitBBQ