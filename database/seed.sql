-- seed.sql — dados de exemplo para testar (opcional).
-- Rode DEPOIS do banco.sql, uma vez só (rodar de novo dá "Duplicate entry").

USE barbearia_abobrinha;

-- Os mesmos serviços que o sistema antigo (main.py) já trazia na memória
INSERT INTO servicos (nome, preco) VALUES
    ('Corte de cabelo', 30.00),
    ('Barba', 20.00),
    ('Sobrancelha', 15.00),
    ('Corte de cabelo + Barba + Sobrancelha', 55.00),
    ('Corte de cabelo + Barba', 40.00);

-- Clientes fictícios
INSERT INTO clientes (nome, telefone, email, data_nascimento, problema_quimico) VALUES
    ('Carlos Exemplo', '74999990001', 'carlos@exemplo.com', '1995-03-25', 'Nenhum'),
    ('Marina Teste',   '74999990002', 'marina@exemplo.com', '2001-11-02', 'Alergia a amônia'),
    ('Pedro Menor',    '74999990003', 'pedro@exemplo.com',  '2012-07-14', 'Nenhum');
