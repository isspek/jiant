import numpy as np
import pandas as pd
import torch
from dataclasses import dataclass
from typing import List
from cleantext import clean
import re
import csv
from jiant.tasks.core import (
    BaseExample,
    BaseTokenizedExample,
    BaseDataRow,
    BatchMixin,
    Task,
    TaskTypes,
)
from jiant.tasks.lib.templates.shared import double_sentence_featurize, labels_to_bimap


def clean_text(text):
    if type(text) == float:
        return ""
    text = re.sub(r'\([^)]*\)', '', text)
    cleaned_text = clean(text,
                         fix_unicode=True,  # fix various unicode errors
                         to_ascii=True,  # transliterate to closest ASCII representation
                         lower=True,  # lowercase text
                         no_line_breaks=True,  # fully strip line breaks as opposed to only normalizing them
                         no_urls=True,  # replace all URLs with a special token
                         no_emails=True,  # replace all email addresses with a special token
                         no_phone_numbers=True,  # replace all phone numbers with a special token
                         no_numbers=True,  # replace all numbers with a special token
                         no_digits=True,  # replace all digits with a special token
                         no_currency_symbols=True,  # replace all currency symbols with a special token
                         no_punct=False,  # fully remove punctuation
                         replace_with_url='<url>',
                         replace_with_email='<email>',
                         replace_with_phone_number='<phone>',
                         replace_with_number="<number>",
                         replace_with_digit="0",
                         replace_with_currency_symbol="<cur>",
                         lang="en"  # set to 'de' for German special handling
                         )
    cleaned_text = cleaned_text.strip()
    return cleaned_text


@dataclass
class Example(BaseExample):
    guid: str
    title: str
    content: str
    label: str

    def tokenize(self, tokenizer):
        return TokenizedExample(
            guid=self.guid,
            title=tokenizer.tokenize(self.title),
            content=tokenizer.tokenize(self.content),
            label_id=ForecastingTask.LABEL_TO_ID[self.label],
        )


@dataclass
class DataRow(BaseDataRow):
    guid: str
    input_ids: np.ndarray
    input_mask: np.ndarray
    segment_ids: np.ndarray
    label_id: int
    tokens: list


@dataclass
class Batch(BatchMixin):
    input_ids: torch.LongTensor
    input_mask: torch.LongTensor
    segment_ids: torch.LongTensor
    label_id: torch.LongTensor
    tokens: list


@dataclass
class TokenizedExample(BaseTokenizedExample):
    guid: str
    title: List
    content: List
    label_id: int

    def featurize(self, tokenizer, feat_spec):
        return double_sentence_featurize(
            guid=self.guid,
            input_tokens_a=self.title,
            input_tokens_b=self.content,
            label_id=self.label_id,
            tokenizer=tokenizer,
            feat_spec=feat_spec,
            data_row_class=DataRow,
        )


class ForecastingTask(Task):
    Example = Example
    TokenizedExample = Example
    DataRow = DataRow
    Batch = Batch
    TASK_TYPE = TaskTypes.CLASSIFICATION
    LABELS = ['right', 'satire', 'propaganda', 'conspiracy', 'neutral', 'left']
    LABEL_TO_ID, ID_TO_LABEL = labels_to_bimap(LABELS)

    def get_train_examples(self):
        return self._create_examples(path=self.train_path, set_type="train")

    def get_val_examples(self):
        return self._create_examples(path=self.val_path, set_type="val")

    def get_test_examples(self):
        return self._create_examples(path=self.test_path, set_type="test")

    @classmethod
    def _create_examples(cls, path, set_type):
        examples = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, quotechar='"', delimiter='\t', quoting=csv.QUOTE_ALL,
                                    skipinitialspace=True)
            next(csv_reader)
            for i, row in enumerate(csv_reader):
                url, title, content, label = row
                content = clean_text(content)
                title = clean_text(title)
                examples.append(
                    Example(
                        guid="%s-%s" % (set_type, i),
                        title=title,
                        content=content,
                        label=label if set_type != "test" else cls.LABELS[-1],
                    )
                )
        return examples
