from sqlalchemy import create_engine, Column, Integer, String, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from application.interfaces.venda_repository import IVendaRepository
from domain.models.venda import Venda

Base = declarative_base()

class SQLiteVenda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, Sequence('venda_id_seq'), primary_key=True)
    total = Column(Float)
    data_hora = Column(String)

class SQLiteVendaRepository(IVendaRepository):
    def __init__(self, db_url='sqlite:///my_database.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, venda: Venda):
        session = self.Session()
        nova_venda = SQLiteVenda(total=venda.get_total(), data_hora=str(venda.data_hora))
        session.add(nova_venda)
        session.commit()
        session.close()

    def get_all(self):
        session = self.Session()
        vendas = session.query(SQLiteVenda).all()
        session.close()
        return vendas

    def get_by_id(self, venda_id: int):
        session = self.Session()
        venda = session.query(SQLiteVenda).filter(SQLiteVenda.id == venda_id).first()
        session.close()
        return venda

    def delete(self, venda_id: int):
        session = self.Session()
        venda = session.query(SQLiteVenda).filter(SQLiteVenda.id == venda_id).first()
        if venda:
            session.delete(venda)
            session.commit()
        session.close()