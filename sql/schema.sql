CREATE TABLE dim_students (
    student_id INT PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INT
);

CREATE TABLE fact_library (
    id SERIAL PRIMARY KEY,
    student_id INT,
    duration FLOAT,
    hour INT
);