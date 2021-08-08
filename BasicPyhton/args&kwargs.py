    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f'{key} is a {value}')


dic = {
    'Shaun':'Police',
    'Óvi':"Chef",
    'Ashraf':'Programmer'
}
li = list(('mira','harry','mahadi',('musa','maggi')))
arbitrary_function(li,*li,**dic)
