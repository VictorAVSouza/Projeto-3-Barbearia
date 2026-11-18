-- banco.sql — cria o banco e as tabelas da Barbearia Abobrinha.
-- Rode UMA vez (MySQL Workbench: abra o arquivo e clique no raio).

CREATE DATABASE IF NOT EXISTS barbearia_abobrinha
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE barbearia_abobrinha;

-- Clientes. O telefone é guardado só com números e não pode repetir.
CREATE TABLE IF NOT EXISTS clientes (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    nome             VARCHAR(100) NOT NULL,
    telefone         VARCHAR(15)  NOT NULL UNIQUE,
    email            VARCHAR(120) NOT NULL,
    data_nascimento  DATE         NOT NULL,
    problema_quimico VARCHAR(150) NOT NULL DEFAULT 'Nenhum',
    criado_em        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Serviços da barbearia. O nome não pode repetir.
CREATE TABLE IF NOT EXISTS servicos (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    nome      VARCHAR(100) NOT NULL UNIQUE,
    preco     DECIMAL(8,2) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Fila de espera: quem tem o menor id chegou primeiro.
-- Cada cliente aparece uma vez só (UNIQUE). Se o cliente for excluído, sai da fila junto.
CREATE TABLE IF NOT EXISTS fila_espera (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL UNIQUE,
    criado_em  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id) ON DELETE CASCADE
);

