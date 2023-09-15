-- Active: 1694736725633@@127.0.0.1@3306
CREATE TABLE IF NOT EXISTS sistemas (
cod_sistema VARCHAR(15) UNIQUE NOT NULL PRIMARY KEY,
nome_sistema VARCHAR(20) UNIQUE NOT NULL);

INSERT INTO sistemas(cod_sistema, nome_sistema) VALUES 
('admin1', 'Administrador'),
('coord1', 'Coordenador'),
('dir1','Diretor'),
('prof-mat', 'Professor de Matematica'),
('alun1', 'Aluno'),
('prof-port', 'Professor de Portugues');

DROP TABLE sistemas;

