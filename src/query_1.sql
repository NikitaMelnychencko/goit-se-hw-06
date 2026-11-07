-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів
SELECT ROUND(AVG(g.grade), 2) AS avggrade, s.fullname
FROM grades AS g
LEFT JOIN students AS s ON s.id = g.student_id
GROUP BY g.student_id
ORDER BY ROUND(AVG(g.grade), 2) DESC
LIMIT 5;
