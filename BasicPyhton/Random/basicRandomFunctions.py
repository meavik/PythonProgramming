import random
#random generates value from 0 to 1...excluding 1
val = random.random()
print(int(val*10))
# uniform method generates the random numbers in ceratain range given in arguments
val = random.uniform(23,25.5)
print(val)
# the randint() generates a random number in a certain range including the end point
val = random.randint(10,20)
print(val)
# choice() selects a random value from a container
li = ['green','blue','yellow','megenta','pink','violet']
val = random.choice(li)
print(val)
# choices() retrives multiple values from a container..k value specifies how many value to retrive the wieght specifies how's the probability of an items being retrived 
li = ['green','blue','yellow','megenta','pink','violet']
val = random.choices(li,k=2,weights=[10,10,5,2,1,.5,])
print(val)
# sample() retrives the unique value from a list
li = ['green','blue','yellow','megenta','pink','violet']
val = random.sample(li,k=5)
print(val)
