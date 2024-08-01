-- Criação de uma tabela para armazenar as respostas da pesquisa
CREATE TABLE survey_responses (
    id SERIAL PRIMARY KEY,
    response TEXT NOT NULL
);
