SELECT student_id, COUNT(*) as count
FROM assignments
WHERE grade IS NOT NULL
GROUP BY student_id;
