-- Знайти список студентів у певній групі
SELECT s.fullname
FROM students AS s
JOIN groups AS g ON g.id = s.group_id
WHERE g.id = 1;
