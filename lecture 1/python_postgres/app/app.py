import os
import sys
import time
import psycopg2
import logging
import psycopg2.extras

# ENV variables
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'dev')
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_PORT = os.getenv('DB_PORT', '5432')

# Define logging LEVEL, output type
logging.basicConfig(level=logging.INFO,format='[%(asctime)s] [%(levelname)s] %(message)s')

def connect():
  return psycopg2.connect(host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD, port=DB_PORT, dbname=DB_NAME)


def select(conn, sql):
  with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    records = []
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        records.append(row)
    cur.close()
    return records

def close(conn):
  conn.close()

def main():
  while(True):
    logging.info("Start with DB")

    connection = connect()
    logging.info("Got connection {}".format(connection))
    
    record = select(connection, "SELECT 5;")
    logging.info("Selected record {}".format(record))

    close(connection)
    time.sleep(15)


if __name__ == "__main__":
  main()