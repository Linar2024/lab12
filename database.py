import sqlalchemy as sqla
import database 
CONNECTION_STRING = "mysql+pymysql://root@localhost/db"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connection = self.engine.connect()
    def translate_to_dict(self, result_raw):
        result = []
        for r in result_raw:
            result.append(r._asdict())
        return result    
    def get_news(self):
        query = sqla.text("SELECT * FROM news")
        result_raw = self.connection.execute(query).all()
        return self.translate_to_dict(result_raw)
    def del_news(self, id):
        query = sqla.text("DELETE FROM news WHERE id = :id")
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        result = self.connection.commit()
        return result
    def add_news(self, name):
        query = sqla.text("INSERT INTO news (name) VALUES (:name)")
        query = query.bindparams(sqla.bindparam("name", name))
        self.connection.execute(query)
        self.connection.commit()
    def edit_news(self, name, id):
        query = sqla.text("UPDATE news SET name = :name WHERE id = :id")
        query = query.bindparams(sqla.bindparam("name", name))
        query = query.bindparams(sqla.bindparam("id", id))
        self.connection.execute(query)
        self.connection.commit()