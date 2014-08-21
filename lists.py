#!/usr/bin/python
# -*- coding: latin-1 -*-
list_1 = [1,2,3,4,'a','b','c','d'];

print '>>>>>'+str(list_1[6]);
print '>>>>>list_1 3:6'+str(list_1[3:6]);
# 中文
print list_1;
del list_1[2];
print list_1;   

# 列表合并+
abc_list = ['a','b','c','d','e','f','g','a','e','d'];
print list_1 + abc_list;
# cmp 返回值 0 lists 一致 1 不一致
lists_a,lists_b =['a','b','c','d','g'],['a','b','c','d'];
print cmp(lists_a,lists_b);


# lists 的常用的方法

lists_n = [1,2,3,4,6,10,38];
# 最大的值
print max(lists_n);
# 最小的值
print min(lists_n);
# 在列表末尾增加 abcd
abc_list.append('jwjwjwj');
print '>>>count:a='+str(abc_list.count('a'));


