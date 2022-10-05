USE lesson_5;

/*
+----+------------+--------+
| Id | Name       | Cost   |
+----+------------+--------+
| 1  | Audi       | 52642  |
| 2  | Mercedes   | 57127  |
| 3  | Skoda      | 9000   |
| 4  | Volvo      | 29000  |
| 5  | Bentley    | 350000 |
| 6  | Citroen    | 21000  |
| 7  | Hummer     | 41400  |
| 8  | Volkswagen | 21600  |
+----+------------+--------+ */

/* 1. Создайте представление, в которое попадут автомобили стоимостью до 25 000 долларов */

DROP TABLE IF EXISTS auto;
CREATE TABLE auto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(45),
    Cost INT);
    
INSERT INTO auto (`Name`, Cost) VALUES
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000),
    ('Citroen', 21000),
    ('Hummer', 41400),
    ('Volkswagen', 21600);

DROP VIEW IF EXISTS auto_view;
CREATE VIEW auto_view AS
    SELECT * FROM auto
    WHERE Cost < 25000;
    
SELECT * FROM auto_view;

/* 2. Изменить в существующем представлении порог для стоимости:
пусть цена будет до 30 000 долларов (используя оператор ALTER VIEW) */

ALTER VIEW auto_view AS
    SELECT * FROM auto
    WHERE Cost < 30000;
    
SELECT * FROM auto_view;

/* 3. Создайте представление, в котором будут только автомобили марки “Шкода” и “Ауди” */

DROP VIEW IF EXISTS new_auto_view;
CREATE VIEW new_auto_view AS
    SELECT * FROM auto
    WHERE `Name` IN('Skoda', 'Audi');
    
SELECT * FROM new_auto_view;

/* Есть таблица анализов Analysis:
an_id — ID анализа;
an_name — название анализа;
an_cost — себестоимость анализа;
an_price — розничная цена анализа;
an_group — группа анализов.
Есть таблица групп анализов Groups:
gr_id — ID группы;
gr_name — название группы;
gr_temp — температурный режим хранения.
Есть таблица заказов Orders:
ord_id — ID заказа;
ord_datetime — дата и время заказа;
ord_an — ID анализа */

-- Создание и наполнение таблиц:
DROP TABLE IF EXISTS Analysis;
CREATE TABLE Analysis (
    an_id INT PRIMARY KEY AUTO_INCREMENT,
    an_name VARCHAR(45),
    an_cost INT,
    an_price INT,
    an_group INT);
    
DROP TABLE IF EXISTS `Groups`;
CREATE TABLE `Groups` (
    gr_id INT PRIMARY KEY,
    gr_name VARCHAR(45),
    gr_temp VARCHAR(12));
    
DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    ord_id INT PRIMARY KEY AUTO_INCREMENT,
    ord_datetime DATETIME,
    ord_an INT);
    
INSERT INTO Analysis (an_name, an_cost, an_price, an_group) VALUES
    ('Общий анализ крови', 275, 300, 1),
    ('Клинический анализ крови', 455, 485, 1),
    ('Клинический анализ мочи', 285, 310, 2),
    ('Биохимический анализ мочи', 430, 450, 2),
    ('Клинический анализ кала', 500, 550, 3),
    ('Биохимический анализ кала', 1030, 1150, 3),
    ('Барий', 350, 370, 4),
    ('Железо', 350, 370, 4),
    ('Йод', 350, 370, 4),
    ('Кальций', 350, 370, 4),
    ('Калий', 350, 370, 4);
    
INSERT INTO `Groups` (gr_id, gr_name, gr_temp) VALUES
    (1, 'Гематологические исследования', '+2 Цельсия'),
    (2, 'Исследования мочи', '+5 Цельсия'),
    (3, 'Исследования кала', '+5 Цельсия'),
    (4, 'Микроэлементы', '+5 Цельсия');
    
INSERT INTO Orders (ord_datetime, ord_an) VALUES
    ('2020/02/05 10:23:21', 1),
    ('2020/02/05 11:40:44', 4),
    ('2020/02/05 13:11:05', 1),
    ('2020/02/06 08:25:32', 2),
    ('2020/02/06 16:15:15', 3),
    ('2020/02/07 12:45:03', 11),
    ('2020/02/07 14:22:11', 10),
    ('2020/02/08 09:32:12', 1),
    ('2020/02/08 09:40:48', 2),
    ('2020/02/08 14:48:12', 6),
    ('2020/02/09 11:00:14', 7),
    ('2020/02/09 13:25:44', 8),
    ('2020/02/09 15:32:15', 9),
    ('2020/02/10 10:40:51', 5),
    ('2020/02/11 08:31:16', 8),
    ('2020/02/11 09:54:18', 4),
    ('2020/02/11 11:16:14', 2),
    ('2020/02/11 11:25:11', 1);
    
/* 4. Вывести название и цену для всех анализов, которые продавались 5 февраля 2020
и всю следующую неделю */

SELECT o.ord_datetime, a.an_name, a.an_price FROM Analysis a
JOIN Orders o
WHERE o.ord_an = a.an_id
ORDER BY o.ord_datetime;

/* 5. Добавьте новый столбец под названием «время до следующей станции».
Чтобы получить это значение, мы вычитаем время станций для пар смежных станций.
Мы можем вычислить это значение без использования оконной функции SQL,
но это может быть очень сложно. Проще это сделать с помощью оконной функции LEAD.
Эта функция сравнивает значения из одной строки со следующей строкой,
чтобы получить результат. В этом случае функция сравнивает значения в столбце «время»
для станции со станцией сразу после неё */

-- Создание и наполнение таблицы:
DROP TABLE IF EXISTS train_station;
CREATE TABLE train_station (
    id INT PRIMARY KEY AUTO_INCREMENT,
    train_id INT,
    station VARCHAR(20),
    station_time TIME);
    
INSERT INTO train_station (train_id, station, station_time) VALUES
    (110, 'San Francisco', '10:00:00'),
    (110, 'Redwood City', '10:54:00'),
    (110, 'Palo Alto', '11:02:00'),
    (110, 'San Jose', '12:35:00'),
    (120, 'San Francisco', '11:00:00'),
    (120, 'Palo Alto', '12:49:00'),
    (120, 'San Jose', '13:30:00');
    
SELECT
    train_id,
    station,
    station_time,
    TIMEDIFF(
        LEAD(station_time) OVER(PARTITION BY train_id ORDER BY station_time),
        station_time) AS 'time_to_next_station_interval'
FROM train_station;