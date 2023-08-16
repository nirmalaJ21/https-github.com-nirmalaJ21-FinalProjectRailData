import json

import psycopg2

def push_data_to_postgres(data_json):
    """
    Pushes the data to the PostgresSQL database.
    """

    conn = psycopg2.connect(
        host="database-1.cqfnswik0i0s.us-east-2.rds.amazonaws.com",
        database="DarwinTwo",
        user="gcpostgres",
        password="yb9GPoXzcdaLPFQO2ULv",
    )

    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO darwin (data) VALUES (%s)",
            (json.dumps(data_json),),
        )

    conn.commit()

def main():
    """
    Main function.
    """

    data = {"message": "This is a test message."}

    push_data_to_postgres(data)

if __name__ == "__main__":
    main()
