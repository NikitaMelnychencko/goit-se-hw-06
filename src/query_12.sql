-- Оцінки студентів у певній групі з певного предмета на останньому занятті
SELECT s.fullname, g.grade, g.date
FROM grades AS g
JOIN students AS s ON s.id = g.student_id
WHERE s.group_id = 1
  AND g.subject_id = 1
  AND g.date = (
      SELECT MAX(g2.date)
      FROM grades AS g2
      JOIN students AS s2 ON s2.id = g2.student_id
      WHERE s2.group_id = 1
        AND g2.subject_id = 1
  );
