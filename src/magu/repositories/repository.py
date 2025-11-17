#from magu.database.database import MySQLDatabase as mysql
from magu.database.database import MariaDBDatabase as mariadb
from magu.models.model import Model
from magu.models.model import Column

class MySQLRepository:
    def __init__(self, model: Model.__class__):
        self.model = model

    def save(self):
        table = self.model._table

        for attr in self.model.__dict__:
            print(attr, self.model.__dict__[attr])

        #with mysql.session() as session:
            ...#session.execute("INSERT INTO %s VALUEs ()", (table,))

class MariaDBRepository:
    def __init__(self, model: Model.__class__):
        self.model = model
        self.table = self.model._table
        self.columns = [
            name for name, attr in self.model.__dict__.items()
            if isinstance(attr, Column)
            if not attr.id
        ]
        self.columns_id = [
            name for name, attr in self.model.__dict__.items()
            if isinstance(attr, Column)
        ]

        for name, attr in self.model.__dict__.items():
            if isinstance(attr, Column) and attr.id:
                self.id = name

    def find_all(self):
        with mariadb.session() as session:
            session.execute(f"SELECT * FROM `{self.table}`")
            res = session.fetchall()
            for i in range(len(res)):
                res[i] = dict(zip(self.columns_id, res[i]))
            return res

    def find_by_id(self, id):
        with mariadb.session() as session:
            session.execute(f"SELECT * FROM `{self.table}` WHERE `{self.id}` = {id}")
            return dict(zip(self.columns, session.fetchone()))
        

    def save(self, entity: Model):
        values = [getattr(entity, col) for col in self.columns]

        placeholders = ",".join("%s" for _ in self.columns)

        query = f"INSERT INTO `{self.table}` ({",".join(f"`{value}`" for value in self.columns)}) VALUES ({placeholders});"
        fetch = f"SELECT * FROM `{self.table}` WHERE `{self.id}` = %s"
        with mariadb.session() as session:
            session.execute(query, values)
            
            last_id = session.lastrowid
            entity.id = last_id

            session.execute(fetch, (last_id,))
            res = dict(zip(self.columns_id, session.fetchone()))
            return res
