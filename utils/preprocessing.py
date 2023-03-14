def get_stopword(file):
    with open(file,'r',encoding='utf8') as f:
        lines = f.readlines()
        extended_lsw = list(map(lambda line:line.strip('\n'),lines))
    return extended_lsw

def preprocessing(doc,lsw,annotator):
    output = annotator.annotate_text(doc)
    result = []
    for item in output.values():
        result.extend(item)
    tokenized_doc = [item['wordForm'] for item in result if (item['posTag'].startswith("N") or item['posTag'].startswith("V") or item['posTag'].startswith("A")) and '.' not in item['wordForm']]
    for item in lsw:
        tokenized_doc = list(filter((item).__ne__, tokenized_doc))
    return tokenized_doc