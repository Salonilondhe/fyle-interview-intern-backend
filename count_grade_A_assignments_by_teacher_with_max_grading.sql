SELECT teacher_id, COUNT(*) as count
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id
ORDER BY count DESC;
