# Use the official MySQL 8.0 image as the base
FROM mysql:8.0.33-0ubuntu0.20.04.2

LABEL maintainer="Mateus Oliveira da Silva <oliveira.mats.oo@gmail.com>"
ENV TZ=America/Sao_Paulo

# Set the MySQL root password (change "your_password" to your desired password)
ENV MYSQL_ROOT_PASSWORD=12345678

# Expose the MySQL port (default is 3306)
EXPOSE 3360

# Start MySQL server when the container launches
CMD ["mysqld"]