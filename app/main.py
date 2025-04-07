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
            wife_name = person_dict.get("wife")
            if wife_name is not None and wife_name in Person.people:
                Person.people[name].wife = Person.people[wife_name]
                Person.people[wife_name].husband = Person.people[name]

            husband_name = person_dict.get("husband")
            if husband_name is not None and wife_name in Person.people:
                Person.people[name].husband = Person.people[husband_name]
                Person.people[husband_name].wife = Person.people[name]

        return person_instances
