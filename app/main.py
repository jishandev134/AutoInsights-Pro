import os
import streamlit as st
import pandas as pd
from data_processing import clean_and_summarize
from report_generator import generate_report
from email_sender import send_email_with_report
from datetime import datetime

st.set_page_config(
    page_title="AutoInsights Pro",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AutoInsights Pro")
st.markdown("### Upload your raw data, get instant insights, and generate professional reports.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded successfully! ✅")

    # Process file
    cleaned_df, summary_df = clean_and_summarize(uploaded_file)

    st.subheader("🧹 Cleaned Data")
    st.dataframe(cleaned_df)

    st.subheader("📈 Data Summary")
    st.dataframe(summary_df)

    st.subheader("Data Preview")
    st.dataframe(cleaned_df.head())

    # Select columns for chart
    st.subheader("Select Columns for Bar Chart Analysis")
    selected_column = st.selectbox("Select primary column (X-axis)", cleaned_df.columns)
    compare_column = st.selectbox("Select secondary column (Y-axis for relationship chart)", cleaned_df.columns)

    if st.button("Generate Report"):
        report_data = generate_report(cleaned_df, summary_df, selected_column, compare_column)
        st.success("Report generated successfully!")

        
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data = report_data,
            file_name= f"AutoInsights Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    
    report_data = generate_report(cleaned_df, summary_df, selected_column, compare_column)
    report_path = f"AutoInsights Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    with open(report_path, "wb") as f:
        f.write(report_data.getvalue())

    email = st.text_input("Enter email to send the report:")
    if st.button("Send Report via Email"):
        if send_email_with_report(email, "Data Analysis Report", "Please find attached report.", report_path):
            st.success("Email sent successfully!")
        else:
            st.error("Failed to send email.")

    if os.path.exists(report_path):
        os.remove(report_path)
else:
    st.info("Please upload a CSV file to proceed.")


