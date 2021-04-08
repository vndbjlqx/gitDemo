from heroHomework.hero import hero


class police(hero):
    name = "Police"
    hp = 2000
    power = 200
    speak_lines = "Taste my justic bullets."

    def speak(self, speak_lines):
        print(self.speak_lines)