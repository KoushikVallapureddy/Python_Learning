from character import Character

class Mage(Character):
    def __init__(self, name, level=1):
        super().__init__(name, level)
        self.max_health = 80
        self.health = 80
        self.max_mana = 150
        self.mana = 150
        self.strength = 5
        self.intelligence = 20
        self.defense = 3
    
    def level_up(self):
        result = super().level_up()
        self.intelligence += 2
        self.max_mana += 15
        self.mana = self.max_mana
        return result
    
    def attack(self, target):
        damage = self.intelligence * 0.4
        damage_dealt = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage_dealt:.1f} damage")

        mana_regen = 5
        self.mana = min(self.max_mana, self.mana + mana_regen)

        return damage_dealt