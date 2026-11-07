-- Знайти оцінки студентів у окремій групі з певного предмета
SELECT s.fullname, gr.grade, gr.student_id, gr.date
FROM students AS s
JOIN groups AS g ON g.id = s.group_id
LEFT JOIN grades AS gr ON gr.student_id = s.id
WHERE g.id = 1 AND gr.subject_id = 1;
