# wiki api
from mediawiki import MediaWiki
from gensim.summarization import summarize


class SentenceRanker:

    def __init__(self):
        self.wikipedia = MediaWiki()

    def retrieve_page_summary(self, page):
        p = self.wikipedia.page(page)
        return p.summary

    def summarize_text(self, text, word_count=600):
        return summarize(text, split=True, word_count=word_count)

    def get_top_sentences_from_page(self, pageName):
        print("Starting get_top_sentences_from_page...")

        # fetch summary from wiki page
        text = self.retrieve_page_summary(page=pageName)
        print("get_top_sentences_from_page finished.")

        # summarize summary
        return self.summarize_text(text)


# sentence_list = get_top_sentences_from_page("Dog")
# print(len(sentence_list))
# print(sentence_list)
