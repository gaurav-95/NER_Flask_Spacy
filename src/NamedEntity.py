import spacy

class NamedEntityService(object):
    
    @classmethod
    def get_entities(cls, input):
        
        clf = spacy.load("en_core_web_trf")
        return dict([(str(x), x.label_) for x in clf(input).ents])