import numpy as np
import torch
from dataclasses import dataclass
from typing import List
import csv
from jiant.tasks.core import (
    BaseExample,
    BaseTokenizedExample,
    BaseDataRow,
    BatchMixin,
    Task,
    TaskTypes,
)
from jiant.tasks.lib.templates.shared import single_sentence_featurize, labels_to_bimap


@dataclass
class Example(BaseExample):
    guid: str
    statement: str
    label: str

    def tokenize(self, tokenizer):
        return TokenizedExample(
            guid=self.guid,
            statement=tokenizer.tokenize(self.statement),
            label_id=ClaimBusterTask.LABEL_TO_ID[self.label],
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
    statement: List
    label_id: int

    def featurize(self, tokenizer, feat_spec):
        return single_sentence_featurize(
            guid=self.guid,
            input_tokens=self.statement,
            label_id=self.label_id,
            tokenizer=tokenizer,
            feat_spec=feat_spec,
            data_row_class=DataRow,
        )


class ClaimBusterTask(Task):
    Example = Example
    TokenizedExample = Example
    DataRow = DataRow
    Batch = Batch
    TASK_TYPE = TaskTypes.CLASSIFICATION
    LABELS = ['NFS', 'UFS', 'CFS']
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
            csv_reader = csv.reader(csv_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL,
                                    skipinitialspace=True)
            next(csv_reader)
            for i, row in enumerate(csv_reader):
                label = int(row[9]) + 1
                if label == 0:
                    label = 'NFS'
                elif label == 1:
                    label = 'UFS'
                else:
                    label = 'CFS'
                statement = row[1]
                examples.append(
                    Example(
                        guid="%s-%s" % (set_type, i),
                        statement=statement,
                        label=label,
                    )
                )
        return examples
