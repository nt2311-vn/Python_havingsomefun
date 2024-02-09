class Soldier:
    health = 100
    weapon = "gun"

    def take_weapon(self):
        self.weapon = ""

    def cause_damage(self, dmg):
        self.health -= dmg

    def assign_weapon(self, give_weapon):
        self.weapon = give_weapon

    def recover_heath(self):
        self.health = 100


soldier_1 = Soldier()

soldier_1.cause_damage(20)
soldier_1.assign_weapon("machine gun")


def soldier_status(soldier):
    print(
        f"Current status of soldier: health - {soldier.health}, weapon - {soldier.weapon}"
    )


soldier_status(soldier_1)
