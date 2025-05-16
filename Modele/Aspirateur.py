from Modele.RobotMobile import RobotMobile


class Aspirateur:
    def __init__(self, marque, puissance : int):

        self._marque = marque
        self._puissance = puissance


    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque):
        self._marque = marque

    @property
    def puissance(self):
        return self._puissance
    @puissance.setter
    def puissance(self, puissance):
        self._puissance = puissance

    def __str__(self):
        return "Aspirateur : "+self._marque+" Puissance : "+str(self._puissance)

class AspirateurRobot(Aspirateur, RobotMobile):
    def __init__(self, abs=0, ord=0, marque="Bosch'", puissance=4):
        RobotMobile.__init__(self, robot_type="Aspirateur Robot", abs=0, ord=0)
        Aspirateur.__init__(self, marque, puissance)
        self._distance_max = 1000
        self._robot_type = "Aspirateur Robot"

    @property
    def distance_max(self):
        return self._distance_max
    @distance_max.setter
    def distance_max(self, value):
        if value > 0:
            self._distance_max = value

    def __str__(self):
        return (RobotMobile.__str__(self)+"\n"+
               "Marque : "+str(self._marque)+"\n"+
                "Puissance : "+str(self._puissance))


