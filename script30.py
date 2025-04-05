'''
import csv
#step1
col=['ENO','ENAME','SAL']
record=[[100,'blake',10000],
       [101,'scott',15000]]
with open  ("C:\\Users\\Pitabash\\Documents\\PYTHON_SCRIPTS\\level_004\\employee.csv",'w') as fp:
 table=csv.writer(fp)
 table.writerow(col)
 table.writerows(record)
 print('employee.csv table created--check')
'''
'''
import csv
rec=[500,'adams',20000]
with open("C:\\Users\\Pitabash\\Documents\\PYTHON_SCRIPTS\\level_004\\employee.csv",'a') as fp:
 table=csv.writer(fp)
 table.writerow(rec)
 print('1 record incerted--check')
'''
import csv
