from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

# Connect to Astra DB
ASTRA_DB_SECURE_CONNECT_BUNDLE = 'path_to_secure_connect_bundle.zip'
ASTRA_DB_USERNAME = 'your_username'
ASTRA_DB_PASSWORD = 'your_password'

auth_provider = PlainTextAuthProvider(ASTRA_DB_USERNAME, ASTRA_DB_PASSWORD)
cluster = Cluster(cloud={'secure_connect_bundle': ASTRA_DB_SECURE_CONNECT_BUNDLE}, auth_provider=auth_provider)
session = cluster.connect('translations')

def save_to_db(original_text, translations):
    blog_id = str(uuid.uuid4())
    query = "INSERT INTO user_blogs (blog_id, original_text, translations) VALUES (%s, %s, %s)"
    session.execute(query, (blog_id, original_text, str(translations)))
    return blog_id

def get_blog_metadata(blog_id):
    query = "SELECT * FROM user_blogs WHERE blog_id=%s"
    result = session.execute(query, (blog_id,))
    return result.one()
