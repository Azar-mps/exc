wieght=int( input(' your weight in kg? '))
high=float(input(' your high in M? '))
BMI = (wieght / high ** 2)
if BMI < 18.5:
    print('under wight')
elif BMI > 25:
    print ('over wieght')
else:
    print('awliiiiiiii')
###############################################
s1=[4, 5,6,7]
s2 = [1,2,3,8]
s1[0:2] = s2[2:5]
s2[0:2]=s1[2:5]
print(s1)
print(s2)
