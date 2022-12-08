product_1 = int(input('quantity of first product:'))
product_2 = int(input('quantity of second product:'))
product_3 = int(input('quantity of third product:'))
# if((product_1<=0) or (product_2<=0) or (product_3<=0)):
#     print('please enter a positive value')
# else:
#     print('the amount that you need to pay is:')
#     total = product_1*300+product_2*400+product_3*500
#     print(total)

l = [product_1,product_2,product_3]
for i in l:
    #print(l)
    print(i)
if((product_1<=0) or (product_2<=0) or (product_3<=0)):
    print('please enter a positive value')
else:
    print('the amount that you need to pay is:')
    total = product_1*300 + product_2*400 + product_3*500
    print(total)
