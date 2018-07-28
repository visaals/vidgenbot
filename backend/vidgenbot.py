import backend.WikiSummaryRetriever as WikiSummaryRetriever
import backend.ImageFinder as ImageFinder

def main():
    print("Starting vidgenbot.py...")
    print(ImageFinder)
    wiki_summary_retriever = WikiSummaryRetriever.SentenceRanker();
    image_finder = ImageFinder.ImageFinder();

    summary_text = wiki_summary_retriever.retrieve_page_summary("Science")
    sentences = wiki_summary_retriever.summarize_text(summary_text)
    images = image_finder.retrieve_sentence_image_pairs(sentences)
    print(images)

    print("vidgenbot.py has finished running.")



