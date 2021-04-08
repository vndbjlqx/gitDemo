import random


class hero:
    name = ""
    hp = 0
    power = 0
    speak_lines = ""

    def fight(self, cur_hp, cur_power):

        other_hp = cur_hp - self.power * random.randint(1, 10)
        self.hp = self.hp - cur_power * random.randint(1, 10)

        if other_hp <= 0:
            # enemy be killed by one shot. hero win.
            print(f"{self.name} is win.")
        elif self.hp <= 0:
            # hero be killed by one shot. hero fail.
            print(f"{self.name} is fail.")
        elif self.hp > other_hp:
            # hero has more hp left. hero win.
            print(f"{self.name} is win.")
        elif self.hp < other_hp:
            # enemy has more hp left. hero fail.
            print(f"{self.name} is fail.")
        else:
            print("Draw")

    def speak(self, speak_lines):
        print("hero is saying.")
