# Rasta Serviços de Lanternagem e Pintura

## Proposta 
faça um sistema em python para uma oficina mecanica, com cadastro de funcionarios e clientes ordem de serviço com os dados do cliente valor data da entrega e entrada e o valor que sera paga daquele serviço para o funcionario mais os material usado, isso entrará no contas a pagar e o receber será o saldo desta transação. Monte o banco de dados em mysql ou potegress e esse sistema tem q ter intefarce grafica rodar na werb. sera contenerizado em doker e enviada oara o oke na oracle cloud como imagem no registe. Informe todos os arquivos


## Arquivos necessários:

app.py: o arquivo principal do sistema que contém a lógica de negócios e a interface gráfica
models.py: o arquivo que define os modelos de dados para o banco de dados
database.py: o arquivo que configura a conexão com o banco de dados
templates: pasta que contém os arquivos HTML para a interface gráfica
static: pasta que contém os arquivos estáticos (CSS, JavaScript, etc.)
requirements.txt: arquivo que lista as dependências do sistema
Dockerfile: arquivo que define como construir a imagem do sistema em Docker
docker-compose.yml: arquivo que define como executar o sistema em Docker

oficina-mecanica/
app/
__init__.py
models.py
routes.py
requirements.txt
templates/
index.html
base.html (opcional)
static/
css/
style.css
js/ (opcional)
images/ (opcional)
Dockerfile
docker-compose.yml
kubernetes/
deployment.yaml
service.yaml
persistent-volume-claim.yaml
persistent-volume.yaml
README.md