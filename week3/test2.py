people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]


def get_age(myname):
    for person in people:
        if person['name'] == myname:
            print(person['age'])


print(get_age('bob'))
print(get_age('kay'))