def create_person(**kwargs):
    person = dict(kwargs)
    print("Person created with properties:")
    for key, value in person.items():
        print(f"{key}: {value}")
    return person
