import spacy

class NamedEntityService(object):
    
    @classmethod
    def get_entities(cls, input):
        
        nlp = spacy.load("en_core_web_trf")
        
        #Entities to exclude
        exclude = ["MONEY", "DATE"]

        #Get entities using nlp(input).ents
        res = [(str(x), x.label_) for x in nlp(input).ents if x.label_ not in exclude]

        return dict(res)