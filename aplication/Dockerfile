# Usando uma imagem base com Python
FROM python:3.9-slim

# Instalar dependências
RUN apt-get update && apt-get install -y libaio1 wget unzip

# Instalar o Oracle Instant Client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
    && unzip instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
    && rm instantclient-basiclite-linux.x64-19.8.0.0.0dbru.zip \
    && mv instantclient_19_8 /opt/oracle

# Configurar o Oracle Client
ENV LD_LIBRARY_PATH /opt/oracle
ENV TNS_ADMIN /opt/oracle

# Instalar bibliotecas Python necessárias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar a aplicação
COPY . /app
WORKDIR /app

# Definir variáveis de ambiente
ENV ORACLE_HOST=your_oracle_host
ENV ORACLE_PORT=1521
ENV ORACLE_SERVICE_NAME=your_service_name
ENV ORACLE_USER=your_user
ENV ORACLE_PASSWORD=your_password

# Expor a porta
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
