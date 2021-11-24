from sinling import SinhalaTokenizer
from sinling import word_splitter

# Boost fields names
pmKeywords = ["මන්ත්‍රීවරයා", "මන්ත්‍රීවරයා", "මැතිතුමා", "මැති", "ගරු", "පා.ම."]
locationKeywords = ["ප්‍රදේශයේ", "දිස්ත්‍රික්කයේ", "දිස්ත්‍රික්කය", "ප්‍රදේශය"]
committeeKeywords = ["කමිටුව" "කමිටුවේ"]
partyKeywords = ["පක්ෂයේ", "පක්ෂය", "සන්ධානය", "සන්ධානයේ", "පෙරමුණ"]

tokenizer = SinhalaTokenizer()

class QueryProcessor:
    def __init__(self) -> None:
        print("Initializing Query Processor")

    def preprocessQuery(self, query):
        tokens = tokenizer.tokenize(query)
        return self.getBoostList(tokens)

    def getBoostList(self, tokens):
        field_priorities = {}
        for token in tokens:
            # splitted_words = word_splitter.split(token)

            # if (token in pmKeywords or splitted_words['affix'] in pmKeywords or splitted_words['base'] in pmKeywords):
            #     field_priorities['name'] = 2.0
            
            # if (token in locationKeywords or splitted_words['affix'] in locationKeywords or splitted_words['base'] in locationKeywords):
            #     field_priorities['electoral'] = 2.0

            # if (token in committeeKeywords or splitted_words['affix'] in committeeKeywords or splitted_words['base'] in committeeKeywords):
            #     field_priorities['committees'] = 2.0

            # if (token in partyKeywords or splitted_words['affix'] in partyKeywords or splitted_words['base'] in partyKeywords):
            #     field_priorities['party'] = 2.0
            if (token in pmKeywords):
                field_priorities['name'] = 2.0
            
            if (token in locationKeywords):
                field_priorities['electoral'] = 2.0

            if (token in committeeKeywords):
                field_priorities['committees'] = 2.0

            if (token in partyKeywords):
                field_priorities['party'] = 2.0

        boost_list = []
        if(field_priorities.keys()):
            for field in field_priorities.keys():
                boost_list.append("{0}^{1}".format(field, field_priorities[field]))
            print(boost_list)
        return boost_list
