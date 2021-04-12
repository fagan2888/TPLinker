import json
import unittest

from preprocessor.truncator import BertExampleTruncator


class TruncatorTest(unittest.TestCase):

    def _read_examples(self, tokenizer, nums=1, min_sequence_length=100, **kwargs):
        examples = []
        with open('data/tplinker/bert/valid_data.jsonl', mode='rt', encoding='utf8') as fin:
            for line in fin:
                e = json.loads(line)
                tokens = tokenizer.tokenize(e['text'])
                if len(tokens) < min_sequence_length:
                    continue
                examples.append(e)
                if len(examples) == nums:
                    break
        return examples

    def test_bert_truncator(self):
        t = BertExampleTruncator('data/bert-base-cased', max_sequence_length=100)
        examples = self._read_examples(t.tokenizer, nums=1, min_sequence_length=100)
        truncated_examples = t.truncate(example=examples[0])
        print('original example: ', examples[0])
        for e in truncated_examples:
            print()
            print(e)


if __name__ == "__main__":
    unittest.main()