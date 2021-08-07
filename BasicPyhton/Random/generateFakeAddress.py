import random
f_name = ["Amit","Hrithik","Priya","Mithun","Surpiya","Nilesh","Bankim","Abhay","Nirmala"]
l_name =["Das",'Dasgupta','Khakkar','Desmukh',"Chaterjee",'Mukharjee','Gosh','Çhakrabarty']
city_name = ['Delhi','Mumbai',"Lokhnow",'Ámritsar','Bangalore','Kolkata','Guhati','Patna']
state_name = ['Punjab','Maharastra','Tamil Nadu','Udissa','Jharkhanda','West Bengal','Gujrat']

for i in range(6):
    name = f'{random.choice(f_name)} {random.choice(l_name)}'
    phone_number = f'+99{random.randint(5000,10000)}-22-{random.randint(100,1000)}'
    street_number = f'Road No# {random.randint(1,10)} Block No# {chr(random.choice(range(65,91)))}'
    state = random.choice(state_name)
    city = random.choice(city_name)
    zip = random.randint(700,1200)
    address = f'{street_number}\nZip Code: {zip}\nCity: {city}\nState: {state}'
    mail = f'{name.lower().replace(" ","")}@fakemail.com'

    print(f'Name:{name}\nAddress\n{address}\nContact No: {phone_number}\nEmail: {mail}\n')
