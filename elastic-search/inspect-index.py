import json
from elasticsearch import Elasticsearch

es_client = Elasticsearch(HOST="http://localhost",PORT=9200)
print(
  json.dumps(
    es_client.indices.get_mapping(index="sl_politicians"), 
    indent=1)
)
