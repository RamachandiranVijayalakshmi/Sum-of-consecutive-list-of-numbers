def num(n):
   return sum([i for i in range(n+1)])
a=int(input('Enter the Consecutive number:'))
print('Add a Consecutive List of Numbers',a,'is:',num(a))