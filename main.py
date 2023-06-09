from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
database_url = 'mysql+pymysql://root:Senac2021@localhost:3306/locadora'


class Filme(Base):
    __tablename__ = 'filme'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme [Título = {self.titulo}, Genero = {self.genero}, Ano = {self.ano}]'


def create_database():
    engine = create_engine(database_url, echo=True)
    try:
        engine.connect()
    except Exception as e:
        if '1049' in str(e):
            engine = create_engine(database_url.rsplit('/', 1)[0], echo=True)
            conn = engine.connect()
            conn.execute('CREATE DATABASE locadora')
            conn.close()
            print('Banco locadora criado com sucesso')
        else:
            raise e

create_database()

#Configurações
engine = create_engine(database_url, echo=True)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

def create_table():
    Base.metadata.create_all(engine)
    print('Tabela filme criada com sucesso')
create_table()

# insercao de Dados
# data_insert = Filme(titulo='Batman', ano=2022, genero='ação')
# session.add(data_insert)
# session.commit()
# session.close()


# #Remoção do Banco
# session.query(Filme).filter(Filme.titulo == 'Batman Begins').delete()
# session.commit()
# session.close()

#Atualização de Dados
# session.query(Filme).filter(Filme.titulo == 'Batman').update( {'titulo' : 'Batman Begins' })
# session.query(Filme).filter(Filme.ano == '2022').update({'ano' : 2005})
# session.commit()
# session.close()

#Consulta de Dados
data = session.query(Filme).all()
print(f'filmes {data}')

session.close()