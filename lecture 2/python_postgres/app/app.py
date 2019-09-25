import os
import sys
import time
import psycopg2
import logging

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
  with conn.cursor() as cur:
    records = []
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        records.append(row)
    cur.close()
    return records

def execute(conn, sql, params):
  try:
    with conn.cursor() as cur:
      cur.execute(sql, params)
      logging.info("Executed sql got state {} SQL: {}".format(cur.statusmessage, sql))
      conn.commit()
      cur.close()
  except psycopg2.DatabaseError as e:
    logging.error("Error creating table {}".format(e))

def close(conn):
  conn.close()

def main():
  connection = connect()
  logging.info("Got connection {}".format(connection))
  execute(connection, "CREATE TABLE IF NOT EXISTS test (id serial, number int);", [])
  close(connection)
  i = 0

  while(True):
    logging.info("Start with DB")

    connection = connect()
    logging.info("Got connection {}".format(connection))
    
    execute(connection, "INSERT INTO test(number) VALUES (%s);", [i,])
    records = select(connection, "SELECT * FROM test;")
    logging.info("Selected record {}".format(records))

    close(connection)
    i += 1
    time.sleep(15)


if __name__ == "__main__":
  main()