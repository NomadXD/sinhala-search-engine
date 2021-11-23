from management import EsManagement

es_connection = EsManagement()

# Querying data
# Query and filter contexts
query = {
    "query": {
        "match": {
            "name" : {
                "query": "අංගජන් රාමනාදන්"
            }
        }
    }
}

results = es_connection.es_client.search(index="sl_politicians", body=query)

print(results)
