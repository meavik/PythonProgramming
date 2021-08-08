import time

# print("For loop")
initail1 = time.time()
for i in range(1,10000):
    print(i)
    # time.sleep(.2)
initail2 = time.time()
exc_time1 = initail2 - initail1

# print("While loop")
initail1 = time.time()
i = 1
while i<10000:
    print(i)
    i += 1
    # time.sleep(.2)
initail2 = time.time()
exc_time2 = initail2 - initail1
print(f'Time neede for For loop to execute the program {exc_time1}s')
print(f'Time neede for While loop to execute the program {exc_time2}s')
