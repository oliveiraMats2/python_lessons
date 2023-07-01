FROM ubuntu:20.04

LABEL maintainer="Mateus Oliveira da Silva <oliveira.mats.oo@gmail.com>"
ENV TZ=America/Sao_Paulo

# Install MySQL dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server=8.0.33-0ubuntu0.20.04.2 mysql-client=8.0.33-0ubuntu0.20.04.2 \
    && rm -rf /var/lib/apt/lists/*

# Set the MySQL root password (change "your_password" to your desired password)
ENV MYSQL_ROOT_PASSWORD=12345678

# Expose the MySQL port (default is 3306)
EXPOSE 3306

# Start MySQL server when the container launches
CMD ["mysqld"]
