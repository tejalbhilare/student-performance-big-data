from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Create Spark session
spark = SparkSession.builder \
    .appName("Student Performance Analysis") \
    .master("local[*]") \
    .getOrCreate()

# Read student dataset from HDFS
df = spark.read.csv(
    "hdfs://localhost:9000/student-performance/data/student_performance.csv",
    header=True,
    inferSchema=True
)

# Display dataset
print("===== STUDENT DATA =====")
df.show()

# Display dataset structure
print("===== DATASET SCHEMA =====")
df.printSchema()

# Calculate overall average marks
overall_marks = df.select(
    avg("Marks").alias("Average_Marks")
).collect()[0]["Average_Marks"]

print("===== OVERALL AVERAGE MARKS =====")
print(f"Average Marks: {overall_marks:.2f}")

# Calculate overall average attendance
overall_attendance = df.select(
    avg("Attendance").alias("Average_Attendance")
).collect()[0]["Average_Attendance"]

print("===== OVERALL AVERAGE ATTENDANCE =====")
print(f"Average Attendance: {overall_attendance:.2f}")

# Calculate average marks by department
department_avg = df.groupBy("Department") \
    .agg(avg("Marks").alias("Average_Marks")) \
    .orderBy("Department")

print("===== AVERAGE MARKS BY DEPARTMENT =====")
department_avg.show()

# Save results to local output file
output_file = "output/spark_analysis_results.txt"

with open(output_file, "w") as file:
    file.write("STUDENT PERFORMANCE BIG DATA ANALYSIS\n")
    file.write("=====================================\n\n")

    file.write(f"Overall Average Marks: {overall_marks:.2f}\n")
    file.write(f"Overall Average Attendance: {overall_attendance:.2f}\n\n")

    file.write("Average Marks by Department:\n")
    file.write("----------------------------\n")

    for row in department_avg.collect():
        file.write(
            f"{row['Department']}: {row['Average_Marks']:.2f}\n"
        )

print(f"\nSpark results saved to: {output_file}")

# Stop Spark
spark.stop()
