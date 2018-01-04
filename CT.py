import csv
import time 
file=open(r'writecsv.csv',mode='a', encoding='gb18030')
string_temp="seriesuid coordX coordY coordZ diameter_mm"
file.write(string_temp) 
# tup={"seriesuid","coordX","coordY","coordZ","diameter_mm"}
# csv.DictWriter(file,tup)
# for key in tup:
#  file.write(tup[key])

file.close() 
print("job done!")