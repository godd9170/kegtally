from django.db import connection
from collections import namedtuple


def get_db_rows(sql, args=None):
    """
    Given a string SQL query, performs it and returns rows as
    named tuples.
    https://stackoverflow.com/questions/39381436/graphql-django-resolve-queries-using-raw-postgresql-query
    """
    cursor = connection.cursor()
    cursor.execute(sql, args)
    columns = [col[0] for col in cursor.description]
    RowType = namedtuple('Row', columns)
    data = [
        RowType(*row)  # Edited by John suggestion fix
        for row in cursor.fetchall()]

    cursor.close()
    return data
