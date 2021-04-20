import psycopg2
import boto3

# gets the credentials from .aws/credentials

session = boto3.Session(profile_name='twosteps_admin')
client = session.client('ssm')
ENDPOINT = client.get_parameter(Name='DB_ENDPOINT', WithDecryption=True)[
    'Parameter']['Value']
PORT = client.get_parameter(Name='DB_PORT', WithDecryption=True)[
    'Parameter']['Value']
USER = client.get_parameter(Name='DB_USER', WithDecryption=True)[
    'Parameter']['Value']
PASSWORD = client.get_parameter(Name='DB_PASSWORD', WithDecryption=True)[
    'Parameter']['Value']
REGION = client.get_parameter(Name='DB_REGION', WithDecryption=True)[
    'Parameter']['Value']
DBNAME = client.get_parameter(Name='DB_DBNAME', WithDecryption=True)[
    'Parameter']['Value']

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT,
                            database=DBNAME, user=USR, password=token)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
