from common.database import Database


class DamageType(object):

    def __init__(self, name, _id):
        self.name = name
        self._id = _id

    def json(self):
        return {
            'name': self.name,
            '_id': self._id
        }

    def __save(self):
        Database.insert(collection='damage_types',
                        data=self.json())

    def register(self):
        damage_type = DamageType(self.name, self._id)
        damage_type.__save()

    @classmethod
    def find_by_name(cls, name):
        damage_type = Database.find_one(collection='damage_types', query={'name': name})
        if damage_type:
            return cls(**damage_type)

    @staticmethod
    def find_all():
        damage_types = list(Database.find(collection='damage_types', query={}))

        return damage_types
