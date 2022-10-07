USE lesson_6;

/* 1. Создайте функцию, которая принимает кол-во сек и форматирует их
в кол-во дней, часов, минут и секунд.
Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds' */

DROP FUNCTION IF EXISTS sec_to_datetime;
DELIMITER //
CREATE FUNCTION sec_to_datetime (num INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE days INT DEFAULT 0;
    DECLARE hours INT DEFAULT 0;
    DECLARE minuts INT DEFAULT 0;
    DECLARE seconds INT DEFAULT 0;
    DECLARE result VARCHAR(255);
    IF num > 0 THEN
        SET days = FLOOR(num / 86400);
        SET hours = FLOOR(num / 3600 % 24);
        SET minuts = FLOOR(num / 60 % 60);
        SET seconds = FLOOR(num % 60);
        SET result = CONCAT(days, ' days ', hours, ' hours ', minuts, ' minuts ', seconds, ' seconds ');
        RETURN result;
	ELSE
        RETURN 'Введено отрицательное число';
    END IF;
END//
DELIMITER ;
    
SELECT sec_to_datetime(123456) AS 'Конвертер секунд';

/* 2. Выведите только четные числа от 1 до 10 включительно.
Пример: 2,4,6,8,10 (можно сделать через шаг + 2: х = 2, х+=2) */

DROP PROCEDURE IF EXISTS even_numbers;
DELIMITER //
CREATE PROCEDURE even_numbers()
BEGIN
    DECLARE x INT DEFAULT 2;
    DECLARE even_arr VARCHAR(45);
    SET even_arr = '';
    REPEAT
        SET even_arr = CONCAT(even_arr, x, ', ');
        SET x = x + 2;
        UNTIL x > 10
	END REPEAT;
    SELECT even_arr AS 'Чётные числа';
END//
DELIMITER ;

CALL even_numbers();