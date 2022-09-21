USE lesson_1;
DROP TABLE phones;

/* 1. Создайте таблицу с мобильными телефонами, используя графический 
интерфейс. Заполните БД данными. Добавьте скриншот */

CREATE TABLE `phones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ProductName` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `ProductCount` INT NOT NULL,
  `Price` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ProductName_UNIQUE` (`ProductName` ASC) VISIBLE);

INSERT INTO `lesson_1`.`phones` (`ProductName`, `Manufacturer`, `ProductCount`, `Price`) VALUES ('iPhone X', 'Apple', '3', '76000');
INSERT INTO `lesson_1`.`phones` (`ProductName`, `Manufacturer`, `ProductCount`, `Price`) VALUES ('iPhone 8', 'Apple', '2', '51000');
INSERT INTO `lesson_1`.`phones` (`ProductName`, `Manufacturer`, `ProductCount`, `Price`) VALUES ('Galaxy S9', 'Samsung', '2', '56000');
INSERT INTO `lesson_1`.`phones` (`ProductName`, `Manufacturer`, `ProductCount`, `Price`) VALUES ('Galaxy S8', 'Samsung', '1', '41000');
INSERT INTO `lesson_1`.`phones` (`ProductName`, `Manufacturer`, `ProductCount`, `Price`) VALUES ('P20 Pro', 'Huawei', '5', '36000');

/* 2. Выведите название, производителя и цену для товаров, 
количество которых превышает 2 (SQL - файл, скриншот, либо сам 
код) */

SELECT ProductName, Manufacturer, Price
FROM phones
WHERE ProductCount > 2;

/* 3. Выведите весь ассортимент товаров марки “Samsung” */

SELECT ProductName, ProductCount, Price
FROM phones
WHERE Manufacturer = "Samsung";

/* Доп. задание: (SQL advanced)
4. С помощью регулярных выражений найти:
4.1. Товары, в которых есть упоминание "Iphone" */

SELECT *
FROM phones
WHERE ProductName REGEXP "iPhone";

/* 4.2. Товары, в которых есть упоминание "Samsung" */

SELECT *
FROM phones
WHERE ProductName || Manufacturer REGEXP "Samsung";

/* 4.3. Товары, в которых есть ЦИФРЫ */

SELECT *
FROM phones
WHERE ProductName REGEXP '[0-9]';

/* 4.4. Товары, в которых есть ЦИФРА "8" */

SELECT *
FROM phones
WHERE ProductName REGEXP '[8]';

/* 5. В чем отличие 0 от NULL?
0 - это значение, равное нулю
NULL - это пустое, незаполненное поле, значение отсутствует
*/

