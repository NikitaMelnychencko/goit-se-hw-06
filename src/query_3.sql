-- Знайти середній бал у групах з певного предмета
SELECT
    sub.name AS subject_name,
    gr.name AS group_name,
    ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades AS g
JOIN students AS s ON s.id = g.student_id
JOIN groups AS gr ON gr.id = s.group_id
JOIN subjects AS sub ON sub.id = g.subject_id
WHERE g.subject_id = 1
GROUP BY sub.id, sub.name, gr.id, gr.name
ORDER BY avg_grade DESC;
