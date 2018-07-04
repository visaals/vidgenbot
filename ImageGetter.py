import spacy
import webbrowser as wb
import requests
from lxml import html
import os
nlp = spacy.load('en')
sents_and_images = {}

def imageFinder(sent):
    for sentence in sent:
        doc=nlp(unicode(sentence))
        terms = []
        for token in doc:
            if token.dep_ == 'nsubj' or token.pos_ == 'NOUN':
                terms.append(token.lemma_)
        [terms.remove(word) for word in terms if not word.isalpha()]
        search = "https://www.pexels.com/search/" + ',%20'.join(terms) + "/"
        page = requests.get(search)
        tree = html.fromstring(page.content)
        image = tree.xpath('//article/a/@href')
        if not image:
            image.append('')
        if 'https://' not in image[0]:
            sents_and_images[sentence] = image[1]
        else:
            sents_and_images[sentence] = image[0]