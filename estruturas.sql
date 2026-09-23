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

#--------------------------------------------------------

USE loja_db;

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cnpj VARCHAR(20),
    nome VARCHAR(50) NOT NULL
);

INSERT TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cnpj VARCHAR(14) NOT NULL
);

-- Apagar a tabela de clientes
-- DROP TABLE clientes;

SELECT id, nome, cnpj, endereco, telefone, email, limite_credito FROM clientes;

INSERT INTO clientes (nome, cnpj) VALUE ("HG Textil", "07292007000186");

ALTER TABLE clientes
ADD endereco VARCHAR(255),
ADD telefone VARCHAR(20),
ADD email VARCHAR(100),
ADD limite_credito DECIMAL(10,2) DEFAULT 0.00;+


#############################################################
# Ex. 02: Criar um novo banco de dados chamado helpdesk:
# - Criar uma tabela de categorias com: nome, cor da categoria (hexadecimal) e id
#       Fazer o consultar categorias no python
#       Fazer o cadastro da categoria no python
# - Criar uma tabela de tickets com os seguintes campos:
# id int
# numero_protocolo: str
# titulo: str
# descricao: str
# status: str(ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO)
# prioridade: str(BAIXA, MEDIA, ALTA)
# setor: (TI, RH, FINANCEIRO, ADMINISTRATIVO, MANUTENCAO)
# descricao_solucao: str
# data_criacao: datetime
# Fazer o CRUD em python para permitir interagir com a tabela de tickets


CREATE DATABASE helpdesk;

USE helpdesk;



CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cor_hex VARCHAR(7) NOT NULL -- Exemplo: #67d7c7
);

INSERT INTO categorias (nome, cor_hex) VALUE ("Infra", "#5d00ff");

CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_protocolo VARCHAR(20) NOT NULL UNIQUE,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    status ENUM('ABERTO', 'EM_ANALISE', 'RESOLVIDO', 'CANCELADO') DEFAULT 'ABERTO',
    prioridade ENUM('BAIXA', 'MEDIA', 'ALTA') DEFAULT 'MEDIA',
    setor ENUM('TI', 'RH', 'FINANCEIRO', 'ADMINISTRATIVO', 'MANUTENCAO') NOT NULL,
    descricao_solucao TEXT,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);