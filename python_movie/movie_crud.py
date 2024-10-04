def add_movie(title: str, year: int, conn):
    sql = "INSERT INTO movie (title, year) values (?, ?)"
    with conn.cursor() as cur:
        cur.execute(sql, (title, year))
