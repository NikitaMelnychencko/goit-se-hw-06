-- Знайти студента із найвищим середнім балом з певного предмета
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades AS g
LEFT JOIN students AS s ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY g.student_id, s.fullname
ORDER BY avg_grade DESC
LIMIT 1;
