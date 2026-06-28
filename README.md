# Exploratory Data Analysis (EDA) — Machine Learning YT

This repository contains an Exploratory Data Analysis (EDA) project implemented in Jupyter Notebooks. The notebooks walk through data loading, cleaning, visualization, and initial insights to inform machine learning modeling decisions.

## Project Overview

- Purpose: Perform EDA on datasets to understand features, detect issues (missing values, outliers), and generate visualizations and summary statistics that guide modeling.
- Contents: EDA notebooks, visualizations, and auxiliary resources used for analysis.

## Repository Structure

```
Machine_Learning_YT/
├── README.md
├── EDA/
│   ├── data/                          # Dataset storage
│   └── notebooks/                     # Jupyter notebooks
│       ├── Insurance_EDA.ipynb
│       └── heart_attack.ipynb
└── anaconda_projects/                 # Anaconda project files
```

> Note: This repository's files are primarily Jupyter Notebooks (100% Jupyter Notebook by language composition).

## Notebooks

The main notebooks in the repo and their purpose:

- **Insurance_EDA.ipynb** — Exploratory Data Analysis on insurance dataset, including data loading, cleaning, feature analysis, visualizations, and summary statistics.
- **heart_attack.ipynb** — Exploratory Data Analysis on heart attack prediction dataset, including distribution analysis, correlations, and feature relationships.

## How to run

1. Clone the repository:

   ```bash
   git clone https://github.com/BitanXD/Machine_Learning_YT.git
   cd Machine_Learning_YT
   ```

2. (Optional) Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .\.venv\Scripts\activate   # Windows (PowerShell)
   ```

3. Install dependencies. A typical set of packages for EDA includes:

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter jupyterlab
   ```

4. Launch Jupyter and open the notebooks:

   ```bash
   jupyter lab
   ```

   or

   ```bash
   jupyter notebook
   ```

   Navigate to `EDA/notebooks/` and open the notebooks in order.

## Data

Datasets are stored in the `EDA/data/` directory. Refer to individual notebooks for specific data sources and any preprocessing steps applied before analysis.

## Findings and Recommendations

Refer to individual notebook outputs for key findings, patterns identified, issues to address before modeling, important correlations, and recommended features for next steps.

## Reproducibility

- Random seeds are set where applicable in notebooks to ensure reproducible results.
- Key Python packages and their versions can be captured with:

   ```bash
   pip freeze > requirements.txt
   ```

## Contributing

If you want to contribute improvements to the EDA (additional visualizations, notebook cleanup, or derived features):

1. Fork the repository
2. Create a feature branch
3. Open a pull request with a clear description of changes

## License

This repository is provided as-is for educational purposes. If you want to add a specific license, please update this section (e.g., MIT, Apache-2.0).

## Contact

For questions or feedback, open an issue or contact the repository owner: https://github.com/BitanXD
