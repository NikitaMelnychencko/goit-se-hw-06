-- Знайти список курсів, які відвідує студент
SELECT s.fullname, sub.name
FROM students AS s
LEFT JOIN groups AS g ON g.id = s.group_id
LEFT JOIN subjects AS sub ON sub.group_id = g.id
WHERE s.id = 1
GROUP BY s.fullname, sub.name;
