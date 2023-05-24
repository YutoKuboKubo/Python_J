import sys
from sqlalchemy import Column, String, Date, Integer, VARCHAR, DateTime
from database import Base
from database import ENGINE


# テーブル：Holidayの定義
class Holiday(Base):
    __tablename__ = 'holiday'
    holi_date = Column('holi_date', Date, primary_key=True)
    holi_text = Column('holi_text', String(20))


# テーブル：Attendnumの定義
class Attendnum(Base):
    __tablename__ = 'attendnum'
    date = Column('entry_date', Date, primary_key=True)
    seq = Column('seq', Integer, primary_key=True)
    adult = Column('adult', Integer)
    child = Column('child', Integer)


# テーブル：商品マスタの定義
class Mst_merchandise(Base):
    __tablename__ = 'mst_merchandise'
    id = Column('id', VARCHAR(10), primary_key=True)
    name = Column('name', VARCHAR(20))
    price = Column('price', Integer)


# テーブル：商品在庫テーブルの定義
class Tbl_stock(Base):
    __tablename__ = 'tbl_stock'
    id = Column('id', VARCHAR(10), primary_key=True)
    stock = Column('stock', Integer)


# テーブル：貨幣格納テーブルの定義
class Tbl_money(Base):
    __tablename__ = 'tbl_money'
    price = Column('price', Integer, primary_key=True)
    number = Column('number', Integer)


# テーブル：メッセージテーブルの定義
class Tbl_message(Base):
    __tablename__ = 'tbl_message'
    seq = Column('seq', Integer, primary_key=True)
    message = Column('message', VARCHAR(100))
    datetime = Column('datetime', DateTime)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)
