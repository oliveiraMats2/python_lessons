CREATE DATABASE data_vector;
USE data_vector;

CREATE TABLE coordenadas (
    id INT PRIMARY KEY,
    x FLOAT,
    y FLOAT,
    z FLOAT
);

CREATE TABLE magnitude (
    id INT PRIMARY KEY,
    mag FLOAT
);
