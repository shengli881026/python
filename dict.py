# -*- coding: cp936 -*-
l_dict ={'1':10,'2':15,'3':25,'4':30,'5':35};

start = 10;
end   = 30;

# ��10-30 ѭ��,Ȼ��ѭ���ֵ��е�����,ƴдsql;
i = start;
j =0
while(i <= end):
    print i;
    for index in l_dict:
        #index = str(index);
        #print str(l_dict[index]);
        #print '>>>>>----------------'+l_dict[index];
        print '-------inset into test("id","value") values(\''+index+'\',\''+str(l_dict[index])+'\')';
        j+=1;
    i +=1;

print 'count --- insert '+str(j);

#for fruit in l_dict:
   # print l_dict[fruit];

for index in l_dict:
    print '>>>---'+index;
    print l_dict[index];

for letter in 'python':
    if letter == 'o':
        #break;
        #continue;
        pass;
        print 'o ----pass';
    print '>>>>Current Letter :',letter;

print 'end';


# ���ݼ�����ַ����ĳ��Ƚ���ѭ��
abc ='ssssssss';

for ind in abc:
    print ind;
    #print '**********'+str(n);
#print len(abc);
#print
