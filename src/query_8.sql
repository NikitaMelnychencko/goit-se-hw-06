-- Знайти середній бал, який ставить певний викладач зі своїх предметів
SELECT ROUND(AVG(g.grade), 2) AS avg_grade, t.fullname
FROM grades AS g
LEFT JOIN subjects AS s ON s.id = g.subject_id
LEFT JOIN teachers AS t ON t.id = s.teacher_id
WHERE t.id = 1
GROUP BY t.fullname;
