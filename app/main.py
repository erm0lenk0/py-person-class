class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]

        person_instance = Person(name, age)

        person_instances.append(person_instance)

    for person_dict in people_list:
        name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            if wife_name in Person.people:
                Person.people[name].wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            if husband_name in Person.people:
                Person.people[name].husband = Person.people[husband_name]

    return person_instances





