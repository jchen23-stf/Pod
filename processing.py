import sumy
import nltk
import csv
import json
import re
import os

from rouge_score import rouge_scorer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

def generate_summaries(location, task):
    original_text = open("test_transcript").read()

    parser = PlaintextParser.from_string(original_text,Tokenizer('english'))

    summarizers = [LexRankSummarizer(), LsaSummarizer(), LuhnSummarizer()]
    summaries = [x(parser.document, 20) for x in summarizers]

    # Printing the summary
    for i in range(len(summarizers)):
        with open(f"{location}\{task}_{i}.txt", "w") as f:
            for sentence in summaries[i]:
                f.write(str(sentence) + "\n")


if __name__ == "__main__":

    # nltk.download('punkt')

    #generate_summaries("summaries", "test")

    # scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

    # targets = ["lexrank_summary.txt", "lsa_summary.txt", "luhn_summary.txt"]
    # predictions = ["bert.txt", "gpt.txt"]

    # for prediction in predictions:
    #     for target in targets:
    #         scores = scorer.score(open(target).read(), open(prediction).read())
    #         print(f"{prediction} against {target}\n", scores)

    read_tsv = csv.reader(open("metadata.tsv"), delimiter="\t")

    print(read_tsv.__next__())

    for i in range(100):
        read_tsv.__next__()

    for i in range(1000):
        data = read_tsv.__next__()
        show = data[10]
        episode = data[11]
        filename = f"spotify-podcasts-2020/podcasts-transcripts/{show[5]}/{show[6]}/{show}/{episode}.json"
        print(filename)

        transcript = ""

        with open(filename, "r") as f:
            meow = json.load(f)
            for mew in meow['results']:
                if 'transcript' in mew['alternatives'][0]:
                    transcript += mew['alternatives'][0]['transcript']
            #transcript = re.sub("(?<=[?.!]) (?=[A-Z])", "\n", transcript)
        
        # new_filename = f"spotify-podcasts-2020-json/{show[5]}/{show[6]}/{show}/{episode}.json"

        # try:
        #     os.makedirs(f"spotify-podcasts-2020-json/{show[5]}/{show[6].upper()}/{show}")
        # except:
        #     pass

        #with open(new_filename, "w") as f:
        with open("spotify-data-1100-train.json", "a") as f:
            meow = {"document": transcript, "summary": data[8], "id": f"{data[10]}:{data[11]}"}
            mew = json.dumps(meow)
            f.write(mew)
            f.write('\n')
 
