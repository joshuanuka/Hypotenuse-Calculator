name=input('What is your name?')
print('Hello',name+'!')


print('I will compute the hypotenuse of a right triangle.\nBut first, you must tell me the lengths of the legs.')
leg1=input('What is the length of the first leg?')
leg2=input('What is the length of the second leg?')
hypo=(int(leg1)**2+int(leg2)**2)**0.5
print('The length of the hypotenuse is',str(hypo)+'.')
