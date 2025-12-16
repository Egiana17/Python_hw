import pytest
from sqlalchemy import create_engine, text
from subject import SubjectTable

db_connection_string = "postgresgl://postgres@localhost:5432/postgres"

@pytest.fixture()
def db_connection():
    engine = create_engine(db_connection_string)
    connection = engine.connect
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()


    @pytest.fixture()
    def subject_table(db_connection):
        return SubjectTable(db_connection_string)
    