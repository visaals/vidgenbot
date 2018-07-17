import ImageFinder
import TextSummarizer
import WikiSummaryRetriever

def main():
    print("Starting vidgenbot.py...")
    wiki_summary_retriever = new WikiSummaryRetriever();
    text_summarizer = new TextSummarizer();
    image_finder = new ImageFinder();

    summary_text = wiki_summary_retriever.retrieve_page_summary("Dog")
    sentences = text_summarizer.summarize_text(summary_text)
    images = image_finder.retrieve_sentence_image_pairs(sentences)
    print(images)

    print("vidgenbot.py has finished running.")

main()
