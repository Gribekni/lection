filename = '/home/roman/Downloads/Doner_Loren_Furi_(LP)_Litmir.net_bid224439_2a09f.txt'
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(filename, 'r', encoding='cp1251') as f:
        content = f.read()

import nltk
nltk.download('punkt')
tokens = nltk.word_tokenize(content, language='russian')

import spacy
try:
    nlp = spacy.load('ru_core_news_sm')
except OSError:
    from spacy.cli import download
    download('ru_core_news_sm')
    nlp = spacy.load('ru_core_news_sm')
doc = nlp(' '.join(tokens))
lemmas = [token.lemma_ for token in doc]

from collections import Counter
lemma_counts = Counter(lemmas)
sorted_lemmas = lemma_counts.most_common()
all_lemmas_str = ', '.join([f"{lemma}:{count}" for lemma, count in sorted_lemmas])
print(all_lemmas_str)

nouns = [token.lemma_ for token in doc if token.pos_ == 'NOUN']
adjs = [token.lemma_ for token in doc if token.pos_ == 'ADJ']
verbs = [token.lemma_ for token in doc if token.pos_ == 'VERB']
most_common_noun = Counter(nouns).most_common(1)
most_common_adj = Counter(adjs).most_common(1)
most_common_verb = Counter(verbs).most_common(1)
print('Самое частое существительное:', most_common_noun)
print('Самое частое прилагательное:', most_common_adj)
print('Самый частый глагол:', most_common_verb)

lemma_counts = Counter(lemmas) 
unique_lemmas = len(lemma_counts)
total_lemmas = sum(lemma_counts.values())
lex_diversity = unique_lemmas / total_lemmas if total_lemmas else 0
print(f'Лексическое разнообразие: {lex_diversity:.4f}')

