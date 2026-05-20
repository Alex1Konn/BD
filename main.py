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