import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source_families import group_sources
class SourceTests(unittest.TestCase):
 def test_reprints_not_independent(self):self.assertEqual(len(group_sources([{'id':str(i),'root':'回忆录A'} for i in range(10)])),1)
 def test_two_declared_roots(self):self.assertEqual(len(group_sources([{'id':'a','root':'聘书'},{'id':'b','root':'回忆录'}])),2)
 def test_unknown(self):
  with self.assertRaises(ValueError):group_sources([{'id':'a'}])
 def test_duplicate(self):
  with self.assertRaises(ValueError):group_sources([{'id':'a','root':'x'},{'id':'a','root':'y'}])
