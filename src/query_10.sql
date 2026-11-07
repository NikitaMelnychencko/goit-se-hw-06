-- Список курсів, які певному студенту читає певний викладач
SELECT s.fullname, sub.name
FROM students AS s
LEFT JOIN groups AS g ON g.id = s.group_id
LEFT JOIN subjects AS sub ON sub.group_id = g.id
LEFT JOIN teachers AS t ON t.id = sub.teacher_id
WHERE t.id = 1 AND s.id = 1
GROUP BY s.fullname, sub.name;
