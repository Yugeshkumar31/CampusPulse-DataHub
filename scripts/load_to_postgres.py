import pandas as pd
import os
from sqlalchemy import create_engine

# 🔴 CHANGE PASSWORD HERE
engine = create_engine("postgresql://postgres:1234@localhost:5432/campuspulse")

# -------- STUDENTS (MERGE FILES) --------
student_folder = "data/processed/students_clean"

student_files = [f for f in os.listdir(student_folder) if f.endswith(".csv")]

students = pd.concat([
    pd.read_csv(f"{student_folder}/{f}") for f in student_files
])

# -------- LIBRARY --------
library = pd.read_csv("data/processed/library_final.csv")

# -------- LOAD INTO DB --------
students.to_sql("dim_students", engine, if_exists="replace", index=False)

library[['student_id','duration','hour']].to_sql(
    "fact_library", engine, if_exists="replace", index=False
)

print("🔥 Data loaded successfully")