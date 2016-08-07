import csv


class User:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.occupation = kwargs['occupation']
        self.zip_code = kwargs['zip_code']

    def __str__(self):
        return "{} {}".format(self.user_id, self.age)


class UserLibrary:
    def __init__(self):
        fieldnames = ['id', 'age', 'gender', 'occupation', 'zip_code']
        self.users = {}
        with open('ml-100k/u.user', 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter='|')
            for row in reader:
                user = User(**row)
                self.users[user.id] = user
        print(self.users)
