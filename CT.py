import csv
import time 
file=open(r'writecsv.csv',mode='a', encoding='gb18030')
string_temp="你,好,啊,！\n"
file.write(string_temp) 
         
file.close() 
print("job done!")