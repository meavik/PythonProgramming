import random

f_name = ['Avik','Animesh',"Shaun","Ovi","Guddu","Manish","Deep","Amit","Sushant"]
l_name = ['Roy',"Pal","Chatergee",'Ganguly',"Banerjee","Mittal","Kapoor"]
city = ["Dhaka","Mumbai","Delhi","Newyork","Beijing","London","Westminister"]

fname = random.choice(f_name)
lname = random.choice(l_name)
full_name = fname + ' ' + lname
city_name = random.choice(city)
email = fname.lower() + lname.lower()+'@gmail.com'
phone_num = '01'+str(random.choice([3,4,5,6,7,8,9]))+str(random.randint(10000000,99999999))
print("Name: "+full_name+'\n'+"City: "+city_name+'\n'+"Email: "+email+'\n'+"Phone-no: "+phone_num)
