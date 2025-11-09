# Solar Data Discovery and Analysis for West Africa

**A Week 0 Project for the KIFIYA - Kaim 10 Academy Generative AI Engineering Program.**

## Project Overview

The objective of this project is to analyze solar irradiance and weather data for three potential locations in West Africa—Malanville (Benin), Bumbuna (Sierra Leone), and Dapaong (Togo)—to provide a strategic recommendation for the optimal placement of a new solar energy farm. The analysis follows a structured data science workflow, from initial setup and data cleaning to in-depth exploratory data analysis and statistical comparison.

---

## Analysis & Key Features

*   **Professional Environment Setup:** The project is configured with a reproducible Python virtual environment, with all dependencies locked in `requirements.txt`.
*   **Version Control:** A feature-branch Git workflow was used, with all major tasks (setup, EDA per country, comparison) isolated on their own branches and merged via Pull Requests.
*   **Automated CI/CD:** A GitHub Actions workflow is in place to automatically validate the environment by installing dependencies on every push and pull request.
*   **Data Cleaning & Profiling:** Each country's dataset (~525,000+ rows) was systematically profiled. Key cleaning steps included:
    *   Handling of physically impossible negative solar irradiance values.
    *   Removal of empty or useless columns.
    *   Statistical flagging of outliers using Z-scores.
*   **Exploratory Data Analysis (EDA):** Individual notebooks were created for each country to explore:
    *   Time series patterns of solar irradiance (GHI).
    *   Distributions of key weather variables like ambient temperature and wind speed.
    *   Correlation analysis between variables using heatmaps.
*   **Comparative Analysis:** A final notebook synthesizes the findings by:
    *   Visually comparing GHI, DNI, and DHI using box plots.
    *   Quantitatively comparing key metrics with a summary statistics table.
    *   Validating the findings with a one-way ANOVA statistical test.

---

## Repository Structure

```
solar-data-discovery/
│
├── .github/
│   └── workflows/
│       └── ci.yml          # Automated CI workflow for GitHub Actions
│
├── data/                   # (Ignored by Git) Local storage for raw and clean .csv files
│
├── notebooks/
│   ├── benin-EDA.ipynb
│   ├── sierraleone-EDA.ipynb
│   ├── togo-EDA.ipynb
│   └── comparative-analysis.ipynb
│
├── .gitignore              # Specifies files and folders for Git to ignore
├── README.md               # This file
└── requirements.txt        # List of Python dependencies for reproducibility
```

---

## Getting Started: How to Reproduce this Analysis

### Prerequisites
*   Git
*   Python 3.11+

### Instructions
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nazjobs/solar-data-discovery.git
    cd solar-data-discovery
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    # Create the environment
    python -m venv VENV

    # Activate it (for bash/zsh)
    source VENV/bin/activate

    # Or activate it (for fish shell)
    source VENV/bin/activate.fish
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Add the Data:**
    *   This repository does not include the raw data.
    *   Place the `benin-malanville.csv`, `sierraleone-bumbuna.csv`, and `togo-dapaong_qc.csv` files into the `data/` directory.

5.  **Launch Jupyter Lab:**
    ```bash
    jupyter lab
    ```
    You can now navigate to the `notebooks/` directory and run the analysis notebooks. The `comparative-analysis.ipynb` notebook contains the final results.

---

## Key Findings & Recommendation

After a comprehensive analysis, the following conclusions were drawn:

*   **Highest Average Potential:** Based on the summary table, **Sierra Leone** exhibits the highest mean GHI (204.4 W/m²), suggesting it has the greatest overall solar energy potential.
*   **Greatest Variability:** The box plot for **Benin** shows the widest range for GHI, and the Z-score analysis for Sierra Leone flagged the most outliers, indicating more variable solar conditions in these locations.
*   **Most Consistent Producer:** **Togo** displays the most compact box plots and the lowest standard deviation in GHI, suggesting it offers the most stable and predictable solar energy generation profile.

**Recommendation:** For an initial investment focused on maximizing raw energy output, **Sierra Leone** is the prime candidate. However, for a project where grid stability and predictability are the primary concerns, **Togo** would be a more prudent choice.