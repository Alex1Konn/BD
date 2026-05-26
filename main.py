"""
БД - набор взаимосвязаных зависимостей
СУБД - комплекс программных средств для управления данными
СУБД - отвечает за поддержку языка БД,
 механизмы хранения и извлечения данных,
оптимизацию процесов извлечения данных И СОЗДАНИЕ БД
SQL

Типы СУБД:
Клиент-серверные: MySQL, PostgreSQL
Файл-верверные: Microsoft Access
Встраиваемые: SQLite

Основные клиент-серверные:
Oracle
PostgreSQL
MySQL
Microsoft Access
SQLite
MS SQL
MariaDB

все они РЕЛЯЦИОННЫЕ - БД в которых данных
хранятся в таблицах и все они поддерживают язык SQL

НЕРЕЛЯЦИОННЫЕ СУБД
существовали задолго до реляционныех (иерархические)

Появились NoSQL движение
mongoDB - одна из нгаиболее популярных NoSQL-СУБД
Реляционные СУБД не хуже и не лучше не реляционных СУБД
У всех видов есть свои преимущества и недостатки


Теоритическиой основной служит реляционная алгебра
Реляционная алгебра определяет систему операций
над отношениями(таблицами):
объеденинение, пересечение, вычитание, соеденинеи  и т.д.

Все эти операции выражаются через SQL


РЕЛЯЦИОННАЯ МОДЕЛЬ
Сущность - например, клиенты, заказы, поставщики
Таблица - отношение
Столбец - атрибут
Строка/запись - кортеж
Результирующий набор - результат запроса QL:
SELECT contact_name, address, city
FROM customers
LIMIT 13

SQL
результатом SQL запроса является
результирующий набор (как правило -траблиция)
Транзакция - в ней может находиться несоклько запросов

DDL Data Definition language - CREATE ALTER DROP
DML 9Data Manipulation Language) SELECT INSET UDDATE DELETE
TCL(transaction Control Language COMMIT ROLLBACK SAVEPOINT
DCL Data Control Lanquage - GRANT REVOKE DENY
ANSI sql-92
Различные в процедурных расширенияхЖ
Pl/SQL, T-SQL


________________

PostgreSQL
Free (Open Source)
Лучший выбор для изучения - проинсталлировал и понеслась
Взрослая СУБД, хорошая
поддерживающая транзакционность из коробки
Весьма развитой дталект SQL
В сравнении с MySQl есть свои плюсы и минусы
В любом случае 90%  возможностей диалекта SQL
подерживающегто Postgres  можно использовать в дру СУБД


Повторить основные типы данных
Так же есть другие типы данных:
Arrays (массивы)
JSON
XML
Геометрические данных и др спец типы
Custom-типы
NULL - отсутсвие данных

Пароль root


Способы создания БД - через код или через интерфейс

Удалить ДБ - drop(Force) удалить безопастно


Созда через код - выбрать постгре - нажать query tools - в поле
пишем CREATE DATABASE testdb - и потом нажиаем F5 - Database и выбрать refreshe

DROP DATABASE IF EXISTS testdb WITH (FORCE)

CREATE TABLE publisher
(
	publisher_id integer PRIMARY KEY,
	org_name varchar(128) NOT NULL,
	address text NOT NULL
)


-- CREATE TABLE book
-- (
-- 	book_id integer PRIMARY KEY,
-- 	title text NOT NULL,
-- 	isbn varchar(32) NOT NULL
-- )

DROP TABLE publisher;
DROP TABLE book
varchar текстовое значение с ограничем симввовлов или chacter vaying  в выборке интерфейса

-- INSERT INTO book VALUES (1, 'Красна шапочка', '452306750234670')
SELECT * FROM book

-- INSERT INTO book VALUES (1, 'Красна шапочка', '452306750234670')
-- SELECT * FROM book

-- INSERT INTO publisher
-- VALUES
-- (1, 'Everyeman``s Library', 'New York'),
-- (2, 'Oxford University Press', 'New York'),
-- (3, 'Grand Central Publishing', 'Washington'),
-- (4, 'Simon & Schuster', 'Chicago')

SELECT * FROM publisher
"""
# зАНЯТИЕ 26.05.26 СВЯЗИ ОДИН КО МНОГИМ
REFERENCES - команда для свзяывания с другой таблицей серез
fk_publisher_id integer REFERENCES publisher(publisher_id)

