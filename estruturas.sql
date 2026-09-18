CREATE DATABASE loja_db;

-- Apagar o banco de dados
-- DROP DATABASE loja_db;

USE loja_db;

CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(200),
    nome VARCHAR(50) NOT NULL
);

-- Apagar a tabela de produtos
-- DROP TABLE produtos;

SELECT id, nome, descricao FROM produtos;

INSERT INTO produtos (nome, descricao) VALUE ("Samsung Neo QLED 4k 65", "'TV mais linda do mundo");

INSERT INTO produtos (nome, descricao) VALUES
("Positivo Dual Core 2Gb", "Computador Melhor que tem"), 
("Garmin Instict", NULL),
("Garmin Instict", "");

SELECT id, nome, descricao FROM produtos;

SELECT id, nome, descricao FROM produtos WHERE id = 4;

INSERT INTO produtos (nome, descricao) VALUE ("Sony Ericsson w 200i", "Celular Infravermelho");

SELECT id, nome, descricao FROM produtos;

-- Consultar os produtos que tem NULL na descrição
SELECT id, nome, descricao FROM produtos WHERE descricao IS NULL;

UPDATE produtos SET descricao = "GPS, laranja" WHERE id = 3;

-- CRUD
-- CREATE
-- READ
-- UPDATE
-- DELETE

MySQL Command line

env
python mysql connector
--> py -m pip install mysql-connector-python
--> py -m pip install mysql-connector-python --break-system-packages

