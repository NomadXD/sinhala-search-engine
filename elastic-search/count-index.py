from management import EsManagement

es_connection = EsManagement()

# Check the number of documents in your index
print(es_connection.es_client.count(index="sl_politicians"))
