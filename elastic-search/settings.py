politician_settings = {
    "analysis": {
        "analyzer": {
            "indexing_analyzer": {
                "type": "custom",
                "char_filter": "character_filter",
                "tokenizer": "icu_tokenizer",
                "filter": [
                    "n_gram_tokenizer"
                ]
            },
            "search_analyzer": {
                "type": "custom",
                "char_filter": "character_filter",
                "tokenizer": "icu_tokenizer",
                "filter": [
                    "stop_words"
                ]
            }
        },
        "filter": {
            "n_gram_tokenizer": {
                "type": "edge_ngram",
                "min_gram": 2,
                "max_gram": 15
            },
            "stop_words": {
                "type": "stop",
                "stopwords": [
                    "හා",   
                    "හෝ",
                    "ද",
                    "සහ",
                    "ගීත",
                    "ගී",
                    "සින්දු"
                ]
            }
        },
        "char_filter": {
            "character_filter": {
                "type": "mapping",
                "mappings": [
                    "\u200d=>",
                    "\u200B=>",
                    ",=> ",
                    ".=> ",
                    "/=> ",
                    "|=> ",
                    "-=> ",
                    "'=> ",
                    "_=> ",
                    ":=> "

                ]
            }
        },
    }
}
