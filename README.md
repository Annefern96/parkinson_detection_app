# Parkinson Detection App — Advanced README

**AI-powered Streamlit prototype** for detecting early signs of Parkinson’s disease from voice biomarkers. Built for education and prototyping. Not for clinical use.

## Project overview

A Streamlit app that ingests tabular voice biomarkers and predicts Parkinson’s disease status using an XGBoost classifier. The app includes local explainability with SHAP, experiment tracking with MLflow, anonymous session logging for traceability, and modular code for easy extension into real-time audio pipelines.


## Key features

- Upload `.csv` files containing voice biomarker features.

- Single-record and batch predictions with confidence scores (probabilities).

- Global and per-sample explainability via SHAP summary and waterfall plots.

- Experiment tracking (metrics, parameters, artifacts) using MLflow.

- Anonymous session logging (`logs/user_sessions.csv`) with UUIDs and timestamps.

- Model persistence with `joblib` and reproducible training scripts.

## Architecture & components

- `app.py` — Streamlit front-end (UI flows, file upload, predictions, plots).

- `models/` — trained model artifacts (e.g., `xgb_model.joblib`, `scaler.joblib`).

- `src/` — modular code: `data.py`, `train.py`, `predict.py`, `explain.py`, `utils.py`.

- `mlflow/` — optional local MLflow tracking server config (if used).

- `logs/` — session logs and lightweight audit trail.

- `requirements.txt` — python dependencies.

## Data schema & input format

**Required columns (order not important)**. Exclude `name` column if present.

- `MDVP:Fo(Hz)`

- `MDVP:Fhi(Hz)`

- `MDVP:Flo(Hz)`

- `Jitter(%)`

- `Shimmer(dB)`

- `HNR`

- `RPDE`

- `DFA`

- `spread1`

- `spread2`

- `D2`

- `PPE`

- `status` (optional during inference; used for evaluation — 0 = healthy, 1 = Parkinson’s)
**Sample dataset: UCI Parkinson’s Data**
  
**Validation**: the app performs schema checks on upload and reports missing/extra columns. For robust ingestion, use the `src/data.py` helper which includes type coercion and NaN handling.



## Quickstart (developer)

### 1. Clone the repo:
```
git clone https://github.com/<you>/parkinson_detection_app.git
cd parkinson_detection_app
```
or 

###  Open the Project Folder
Make sure the project folder (e.g., `parkinson_detection_app`) is saved on your computer.

- **Windows:** Right-click inside the folder → **Open in Terminal** or **Open PowerShell window here**  
- **macOS/Linux:** Open Terminal and navigate to your folder:
```bash
cd ~/Documents/parkinson_detection_app
```

### 2. Create virtual Environment
```
python -m venv venv
# windows
.\venv\Scripts\activate (for windows)
# macOS 
source venv/bin/activate(for macOS)
```

### 3. Install Dependencies

Make sure requirements.txt is in the project folder:
```
pip install -r requirements.txt
```
### 4.Run Locally
```
streamlit run app.py
```

✅ Your app should now open in your browser!

## Model training & reproducibility

- Training pipeline (`src/train.py`) supports:

- Data splitting with stratification and fixed random seed.

- Hyperparameter search (grid/random) with cross-validation.

- Model evaluation (accuracy, ROC AUC, precision/recall, F1) and saving best model as `models/xgb_model.joblib`.

- MLflow logging for params, metrics, confusion matrix, and model artifact.

**Best practices included:**

- Set `RANDOM_SEED` in `config.py` for reproducibility.

- Record package versions via `pip freeze > requirements.txt` and MLflow run tags.

- Save preprocessing objects (scaler, encoders) alongside model.
## Explainability (SHAP) & outputs

- `src/explain.py` contains SHAP wrapper utilities that support:

  - global SHAP summary plot (feature importance across dataset).

  - per-sample SHAP waterfall/force plot for individual explanations.

- Streamlit pages render SHAP using Matplotlib/Plotly; artifacts are saved to MLflow runs.

**Note on SHAP and XGBoost:** We compute SHAP values using the `TreeExplainer` for efficiency. When using different model families, add corresponding explainers.

## Evaluation & reliability

- Evaluation metrics logged with MLflow: accuracy, ROC AUC, precision, recall, F1, confusion matrix.

- Confidence Calibration: plan to add Platt scaling / isotonic regression wrappers to calibrate predicted probabilities. Calibration helper exists at `src/calibration.py` (experimental).

- Drift & monitoring recommendations:

  - Periodic evaluation on recent data

  - Monitor input feature distributions (KL divergence / population stability index)

  - Monitor model output distributions and label shift

## Limitations & ethical considerations

- **Not a diagnostic tool**: For demonstration only. Results should never replace clinical judgement.

- **Data limitations**: The UCI dataset has its own collection biases — the model’s real-world performance may differ across demographics and recording devices.

- **No demographic features**: Limits potential fairness audits; collecting such data must follow strong consent and privacy safeguards.

- **Explainability caveat**: SHAP explains model behaviour, not clinical causality.

## Roadmap & future work

- Add real-time audio ingestion (microphone) and on-device feature extraction (Parselmouth / Librosa).

- Add model calibration pipelines and automated drift detection.

- Add formal fairness and robustness audits if demographic attributes are ethically collected.

- Improve UX: batch reporting, downloadable PDF reports, clinician export formats.


