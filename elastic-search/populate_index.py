from management import EsManagement
import os

es_connection = EsManagement()
es_connection.populate_index(index_name="sl_politicians", 
                             path=os.path.join("corpus", "si"))
                             