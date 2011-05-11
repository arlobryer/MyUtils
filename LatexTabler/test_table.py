from LatexTabler import *
import json
test_json='./test_table.json'
j=open(test_json,'r')
tab=table()

tab.json_fill(j, 'some_table')

print tab.num_cols()

textab=texTable(tab)
textab.texout()
