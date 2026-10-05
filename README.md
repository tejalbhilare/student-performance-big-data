# Student Performance Big Data Analytics System

## Project Overview

This project analyzes student performance data using Big Data technologies.

The project uses Hadoop HDFS for data storage, Hadoop MapReduce for data processing, Apache Spark for data analysis, and Streamlit for creating an interactive dashboard.

## Objectives

- Store student data using Hadoop HDFS.
- Process student data using MapReduce.
- Analyze student performance using Apache Spark.
- Calculate average marks and attendance.
- Compare department-wise performance.
- Analyze pass and fail results.
- Display results using a Streamlit dashboard.

## Technologies Used

- Python
- Hadoop HDFS
- Hadoop MapReduce
- Apache Spark
- PySpark
- Pandas
- Streamlit
- Git
- GitHub

## Dataset

The project uses a student performance CSV dataset containing:

- Student ID
- Name
- Department
- Study Hours
- Attendance
- Marks
- Result

The dataset contains 20 students from three departments:

- CS
- EXTC
- IT

## MapReduce Result

Department-wise average marks:

CS: 61.86

EXTC: 70.83

IT: 71.57

## Spark Analysis Result

Overall Average Marks: 67.95

Overall Average Attendance: 77.95%

Pass Rate: 75.00%

Passed Students: 15

Failed Students: 5

## Dashboard

The project includes an interactive Streamlit dashboard that displays:

- Total students
- Average marks
- Average attendance
- Pass rate
- Department-wise average marks
- Pass/fail analysis
- Student performance data

## Project Workflow

Student CSV Dataset
        ↓
Hadoop HDFS
        ↓
Hadoop MapReduce
        ↓
Apache Spark
        ↓
Data Analysis
        ↓
Streamlit Dashboard

## How to Run

Open the project folder:

cd ~/student-performance-big-data

Activate the virtual environment:

source .venv/bin/activate

Run Spark analysis:

spark-submit src/spark_analysis.py

Run the dashboard:

streamlit run dashboard/app.py

Then open:

http://localhost:8501

## Learning Outcomes

This project helped in understanding:

- Big Data
- Hadoop HDFS
- MapReduce
- Apache Spark
- PySpark
- Data Analysis
- Data Visualization
- Streamlit
- Git and GitHub

## Certificate Connection

This project was developed based on concepts learned from the Simplilearn SkillUp course:

Introduction to Big Data Hadoop and Spark Developer

## Author

Tejal Bhilare

BSc Information Technology Student