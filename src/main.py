from utils.utils import get_stopword,preprocessing_vi,preprocessing_en,postprocessing
import math
import py_vncorenlp
from configparser import ConfigParser
import spacy
import logging

class Extractor():
    def __init__(self,config,lang):
        self.lang=lang
        if self.lang =='vi':
            self.stopwords = get_stopword(config['stopwords_path'])
            self.annotator = py_vncorenlp.VnCoreNLP(annotators=["pos"], save_dir=config['vncore_path'])
        elif self.lang =='en':
            self.annotator = spacy.load("en_core_web_sm")
        else:
            logging.exception("This language don't supporting now!")

    def run(self,document,num_keywords):
        if self.lang=='vi':
            tokens = preprocessing_vi(document,self.stopwords,self.annotator)
        elif self.lang=='en':
            tokens = preprocessing_en(document, self.annotator)    
        # Calculate the position weights of the filtered words using a combination of linear and logarithmic scales
        max_position = len(tokens)
        if max_position <= 1:
            return document
        position_weights = [ i / max_position + (1 - math.log(i + 1) / math.log(max_position)) for i, word in enumerate(tokens)]

        tf = {}

        for i,token in enumerate(tokens):
            if token[0].isupper():
                weight = 2  # Assign a weight of 2 to uppercase tokens
            else:
                weight = 1  # Assign a weight of 1 to lowercase tokens
                if "_" not in token:
                    weight-=0.5
            if "_" in token:
                weight +=0.8
            tf[token] = tf.get(token, 0) + weight * position_weights[i]

        # for i,token in enumerate(tokens):
        #     if token[0].isupper():
        #         weight = 2  # Assign a weight of 2 to uppercase tokens
        #     elif "_" in token:
        #         weight +=1
        #     else:
        #         weight = 1  # Assign a weight of 1 to lowercase tokens
        #     tf[token] = tf.get(token, 0) + weight * position_weights[i]

        # Get top keywords
        sorter = sorted(tf.items(), key=lambda x:x[1], reverse=True)
        # print(sorter)
        top_keywords = postprocessing(list(dict(sorter).keys()))[:num_keywords]
        keywords_resortby_index = sorted(top_keywords, key=lambda x: list(tf.keys()).index(x))
        if self.lang =='vi':
            keywords_resortby_index = list(map(lambda keyword:keyword.replace('_',' '),keywords_resortby_index))
        copy_keywords = [ item.lower() for item in keywords_resortby_index.copy()]
        
        remove_count = 0
        for i,item in enumerate(copy_keywords):
            for other_item in copy_keywords:
                if item != other_item and item in other_item and len(item) < len(other_item):
                    del keywords_resortby_index[i - remove_count]
                    remove_count+=1
        return keywords_resortby_index