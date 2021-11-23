from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(HOST="http://localhost",PORT=9200)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
        index="sl_politicians", 
        size=20, 
        body={
            "query": {
                "bool" : {
                    "should": [
                        {
                            "multi_match": {
                                "query": search_term,
                            }
                        },
                        {
                            "multi_match": {
                                "query": search_term,
                                "operator": "and"
                            }
                        },
                        {
                            "multi_match": {
                                "query": search_term,
                                "type": "phrase",
                                "boost": 2,
                            }   
                        }
                    ]
                }
            }
        }
    )
    return render_template('results.html', res=res )

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)