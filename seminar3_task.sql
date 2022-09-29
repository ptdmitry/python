USE lesson_3;

-- Задание №1
-- Создание таблицы "Продавцы"
DROP TABLE IF EXISTS salespeople;
CREATE TABLE salespeople (
    id INT PRIMARY KEY AUTO_INCREMENT,
    snum INT,
    sname VARCHAR(45),
    city VARCHAR(45),
    comm DECIMAL(2,2));

-- Заполнение таблицы "Продавцы"
INSERT INTO salespeople (snum, sname, city, comm) VALUES
    (1001, "Peel", "London", .12),
    (1002, "Serres", "San Jose", .13),
    (1004, "Motika", "London", .11),
    (1007, "Rifkin", "Barcelona", .15),
    (1003, "Axelrod", "New York", .10);

-- Создание таблицы "Заказчики"
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnum INT,
    cname VARCHAR(45),
    city VARCHAR(45),
    rating INT,
    snum INT);
    
-- Заполнение таблицы "Заказчики"
INSERT INTO customers (cnum, cname, city, rating, snum) VALUES
    (2001, "Hoffman", "London", 100, 1001),
    (2002, "Giovanni", "Rome", 200, 1003),
    (2003, "Liu", "San Jose", 200, 1002),
    (2004, "Grass", "Berlin", 300, 1002),
    (2006, "Clemens", "London", 100, 1001),
    (2008, "Cisneros", "San Jose", 300, 1007),
    (2007, "Pereira", "Rome", 100, 1004);
    
-- Создание таблицы "Заказы"
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    onum INT,
    amt DECIMAL(6,2),
    odate DATE,
    cnum INT,
    snum INT);

-- Заполнение таблицы "Заказы"
INSERT INTO orders (onum, amt, odate, cnum, snum) VALUES
    (3001, 18.69, "1990/03/10", 2008, 1007),
    (3003, 767.19, "1990/03/10", 2001, 1001),
    (3002, 1900.1, "1990/03/10", 2007, 1004),
    (3005, 5160.45, "1990/03/10", 2003, 1002),
    (3006, 1098.16, "1990/03/10", 2008, 1007),
    (3009, 1713.23, "1990/04/10", 2002, 1003),
    (3007, 75.75, "1990/04/10", 2006, 1001),
    (3008, 4723, "1990/05/10", 2006, 1001),
    (3010, 1309.95, "1990/06/10", 2004, 1002),
    (3011, 9891.88, "1990/06/10", 2006, 1001);
    
/* 1. Напишите запрос который вывел бы таблицу со столбцами в следующем порядке:
city, sname, snum, comm (к первой или второй таблице, используя SELECT) */
SELECT city, sname, snum, comm FROM salespeople;

/* 2. Напишите команду SELECT, которая вывела бы оценку(rating), сопровождаемую
именем каждого заказчика в городе San Jose (“заказчики”) */
SELECT cname, rating, city FROM customers
WHERE city = "San Jose";

/* 3. Напишите запрос, который вывел бы значения snum всех продавцов из таблицы заказов
без каких бы то ни было повторений (уникальные значения в “snum“ “Продавцы”) */
SELECT DISTINCT snum FROM orders;

/* 4*. Напишите запрос, который бы выбирал заказчиков, чьи имена начинаются с буквы G.
Используется оператор "LIKE": (“заказчики”) https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html  */
SELECT cname FROM customers
WHERE cname LIKE "G%";

/* 5. Напишите запрос, который может дать вам все заказы со значениями суммы выше чем $1,000
(“Заказы”, “amt” - сумма) */
SELECT * FROM orders
WHERE amt > 1000;

/* 6. Напишите запрос который выбрал бы наименьшую сумму заказа
(Из поля “amt” - сумма в табличке “Заказы” выбрать наименьшее значение) */
SELECT MIN(amt) AS min_order FROM orders;

/* 7. Напишите запрос к табличке “Заказчики”, который может показать всех заказчиков,
у которых рейтинг больше 100 и они находятся не в Риме */
SELECT * FROM customers
WHERE rating > 100 AND city != "Rome";

-- Задание №2
-- Создание таблицы штата фирмы
DROP TABLE IF EXISTS new_staff;
CREATE TABLE new_staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(45),
    surname VARCHAR(45),
    speciality VARCHAR(45),
    seniority INT,
    salary INT,
    age INT);
    
-- Заполнение таблицы штата фирмы
INSERT INTO new_staff (`name`, surname, speciality, seniority, salary, age) VALUES
    ("Вася", "Васькин", "Начальник", 40, 100000, 60),
    ("Петя", "Петькин", "Начальник", 8, 70000, 30),
    ("Катя", "Катькина", "Инженер", 2, 70000, 25),
    ("Саша", "Сашкин", "Инженер", 12, 50000, 35),
    ("Иван", "Иванов", "Рабочий", 40, 30000, 59),
    ("Пётр", "Петров", "Рабочий", 20, 25000, 40),
    ("Сидор", "Сидоров", "Рабочий", 10, 20000, 35),
    ("Антон", "Антонов", "Рабочий", 8, 19000, 28),
    ("Юра", "Юркин", "Рабочий", 5, 15000, 25),
    ("Максим", "Воронин", "Рабочий", 2, 11000, 22),
    ("Юра", "Галкин", "Рабочий", 3, 12000, 24),
    ("Люся", "Люськина", "Уборщик", 10, 10000, 49);
    
-- 1. Отсортируйте поле “зарплата” в порядке убывания:
SELECT * FROM new_staff
ORDER BY salary DESC;

-- в порядке  возрастания:
SELECT * FROM new_staff
ORDER BY salary ASC;

/*  2. Отсортируйте по возрастанию поле “Зарплата”
и выведите 5 строк с наибольшей заработной платой */
SELECT * FROM new_staff
ORDER BY salary
LIMIT 7,5;

 /* 3. Выполните группировку всех сотрудников по специальности “рабочий”,
 зарплата которых превышает 20000 */
 SELECT speciality, COUNT(speciality) AS num_worker FROM new_staff
 WHERE salary > 20000
 GROUP BY speciality
 HAVING speciality IN("Рабочий");
