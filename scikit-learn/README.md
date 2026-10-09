# scikit-learn learning course

A tidy, lesson-based collection of scikit-learn notebooks, datasets, and the
Battery Health Predictor application.

## Course map

| Area | What you will find |
| --- | --- |
| `notebooks/01-foundations` | Introduction, train/test splits, and a regression workflow |
| `notebooks/02-preprocessing` | Pipelines, column transformers, and imputation |
| `notebooks/03-model-selection` | Cross-validation and hyperparameter searches |
| `notebooks/04-supervised-learning` | Classification, trees, random forests, Naive Bayes, and KNN |
| `notebooks/05-ensemble-methods` | Gradient Boosting and XGBoost lessons |
| `notebooks/06-unsupervised-learning` | K-Means, hierarchical clustering, dendrograms, and DBSCAN |
| `notebooks/07-dimensionality-reduction` | PCA with Iris data and a NumPy walkthrough |
| `notebooks/projects` | Customer segmentation project |
| `applications` | Battery Health Predictor notebook and desktop GUI |

## Directory guide

```text
scikit-learn/
├── applications/  # runnable app and application notebook
├── assets/        # images used by course material
├── data/          # CSV datasets
└── notebooks/     # ordered lesson notebooks by topic
```

## Start here

1. Open `notebooks/01-foundations/01_introduction_to_scikit_learn.ipynb`.
2. Continue through the numbered notebooks in each topic.
3. For a concise PCA lesson, open
   `notebooks/07-dimensionality-reduction/36_pca_iris.ipynb`.

## Run the Battery Health Predictor

From this directory, install the dependencies and run the GUI:

```powershell
python -m pip install pandas numpy scikit-learn matplotlib
python applications/battery_health_gui.py
```

The app resolves its dataset from `data/battery.csv`, so it can be launched
from any working directory.
