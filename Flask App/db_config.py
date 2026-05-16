import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hR$@X5882@",
        database="student_performance"
    )

    return connection