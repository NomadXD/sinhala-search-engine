<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="assets/cover.png" alt="Logo" width="800" height="450">
  </a>

  <h3 align="center">CS4642 - Data Mining and Information Retrieval</h3>

  <p align="center">
   Text based search engine to search about politicians in Sri Lanka
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Basic overview](#Basic-overview)
* [Example demonstrations](#Example-demonstrations)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project

This project is done as a part of module CS4642 - Data Mining and Information Retrieval. The main goal of this project is to practise the information retrieval theories and concepts like term frequency, document frequency, tf-idf model, different types of search queries etc. For this project, Sri Lankan parliment website is scraped to extract details about parliment ministers to build a dataset. The dataset contains 225 records which comprises of the following details about parliment ministers.

1. Career
2. Civil Status
3. Committees
4. Date of birth
5. Electoral
6. Name
7. Occupation
8. Party
9. Portfolio
10. Religion


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* docker (for Elasticsearch)
* a python 3.7 environment with the required libraries installed

> Note: You can also run the setup by running elastic search installed locally with the required plugins (ICU tokenizer)

### Installation
 
1. Clone the repo 
```sh
git clone https://github.com/NomadXD/sinhala-search-engine.git
cd sinhala-search-engine
```
2. Build the elastic search docker image with ICU Analysis Plugin
```sh
cd elastic-search
docker build -t elastic-search-icu .
```
3. Start Elastic service docker container
```sh
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elastic-search-icu
```
4. Start the flask web application
```sh
python flask/app.py
```

### Creating the elastic search index and populating index.

> Note: Before trying this section, please start elastic search and flask web application by following installation instructions.

1. Create index by executing the following python command.
```sh
python elastic-search/create-index.py
```

2. Check whether the index is created successfully by executing the following command.
```sh
python elastic-search/inspect-index.py
```
It will show the index as follows if the index is successfully created.

```json
{
 "sl_politicians": {
  "mappings": {
   "properties": {
    "career": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "civil_status": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "committees": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "dob": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "electoral": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "name": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "occupation": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "party": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "portfolio": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    },
    "religion": {
     "type": "text",
     "analyzer": "indexing_analyzer",
     "search_analyzer": "search_analyzer"
    }
   }
  }
 }
}
```
3. Populate the index with politician data.

```sh
python elastic-search/populate_index.py
```

4. Check whether the data is correctly populated by executing the following command.

```sh
python elastic-search/count-index.py
```
If the index is correctly populated, it will show the below output.

```json
{'count': 225, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}}
```

5. Run the follow test query to verify everything is working correclty.

```sh
python elastic-search/query.py
```
6. Go to `http://localhost:5000/` and use the UI to search the politician information

## Basic overview





<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


[product-screenshot]: assets/cover.png