from heroHomework.hero import hero


class timo(hero):
    name = "Timo"
    hp = 2500
    power = 100
    speak_lines = "Captian Timo is ready."

    def speak(self, speak_lines):
        print(self.speak_lines)

