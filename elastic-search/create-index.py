import json

from management import EsManagement
from mappings import politician_mapping

es_connection = EsManagement()
es_connection.create_index(index_name="sl_politicians", mapping=politician_mapping)
