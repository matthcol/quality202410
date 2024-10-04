def add_movie(title: str, year: int, conn):
    sql = "INSERT INTO movie (title, year) values (%s, %s)"
    with conn.cursor() as cur:
        cur.execute(sql, (title, year))
