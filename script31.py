
import csv
col=['BOOK','PRICE']
rec=[{'BOOK':'python','PRICE':500},
     {'BOOK':'JAVA','PRICE':600}]
with open("C:\\Users\\Pitabash\\Documents\\PYTHON_SCRIPTS\\level_004\\book.csv",'w') as fp:
 table=csv.DictWriter(fp,fieldnames=col) #book.csv file created,it is empty
 table.writeheader() #column name inserted
 table.writerows(rec)#records inserted
 print('book.csv file created--check')
 
