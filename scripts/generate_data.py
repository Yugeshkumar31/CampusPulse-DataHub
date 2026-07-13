from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

NUM_STUDENTS = 5000
NUM_LIBRARY = 200000

# ------------------ STUDENTS ------------------
students = []
for i in range(NUM_STUDENTS):
    students.append({
        "student_id": i,
        "name": fake.name(),
        "department": random.choice(["CSE", "ECE", "MECH", "CIVIL"]),
        "year": random.choice([1,2,3,4])
    })

students_df = pd.DataFrame(students)
students_df.to_csv("data/raw/students.csv", index=False)

# ------------------ LIBRARY ------------------
library = []

for _ in range(NUM_LIBRARY):
    # Peak hour logic
    hour = random.choices(
        population=[8,9,10,11,14,15,16,17,18],
        weights=[5,10,15,10,10,15,20,10,5]
    )[0]

    entry_time = fake.date_time_this_year().replace(hour=hour, minute=0)
    duration = random.randint(1, 5)

    library.append({
        "student_id": random.randint(0, NUM_STUDENTS-1),
        "entry_time": entry_time,
        "exit_time": entry_time + timedelta(hours=duration)
    })

library_df = pd.DataFrame(library)
library_df.to_csv("data/raw/library.csv", index=False)

print("🔥 Large Scale Data Generated Successfully!")