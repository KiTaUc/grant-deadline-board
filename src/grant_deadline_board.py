import argparse,json
from datetime import date
from pathlib import Path

def run(applications,today,days=7):
 now=date.fromisoformat(today); return sorted([item for item in applications if not item['done'] and 0 <= (date.fromisoformat(item['due_on'])-now).days <= days],key=lambda item:item['due_on'])

def main():
 parser=argparse.ArgumentParser(description='Локальный отраслевой инструмент')
 parser.add_argument('command')
 parser.add_argument('file',type=Path)
 parser.add_argument('--today',default='')
 parser.add_argument('--days',type=int,default=0)
 args=parser.parse_args()
 data=json.loads(args.file.read_text(encoding='utf-8'))
 print(json.dumps(run(data,args.today,args.days),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
