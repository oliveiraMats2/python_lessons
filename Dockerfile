FROM mysql:latest

COPY data_vector.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=123

EXPOSE 3306
