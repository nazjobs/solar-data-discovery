import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration
st.set_page_config(page_title="Solar Data Analysis", layout="wide")

st.title("☀️ Solar Data Discovery for West Africa")
st.markdown(
    "A comparative analysis of solar potential in Benin, Sierra Leone, and Togo."
)

# --- Sidebar for File Upload ---
st.sidebar.header("Upload Your Cleaned Data")

# The uploader requires the clean CSV files you generated in Task 2
uploaded_benin = st.sidebar.file_uploader("Upload benin-clean.csv", type="csv")
uploaded_sierra = st.sidebar.file_uploader("Upload sierraleone-clean.csv", type="csv")
uploaded_togo = st.sidebar.file_uploader("Upload togo-clean.csv", type="csv")

# --- Main App Body ---
if uploaded_benin and uploaded_sierra and uploaded_togo:
    # Load the data into dataframes
    df_benin = pd.read_csv(uploaded_benin)
    df_sierra = pd.read_csv(uploaded_sierra)
    df_togo = pd.read_csv(uploaded_togo)

    # Add the 'Country' column
    df_benin["Country"] = "Benin"
    df_sierra["Country"] = "Sierra Leone"
    df_togo["Country"] = "Togo"

    # Combine into a single dataframe
    df_combined = pd.concat([df_benin, df_sierra, df_togo], ignore_index=True)

    st.header("Comparative Analysis of Solar Irradiance")
    st.info(
        "The charts below compare the GHI, DNI, and DHI across the three locations."
    )

    # --- Display the Box Plot Chart ---
    metrics = ["GHI", "DNI", "DHI"]
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, metric in enumerate(metrics):
        sns.boxplot(data=df_combined, x="Country", y=metric, ax=axes[i])
        axes[i].set_title(f"Comparison of {metric}")

    plt.tight_layout()
    st.pyplot(fig)  # Use st.pyplot() to display matplotlib figures

    # --- Display the Summary Table ---
    st.header("Quantitative Summary")
    summary_table = df_combined.groupby("Country")[metrics].agg(
        ["mean", "median", "std"]
    )
    st.dataframe(summary_table)  # Use st.dataframe() to display pandas DataFrames

else:
    st.warning(
        "Please upload all three cleaned CSV files using the sidebar to begin the analysis."
    )
