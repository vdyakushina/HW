# -*- coding: utf-8 -*-
def PtoSreads(inpt,outpt):
 import csv
 with open(inpt) as inpf:
   reader = csv.reader(inpf, delimiter='\t')
   names=[]
   for elem in reader:
     if elem not in names:
       names.append(elem[0])
 res=[]
 for n in names:
   with open(inpt) as inpf:
      reader2 = csv.reader(inpf, delimiter='\t')
      read=[]
      nl=[]
      strt=[]
      end=[]
      for line in reader2:
        if n in line:
          nl.append(line[9])
          strt.append(line[3])
          end.append(line[4])
          read.append(line)
      second=strt.index(max(strt[0],strt[1]))
      nl2=str()
      for i in range(2):
        if i == second:
          nl2=str(nl[i])[int(strt[i-1])+int(abs(int(end[i-1])))-int(strt[i]):]
          nnl=nl[i-1]+nl2
          read[i-1][9]=nnl
          res.append("\t".join(read[i-1]))

 with open("outpt", "w") as out_f:
   out_f.write("\n".join(res))