ERD _ посмотреть взаимосязи таблицы

-- CREATE TABLE book
-- (
-- 	book_id integer PRIMARY KEY,
-- 	title text NOT NULL,
-- 	isbn varchar(32) NOT NULL,
-- 	fk_publisher_id integer REFERENCES publisher(publisher_id) NOT NULL
-- )

INSERT INTO book
VALUES
(1, 'Гномы', '475827506503', 1),
(2, 'Томы', '475827506502', 1),
(3, 'Ладно', '475827506505', 2),
(4, 'Потом', '475827506507', 3),
(5, 'Здесь', '475827506509', 4)


# второй вариант без удаления таблицы - добавляем колнку и потом взимосвязи
ALTER TABLE book
ADD COLUMN fk_publisher_id;

ALTER TABLE book
ADD CONSTRANT fk_book_publisher
FOREIGN KEY(fk_publisher_id ) REFERENCES publisher(publisher_id)

FOREIGN KEY - внешний ключ

# ОДИН К ОДНОМУ - (У ОДНОГО ЧЕЛОВЕКА ОДИН ПАСПОРТ)
CREATE TABLE person(
	person_id int PRIMARY KEY,
	first_name varchar(64) NOT NULL,
	last_name varchar(64) NOT NULL
);

CREATE TABLE passport(
	passport_id int PRIMARY KEY,
	serial_number int NOT NULL,
	registration text NOT NULL,
	fk_passport_person int UNIQUE REFERENCES person(person_id)
)

пакетная ставка - это множественная ставка строк в таблицу
-- INSERT INTO person(person_id, first_name, last_name)
-- VALUES
-- (1, 'Vasia', 'Snow'),
-- (2, 'Ned', 'Stark'),
-- (3, 'Rob', 'Bob'),
-- (4, 'Dag', 'Week')

SELECT * FROM person

-- INSERT INTO passport(passport_id, serial_number, registration, fk_passport_person)
-- VALUES
-- (1, 123456, 'Winterfell', 1),
-- (2, 123457, 'Summerfell', 2),
-- (3, 123458, 'Springfell', 3),
-- (4, 123459, 'Autumnfell', 4)

-- SELECT * FROM passport

# МНОГИЕ КО МНОГИМ

удалить содержимое таблиуцы book (строчки) TRUNCATE book ИЛИ DELETE FROM book
Далее
INSERT INTO book
VALUES
(1, 'Book for Dumnies', '123456', 1),
(2, 'Book for Smart Gyes', '789456', 1),
(3, 'Book for Happy People', '123456', 2),
(4, 'Book for Dumnies', '123456', 2);

CREATE TABLE author
(
	autor_id int PRIMARY KEY,
	full_name text NOT NULL,
	rating real
);

INSERT INTO author
VALUES
(1, 'Bob', 4.5),
(2, 'Alice', 4.0),
(3, 'Bob', 4.7)

Делаем результирующую таблицу

CREATE TABLE book_author
(
	book_id int REFERENCES book (book_id),
	author_id int REFERENCES author (author_id),

	CONSTRAINT book_author_pkey PRIMARY KEY (book_id, author_id)
);

INSERT INTO book_author
VALUES
(1, 1),
(2, 1),
(3, 1),
(3, 2),
(4, 1),
(4, 2),
(4, 3)


""""
Задания

CREATE TABLE employees(
	id int PRIMARY KEY,
	full_name text NOT NULL
	)

CREATE TABLE employee_profiles
	(
	id int PRIMARY KEY,
	employee_id int NOT NULL,
	position text NOT NULL,
	salary int NOT NULL
	)
	
INSERT INTO employees
VALUES
(1, 'Иванов Петр'),
(2, 'Силанова Анастасия'),
(3, 'Бузухов Константин')

INSERT INTO employee_profiles
VALUES
(1, 345, 'работник', 10000),
(2, 344, 'работник', 10000),
(3, 343, 'работник', 10000)
"""