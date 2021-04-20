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
                            database=DBNAME, user=USER, password=PASSWORD)
    cur = conn.cursor()
    cur.execute("""SELECT version()""")
    query_results = cur.fetchall()
    print(
        f"You are successfully connected to {query_results[0][0]} with user {query_results[0][1]}. The RDS version is {query_results[0][2]}")
except Exception as e:
    print(f"Database connection failed due to {e}")
