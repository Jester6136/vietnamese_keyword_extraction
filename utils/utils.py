def get_stopword(file):
    with open(file,'r',encoding='utf8') as f:
        lines = f.readlines()
        extended_lsw = list(map(lambda line:line.strip('\n'),lines))
    return extended_lsw

def preprocessing_vi(doc,lsw,annotator):
    output = annotator.annotate_text(doc)
    result = []
    for item in output.values():
        result.extend(item)
    tokenized_doc = [item['wordForm'] for item in result if (item['posTag'].startswith("N") or item['posTag'].startswith("V") or item['posTag'].startswith("A")) and '.' not in item['wordForm']]
    for item in lsw:
        tokenized_doc = list(filter((item).__ne__, tokenized_doc))
    return tokenized_doc

def preprocessing_en(doc,annotator):
    doc = annotator(doc)
    tokenized_doc = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            if token.pos_ == "NOUN" or token.pos_ == "ADJ":
                tokenized_doc.append(token.text)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            tokenized_doc.append(ent.text)
    return tokenized_doc

def postprocessing(keywords):
    copy_keywords = [word.lower() for word in keywords]
    duplicates = []
    for i, item in enumerate(copy_keywords):
        if item in copy_keywords[:i]:
            duplicates.append(i)
    keywords = [item for i, item in enumerate(keywords) if i not in duplicates]
    return keywords