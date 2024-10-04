import pytest
from movie_crud import add_movie
import psycopg2 as pg

@pytest.fixture
def conn():
    # TODO!!!!: db ut config read from (env, file, ...)
    #       Carton Rouge:  Code Quality
    # setup
    with pg.connect(
        dsn="dbname=dbmovie user=movie password=password port=5433 host=localhost"
    ) as new_conn:
        yield new_conn
        # teardown
        new_conn.rollback() # or SQL delete, drop, ...
    # end with connect: new_conn.close()

@pytest.mark.parametrize(
        "title, year",
        [
            ("Joker: Folie à Deux", 2024),
            ("Joker: Folie à Deux", 2024),
            ("Le Comte de Monte-Cristo", 2024),
        ],
        ids=[
            "Joker 1st time",
            "Joker 2time",
            "Comte 1st time"
        ]
)
def test_add_movie(title, year, conn):
    # Arange
    title = "Joker: Folie à Deux"
    year = 2024
    # Act
    add_movie(title, year, conn)
    # Assert
    sql_verify = "SELECT id, title, year FROM movie WHERE title = %s AND year = %s"
    with conn.cursor() as cur:
        cur.execute(sql_verify, (title, year))
        response_verify = list(cur)
    assert len(response_verify) == 1
    id_generated, title_read, year_read = response_verify[0]
    assert id_generated is not None
    assert title == title_read
    assert year == year_read
    