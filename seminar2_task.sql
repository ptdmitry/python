USE lesson_2;
DROP TABLE IF EXISTS sales;

/* 1.  Используя операторы языка SQL, создайте табличку “sales”. Заполните ее данными */

CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE NOT NULL,
    bucket INT NOT NULL);

INSERT sales (order_date, bucket)
VALUES
('2021-01-01', 140),
('2021-01-02', 400),
('2021-01-03', 200),
('2021-01-04', 250),
('2021-01-05', 120),
('2021-01-06', 380),
('2021-01-07', 420),
('2021-01-08', 80);

/* 2. Разделите значения количества в 3 сегмента — меньше 100(“Маленький заказ”), 
100-300(“Средний заказ” и больше 300 (“Большой заказ”). Используйте оператор IF */

SELECT order_date, bucket,
IF (bucket < 100, 'Маленький заказ',
(IF (bucket >= 100 AND bucket < 300, 'Средний заказ',
(IF (bucket > 300, 'Большой заказ', 'Не было заказов')))))
AS 'Размер заказа'
FROM sales;

/* 3. Создайте таблицу “orders”, заполните ее значениями. Покажите “полный” 
статус заказа, используя оператор CASE */

DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
	id INT PRIMARY KEY AUTO_INCREMENT,
    employe_eid VARCHAR(10) NOT NULL,
    amount DECIMAL(5,2) NOT NULL,
    orderstatus VARCHAR(45));

INSERT orders (employe_eid, amount, orderstatus)
VALUES
('e03', 15, 'OPEN'),
('e01', 25.5, 'OPEN'),
('e05', 100.7, 'CLOSED'),
('e02', 22.18, 'OPEN'),
('e04', 9.5, 'CANCELLED'),
('e04', 99.99, 'OPEN');

SELECT id, orderstatus,
CASE orderstatus
    WHEN 'OPEN' THEN 'Order is in open state'
    WHEN 'CLOSED' THEN 'Order is closed'
    WHEN 'CANCELLED' THEN 'Order is cancelled'
END AS order_summary
FROM orders;