## iterate over dict
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}

for name in x:
    print(x[name])

for email in x.values():
    print(email)

for name, email in x.items():
    print(name)
    print(email)

## unpack a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x

