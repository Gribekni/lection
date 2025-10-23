import spacy
from collections import Counter

try:
    nlp = spacy.load('ru_core_news_sm')
except OSError:
    from spacy.cli import download
    download('ru_core_news_sm')
    nlp = spacy.load('ru_core_news_sm')

with open('/home/roman/Downloads/Doner_Loren_Furi_(LP)_Litmir.net_bid224439_2a09f.txt', 'r', encoding='cp1251') as file:
    content = file.read()
    
#решил разобраться, как работает токенизация + лемматизация только через spacy. Выводит леммы без стоп-слов + количество каждой.
#также выводит изменение длины текста без них, а также самое частое слово, являющееся корнем предложения.

doc = nlp(content)

total_tokens = 0
lemmas = []
for token in doc:
    if token.is_alpha:
        total_tokens += 1
        if not token.is_stop:
            lemma = token.lemma_.lower()
            lemmas.append(lemma)

lemma_counts = Counter(lemmas)
sorted_lemmas = lemma_counts.most_common()

all_lemmas_str = ', '.join([f'"{lemma}": {count}' for lemma, count in sorted_lemmas])
print(all_lemmas_str)

filtered_tokens = len(lemmas)
reduction = filtered_tokens / total_tokens * 100

print(f"Всего токенов: {total_tokens}")
print(f"Осталось: {filtered_tokens}")
print(f"Сокращение текста на {reduction:.2f}%")

#Корни предложений

root_counter = Counter()
for sent in doc.sents:
    root = sent.root
    if root.is_alpha:
        root_counter[root.lemma_.lower()] += 1
        
most_common_root, count = root_counter.most_common(1)[0]
print(f"\nЧаще всего в качестве корня предложения используется слово \"{most_common_root}\" ({count} раз)")