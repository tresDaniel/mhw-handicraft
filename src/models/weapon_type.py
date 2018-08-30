from common.database import Database


class WeaponType(object):

    def __init__(self, name, multiplier, _id):
        self.name = name
        self.multiplier = multiplier
        self._id = _id

    def json(self):
        return {
            'name': self.name,
            'multiplier': self.multiplier,
            '_id': self._id
        }

    def __save(self):
        Database.insert(collection='weapon_types',
                        data=self.json())

    def register(self):
        weapon_type = WeaponType(self.name, self.multiplier, self._id)
        weapon_type.__save()

    @classmethod
    def find_by_name(cls, name):
        weapon_type = Database.find_one(collection='weapon_types', query={'name': name})
        if weapon_type:
            return cls(**weapon_type)

    @staticmethod
    def find_all():
        weapon_types = Database.find(collection='weapon_types', query={})

        weapon_type = next(weapon_types)

        if weapon_type:
            return weapon_type
