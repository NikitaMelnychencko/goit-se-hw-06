-- Середній бал, який певний викладач ставить певному студентові
SELECT ROUND(AVG(g.grade), 2) AS avg_grade, s.fullname AS studentname, t.fullname AS teachername
FROM grades AS g
LEFT JOIN subjects AS sub ON sub.id = g.subject_id
LEFT JOIN teachers AS t ON t.id = sub.teacher_id
LEFT JOIN students AS s ON s.id = g.student_id
WHERE t.id = 1 AND s.id = 1
GROUP BY t.fullname, s.fullname;
