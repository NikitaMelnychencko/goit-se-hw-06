-- Знайти які курси читає певний викладач
SELECT s.name, t.fullname
FROM subjects AS s
JOIN teachers AS t ON t.id = s.teacher_id
WHERE t.id = 1
GROUP BY s.name, t.fullname;
