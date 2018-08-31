from common.database import Database


class Weapon(object):
    def __init__(self, weapon_type, name, rarity, raw_damage, true_damage, elemental_damage, status_damage, damage_type,
                 sharpness, awakened, affinity, defense, slot, _id):
        self.weapon_type = weapon_type
        self.name = name
        self.rarity = rarity
        self.raw_damage = raw_damage
        self.true_damage = true_damage
        self.elemental_damage = elemental_damage
        self.status_damage = status_damage
        self.damage_type = damage_type
        self.sharpness = sharpness
        self.awakened = awakened
        self.affinity = affinity
        self.defense = defense
        self.slot = slot
        self._id = _id

    def json(self):
        return {
            'weapon_type': self.weapon_type,
            'name': self.name,
            'rarity': self.rarity,
            'raw_damage': self.raw_damage,
            'true_damage': self.true_damage,
            'elemental_damage': self.elemental_damage,
            'status_damage': self.status_damage,
            'damage_type': self.damage_type,
            'sharpness': self.sharpness,
            'awakened': self.awakened,
            'affinity': self.affinity,
            'defense': self.defense,
            'slot': self.slot,
            '_id': self._id
        }

    def __save(self):
        Database.insert(collection='weapons',
                        data=self.json())

    def register(self):
        weapon = Weapon(self.weapon_type.json(), self.name, self.rarity, self.raw_damage, self.true_damage,
                        self.elemental_damage, self.status_damage, self.damage_type.json(), self.sharpness,
                        self.awakened, self.affinity, self.defense, self.slot, self._id)
        weapon.__save()

    @classmethod
    def find_by_name(cls, name):
        weapon = Database.find_one(collection='weapon', query={'name': name})
        if weapon:
            return cls(**weapon)

    @classmethod
    def find_by_type(cls, weapon_type):
        weapon = Database.find_one(collection='weapon', query={'type': weapon_type})
        if weapon:
            return cls(**weapon)

    @staticmethod
    def find_all():
        weapon = list(Database.find(collection='weapon', query={}))

        return weapon
