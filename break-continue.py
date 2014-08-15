#/usr/bin/python
# -*- coding: latin-1 -*-

#continue 语句测试

i=1;
while i<=100:
	i=i+1;
	if i%2 ==1:
		continue;
	print '>>>>>>'+str(i);

#break 语句

for index in 'abcdefghijklnm':
	if index =='c':
		break;
	print index;



# pass 语句,让结构更加完整

for index in [1,2,3,4,5]:
	if index ==3:
		pass;
		print '>>>pass'+str(index);
	print index;
