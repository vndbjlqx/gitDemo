from heroHomework.police import police
from heroHomework.timo import timo


class heroFactory:
    def createhero(self, heroName):
        heroName = str.upper(heroName)
        if heroName == "timo".upper():
            return timo()
        elif heroName == "police".upper():
            return police()
        else:
            raise Exception(f"Hero {heroName} is on the road.")


facObj = heroFactory()
timoObj = facObj.createhero("timo")
policeObj = facObj.createhero("police")

timoObj.fight(policeObj.hp, policeObj.power)
#policeObj.fight(timoObj.hp, timoObj.power)
