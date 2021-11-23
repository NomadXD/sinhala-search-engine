from typing import Dict
from elasticsearch import Elasticsearch
import logging
import json
import glob

logging.basicConfig(filename="es.log", level=logging.DEBUG)

class EsManagement:
    def __init__(self) -> None:
        self.es_client = Elasticsearch(HOST="http://localhost",PORT=9200)
        logging.info(self.es_client.ping())

    def create_index(self, index_name: str, mapping: Dict, settings) -> None:
        """
        Create an ES index.
        :param index_name: Name of the index.
        :param mapping: Mapping of the index
        """
        logging.info(f"Creating index {index_name} with the following schema: {json.dumps(mapping, indent=2)}")
        self.es_client.indices.create(index=index_name, ignore=400, mappings=mapping, settings=settings)

    def populate_index(self, path: str, index_name: str) -> None:
        files = glob.glob(path+"/*")
        for file in files:
            data = open(file, "r")
            try:
                politician = json.load(data)
                self.es_client.index(index=index_name, body=json.dumps(politician))
            except:
                print(file)