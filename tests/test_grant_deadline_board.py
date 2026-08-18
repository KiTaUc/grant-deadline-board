import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('x',Path(__file__).parents[1]/'src/grant_deadline_board.py');x=importlib.util.module_from_spec(s);s.loader.exec_module(x)
class T(unittest.TestCase):
 def test_domain_workflow(self):
  r=x.run([{'name':'A','due_on':'2026-08-20','done':False},{'name':'B','due_on':'2026-09-01','done':False}],'2026-08-18',7); self.assertTrue(len(r)==1 and r[0]['name']=='A')
if __name__=='__main__':unittest.main()
