##1  Done

##2
 print(5**9)
 print(3//2)
 print(7//3)
 print(7/3)
 print(6==6)
 a=20
 a+=30
 a%=3
 print(a)
 print(True * False)
 print(True & False)
 print(True and False)
 print(((6>=3 and(7<=4) or (18==3)) and (9>3))
 print(True is False)
 print(((True == False) or (False > True)) and (False <=True))

 ##3

 s1 = 'Nice to have it'
 s2 = 'here'
 print(s1,s2)

 ##4

 a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
 print(a[3][1][2])

 ##5

 a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
 a[0] = 's1'
 a[-1] = 's2'
 print(a)

 ##6

 color_list_1 = set(["white","black","red"])
 color_list_2 = set(["red","green"])
 print(color_list_1 - color_list_2)

 ##7

 import string
 def ispangram (str)
     alphabet = 'abcdefghijklmnopqretuvwxyz'
     for char in alphabet:
         if char not in str.lower():
             return False
         return True

 string = 'live is good'
 if ispangram(string)== True:
     print('yes')
 else:
     print('NO')



 ##8

 n = input('enter any number')
 result = eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
 print(result)


 ##9


 p = input('Enter some comma separated sequence of words:)
 tuple = p.split(",")
 tuple.sort()
 print(p)
 print(tuple)

 ##10

 d = {'Student':['Rahul','Kishore','Vidhya','Rakhi'],'Marks':[57,87,67,79]}
 res = max(d['marks'])
 print(res)
 pos = d['Marks'].index(res)
 print(pos)
 print(d['Student'].index(pos))          
           
 
