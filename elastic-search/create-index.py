from management import EsManagement
from mappings import politician_mapping
from settings import politician_settings

es_connection = EsManagement()
es_connection.create_index(index_name="sl_politicians", mapping=politician_mapping, settings=politician_settings)
