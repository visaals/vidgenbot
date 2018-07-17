import spacy
import webbrowser as wb
import requests
from lxml import html
import os

"""
Given a list of sentences, this class will pair a relevant image to each sentence.
"""
class ImageFinder:

    def __init__(self):
        self.nlp = spacy.load('en')
        self.sents_and_images = {}

    def retrieve_sentence_image_pairs(sentence_list):
        for sentence in sentence_list:
            # tags words of sentences with part of speech
            doc=self.nlp(unicode(sentence))
            terms = []
            for token in doc:
                if token.dep_ == 'nsubj' or token.pos_ == 'NOUN':
                    terms.append(token.lemma_)
            [terms.remove(word) for word in terms if not word.isalpha()]
            # search keywords on pexels.com
            search = "https://www.pexels.com/search/" + ',%20'.join(terms) + "/"
            page = requests.get(search)
            tree = html.fromstring(page.content)
            image = tree.xpath('//article/a/@href')
            # append image to list
            if not image:
                image.append('')
            if 'https://' not in image[0]:
                self.sents_and_images[sentence] = image[1]
            else:
                self.sents_and_images[sentence] = image[0]

        return self.sents_and_images
