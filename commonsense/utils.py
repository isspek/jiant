import pandas as pd
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
from textblob import TextBlob
import pandas as pd
import conceptnet_lite
from conceptnet_lite import Label, edges_for
from cleantext import clean
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import ngrams
import re
import itertools
import json
from tqdm import tqdm
from pathlib import Path
from argparse import ArgumentParser
import jiant.scripts.download_data.runscript as downloader


def clean_news(text):
    return clean(text,
                 fix_unicode=True,  # fix various unicode errors
                 to_ascii=True,  # transliterate to closest ASCII representation
                 no_urls=True,  # replace all URLs with a special token
                 no_emails=True,
                 lower=True,
                 no_phone_numbers=True,
                 no_numbers=True,  # replace all numbers with a special token
                 no_digits=True,  # replace all digits with a special token
                 no_currency_symbols=True,
                 replace_with_url="$URL$",
                 replace_with_email="$EMAIL$",
                 replace_with_phone_number="$PHONE$",
                 replace_with_number="$NUMBER$",
                 replace_with_digit="$DIGIT$",
                 replace_with_currency_symbol="$CUR$",
                 lang="en")


class ConceptNet:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = list(set(stopwords.words('english')))
        self.excluded_tags = ['$url$', '$email$', '$phone$', '$number$', '$digit$', '$cur$']
        # TODO make it parametric
        self.KB = conceptnet_lite.connect('../datasets/conceptnet.db', db_download_url=None)

    def _pos_tags(self, news):
        _sentences = sent_tokenize(news)
        sentences = []
        for sentence in _sentences:
            words = word_tokenize(sentence)
            sentence = [word for word in words if word.isalpha()]
            pos_tags = pos_tag(sentence)
            sentences.append(pos_tags)
        return sentences

    def _conceptnet_entity(self, mention):
        Label.get(text=mention).concepts

    def extract_mentions(self, news):
        news = news.lower()
        for i in self.excluded_tags:
            news = news.replace(i, '')
        pos_tags = self._pos_tags(news)
        mentions = []
        for sent in pos_tags:
            chunks = ne_chunk(sent, binary=True)
            try:
                for (mention, pos_tag) in chunks:
                    if mention in self.excluded_tags:
                        continue
                    if mention in self.stop_words:
                        continue
                    mention = self.lemmatizer.lemmatize(mention, 'v')
                    mentions.append(mention)
            except:
                print(f'Error is occured at {mention}')
                continue
        return mentions

    def entity_linker(self, mentions):
        '''
        For each concept extract 1-hop related concept
        :param concepts:
        :return:
        '''
        entities = []
        for mention in mentions:
            try:
                Label.get(text=mention)
                entities.append(mention)
            except:
                # logger.error(f'{mention} is not a conceptnet entity')
                continue
        return entities

    def extract_commonsense_knowledge_facts(self, entities):
        '''
        For each concept extract related concepts (1-hop)
        :param concepts:
        :return:
        '''
        entity_context = {}
        all_facts = []
        for entity in entities:
            print(f'Query {entity}')
            if entity in entity_context:
                continue

            facts = []
            try:
                concepts = Label.get(text=entity, language='en').concepts

                for edge in edges_for(concepts, same_language=True):
                    entity_1 = edge.start.text
                    entity_2 = edge.end.text
                    relation = edge.relation.name
                    fact = f"{entity_1} {relation} {entity_2}"
                    if fact not in facts:
                        facts.append(fact)
                    print(fact)
            except:
                continue

            entity_context[entity] = facts
        return entity_context


def pipeline_concept_extraction(data_dir, conceptnetkb):
    data_dir = Path(data_dir)
    documents = []
    concept_dir = data_dir / 'concepts'
    Path(concept_dir).mkdir(parents=True, exist_ok=True)

    merged_data = []
    for data_path in data_dir.glob('*.tsv'):
        print(f'Reading {data_path}')
        data = pd.read_csv(data_path, sep='\t')
        merged_data.append(data)

    merged_data = pd.concat(merged_data)
    merged_data.drop_duplicates(inplace=True)

    samples = merged_data['content'].tolist()
    titles = merged_data['title'].tolist()
    for idx, raw_sample in enumerate(tqdm(samples)):
        sample = clean_news(raw_sample)
        mentions = conceptnetkb.extract_mentions(sample)
        entities = conceptnetkb.entity_linker(mentions)
        # extract only unique entities
        entities = list(set(entities))

        documents.append({
            'title': titles[idx],
            'content': raw_sample,
            'concept_entities': entities}
        )

    resulted_file = concept_dir / 'commonsense_concepts.json'
    with open(resulted_file, 'w') as outfile:
        json.dump(documents, outfile)
    print(f'Entities are saved {resulted_file}.')


def pipeline_concept_extraction_commonsense(data_dir, conceptnetkb):
    data_dir = Path(data_dir)
    concept_dir = data_dir / 'concepts'
    Path(concept_dir).mkdir(parents=True, exist_ok=True)

    downloader.download_data(['commonsenseqa'], data_dir)
    data_dir = data_dir / 'data' / 'commonsenseqa'

    test_file = data_dir / 'test.jsonl'
    print('Processing test data')
    resulted_file = concept_dir / 'test_commonsense_concepts.json'
    extract_and_write_concepts_from_jsonl(conceptnetkb, test_file, resulted_file)

    val_file = data_dir / 'val.jsonl'
    print('Processing val data')
    resulted_file = concept_dir / 'val_commonsense_concepts.json'
    extract_and_write_concepts_from_jsonl(conceptnetkb, val_file, resulted_file)

    train_file = data_dir / 'train.jsonl'
    print('Processing train data')
    resulted_file = concept_dir / 'train_commonsense_concepts.json'
    extract_and_write_concepts_from_jsonl(conceptnetkb, train_file, resulted_file)


def extract_and_write_concepts_from_jsonl(conceptnetkb, test_file, resulted_file):
    with open(test_file, 'r') as json_file:
        json_list = list(json_file)
    documents = []
    for json_str in json_list:
        q_entities = extract_entities_from_json(conceptnetkb, json_str)
        documents.append(
            {
                'concept_entities': q_entities
            }

        )
    with open(resulted_file, 'w') as outfile:
        json.dump(documents, outfile)
    print(f'Entities are saved {resulted_file}.')


def extract_entities_from_json(conceptnetkb, json_str):
    result = json.loads(json_str)
    question = result['question']
    mentions = conceptnetkb.extract_mentions(question)
    q_entities = conceptnetkb.entity_linker(mentions)
    q_entities = list(set(q_entities))
    text = result['choices']['text']
    t_entities = conceptnetkb.entity_linker(text)
    t_entities = list(set(t_entities))
    q_entities.extend(t_entities)
    q_entities = list(set(q_entities))
    return q_entities


def pipeline_concept_matching(source_data_path, target_data_path):
    pass


EXT_PIPELINES = {
    'commonsenseqa': pipeline_concept_extraction_commonsense,
    'news': pipeline_concept_extraction
}

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--source_dir', type=str)
    parser.add_argument('--extract', action='store_true')
    parser.add_argument('--dtype', choices=['commonsenseqa', 'news'])
    parser.add_argument('--match', action='store_true')
    args = parser.parse_args()

    if args.extract:
        conceptnetkb = ConceptNet()
        EXT_PIPELINES[args.dtype](args.source_dir, conceptnetkb)

    if args.match:
        pass
