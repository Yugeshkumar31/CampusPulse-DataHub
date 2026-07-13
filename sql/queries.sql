-- ============================================
-- Average Library Duration
-- ============================================

SELECT AVG(duration) AS avg_hours
FROM fact_library;


-- ============================================
-- Department-wise Usage
-- ============================================

SELECT
    d.department,
    COUNT(*) AS total_usage
FROM fact_library f
JOIN dim_students d
ON f.student_id = d.student_id
GROUP BY d.department
ORDER BY total_usage DESC;


-- ============================================
-- Peak Usage Hours
-- ============================================

SELECT
    hour,
    COUNT(*) AS usage_count
FROM fact_library
GROUP BY hour
ORDER BY usage_count DESC;


-- ============================================
-- Underutilized Hours
-- ============================================

SELECT
    hour,
    COUNT(*) AS usage_count
FROM fact_library
GROUP BY hour
ORDER BY usage_count ASC;