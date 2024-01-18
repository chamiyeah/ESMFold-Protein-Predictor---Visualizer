# ESMFold - Evolutionary-scale Prediction of Atomic-level Protein Structure with a Language Model

## [🧬 LIVE APP](https://esmfold.azurewebsites.net/)

## Overview

ESMFold is a Python-based application designed for predicting protein structures using the ESMFold model. This model is an end-to-end single sequence protein structure predictor built on the ESM-2 language model. The code in this repository is inspired by the works of the MetaAI ESM project.

## Prerequisites

Before using the ESMFold Protein Structure Predictor, make sure you have the following dependencies installed:

```bash
pip install streamlit stmol py3Dmol requests biotite
```
## Usage

  1. Clone the repository:
```bash
git clone https://github.com/your-username/ESMFold.git
cd ESMFold
```

  2. Install dependencies:
   ```bash
pip install -r requirements.txt
  ```

  3. Run the application:
  ```bash
streamlit run esmfold_app.py
```
  4. Open your browser and navigate to the provided URL.

## Features

  Protein Sequence Input: Enter the protein sequence of interest using the sidebar text area.

  Prediction: Click the "Predict" button to initiate the prediction of the protein structure.

  3D Visualization: The predicted protein structure is visualized in 3D using the Py3Dmol library. Rotate and zoom functionalities are available.

  Confidence Score: The per-residue confidence score (pLDDT) is displayed, indicating the confidence in the prediction.

  Download PDB File: Download the predicted protein structure in PDB format.

## Additional Information

  The ESMFold model is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. The model and this app are inspired by the Meta AI ESMfold. For more information, refer to Meta AI's blog post.

