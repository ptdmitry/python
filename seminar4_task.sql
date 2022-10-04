USE lesson_4;

/* Таблички: https://drive.google.com/file/d/1PQn576YVakvlWrIgIjSP9YEf5id4cqYs/view
В файле lesson4_2.sql после комментария "Собеседование" */

-- 1. Вывести на экран сколько машин каждого цвета для машин марок BMW и LADA

SELECT mark, color, COUNT(*) count_auto FROM auto
WHERE mark IN("BMW")
GROUP BY color
UNION
SELECT mark, color, COUNT(*) count_auto FROM auto
WHERE mark IN("LADA")
GROUP BY color;

/* 2. Вывести на экран марку авто (количество) авто не этой марки: 20 - BMW, AUDI - 30, LADA - 15 */
SELECT
    mark,
    COUNT(mark) AS count_mark,
    (SELECT COUNT(mark) FROM auto a1
    WHERE a1.mark != a.mark) AS other_mark
FROM auto a
GROUP BY mark;

-- 3. Даны 2 таблицы, созданные следующим образом:

CREATE TABLE test_a (
    id INT,
    `data` VARCHAR(1));
CREATE TABLE test_b (
    id INT);
    
INSERT INTO test_a (id, `data`) VALUES
(10, 'A'),
(20, 'A'),
(30, 'F'),
(40, 'D'),
(50, 'C');

INSERT test_b (id) VALUES
(10),
(30),
(50);

/* Напишите запрос, который вернет строки из таблицы test_a,
id которых нет в таблице test_b, НЕ используя ключевого слова NOT */

SELECT test_a.id, `data` FROM test_a
LEFT JOIN test_b
ON test_b.id = test_a.id
WHERE test_b.id IS NULL;