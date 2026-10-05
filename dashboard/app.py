import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Load student dataset
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "student_performance.csv"

df = pd.read_csv(DATA_FILE)

# --------------------------------------------------
# Calculate statistics
# --------------------------------------------------

total_students = len(df)
average_marks = df["Marks"].mean()
average_attendance = df["Attendance"].mean()

pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

department_avg = (
    df.groupby("Department")["Marks"]
    .mean()
    .round(2)
)

# --------------------------------------------------
# Dashboard title
# --------------------------------------------------

st.title("🎓 Student Performance Big Data Analytics")
st.write(
    "Interactive dashboard for analyzing student performance "
    "using Hadoop, MapReduce, and Apache Spark."
)

st.divider()

# --------------------------------------------------
# Key performance indicators
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Students", total_students)

with col2:
    st.metric("Average Marks", f"{average_marks:.2f}")

with col3:
    st.metric("Average Attendance", f"{average_attendance:.2f}%")

with col4:
    st.metric("Pass Rate", f"{(pass_count / total_students) * 100:.2f}%")

# --------------------------------------------------
# Department performance
# --------------------------------------------------

st.subheader("📊 Average Marks by Department")

st.bar_chart(department_avg)

# --------------------------------------------------
# Pass / Fail analysis
# --------------------------------------------------

st.subheader("📈 Student Result Analysis")

result_counts = df["Result"].value_counts()

st.bar_chart(result_counts)

# --------------------------------------------------
# Student data
# --------------------------------------------------

st.subheader("👨‍🎓 Student Performance Data")

display_df = df.copy()
display_df["Attendance"] = display_df["Attendance"].astype(str) + "%"
display_df["Marks"] = display_df["Marks"].astype(str)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)
# --------------------------------------------------
# Dataset information
# --------------------------------------------------

st.subheader("📋 Dataset Summary")

col1, col2 = st.columns(2)

with col1:
    st.write("**Departments:**")
    st.write(", ".join(sorted(df["Department"].unique())))

with col2:
    st.write("**Performance:**")
    st.write(f"Passed: {pass_count}")
    st.write(f"Failed: {fail_count}")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Student Performance Big Data Analytics System | "
    "Python • Hadoop HDFS • MapReduce • Apache Spark • Streamlit"
)