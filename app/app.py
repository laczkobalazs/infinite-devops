import psycopg2
import boto3

ENDPOINT = "postgresmydb.123456789012.us-east-1.rds.amazonaws.com"
PORT = "5432"
USR = "jane_doe"
REGION = "us-east-1"
DBNAME = "mydb"

# gets the credentials from .aws/credentials
session = boto3.Session(profile_name='twosteps_admin')
client = session.client('ssm')
ENDPOINT = client.get_parameter(Name='DB_ENDPOINT', WithDecryption=True)
PORT = client.get_parameter(Name='DB_PORT', WithDecryption=True)
USER = client.get_parameter(Name='DB_USER', WithDecryption=True)
PASSWORD = client.get_parameter(Name='DB_PASSWORD', WithDecryption=True)
REGION = client.get_parameter(Name='DB_REGION', WithDecryption=True)
DBNAME = client.get_parameter(Name='DB_DBNAME', WithDecryption=True)

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT,
                            database=DBNAME, user=USR, password=token)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
