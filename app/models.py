from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)

class OrdemDeServico(Base):
    __tablename__ = "ordens_de_servico"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    data_de_entrada = Column(DateTime)
    data_de_entrega = Column(DateTime)
    valor = Column(Float)

class Material(Base):
    __tablename__ = "materiais"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)