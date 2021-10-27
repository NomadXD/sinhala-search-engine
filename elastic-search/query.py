from management import EsManagement

es_connection = EsManagement()

# Querying data
# Query and filter contexts
query = {
    "query": {
        "multi_match": {
            "query": "ගරු. අංගජන් රාමනාදන්, පා.ම."
        }
    }
}

results = es_connection.es_client.search(index="sl_politicians", body=query)

print(results)
# Result
#print([i["_source"]["title"] for i in results["hits"]["hits"]])
