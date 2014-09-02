#/usr/bin/python
# -*- coding: latin-1 -*-
#声明编码格式
#for string 
i=0;
for index in 'abcdefg':
	#print index;
	print i;
	i =i+1;

fr = {'a':1,'b':2,'c':3};

for index in fr:
	print '>>>>>>>key:'+index;
	print '******value:'+str(fr[index]);


fruits =['abc','def','hig','mnw'];

#range 返回序列的数据, len 获取列表 或者元组的长度
#print len(fr);
for index in range(len(fruits)):
	print fruits[index];


#for 嵌套循环

for index in 'abcdefg':
	for j in 'abcdefg':
		if j =='c':
			continue;
		print '>>>>for to -->'+str(j);
	print '>>>>for ---'+str(index);
