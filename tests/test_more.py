from pathlib import Path
import json
import unittest
from tools import more

class MoreExercises(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        catalog=json.loads((Path(__file__).resolve().parents[1]/'curriculum.json').read_text(encoding='utf-8'))
        self.assertEqual(len(catalog),47)
        self.assertEqual(len({item['function'] for item in catalog}),47)
        for item in catalog:
            self.assertGreaterEqual(len(item['cases']),2)
            for case in item['cases']:
                with self.subTest(exercise=item['id'],arguments=case[0]):
                    actual=getattr(more,item['function'])(*case[0])
                    self.assertEqual(json.loads(json.dumps(actual)),case[1])

if __name__=='__main__': unittest.main()
