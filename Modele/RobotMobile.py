from Modele.Robot import Robot


class RobotMobile(Robot):
    '''RobotMobile hérite de Robot'''

    def __init__(self, robot_type="Générique", abs=0, ord=0):
        super().__init__()  #super() pour reprendre la construction de la classe supérieure, sans self
        self._Abscisse=abs
        self._Ordonnée=ord

    @property
    def Abscisse(self):
        return self._Abscisse
    @property
    def Ordonnée(self):
        return self._Ordonnée

    def afficher_position(self):
        position=""
        position=position.join("Position : [abs="+str(self._Abscisse)+" ; ord="+str(self.Ordonnée)+"]")
        return position

    def avancer(self, m:int):
        match self.orientation:
            case "EST":
                self._Abscisse += m
            case "OUEST":
                self._Abscisse -= m
            case "NORD":
                self._Ordonnée += m
            case "SUD":
                self._Ordonnée -= m

    def __str__(self):
        parent_str = super().__str__()              #Récupérer la string de la superclasse
        position_str = self.afficher_position()     #Récupérer la position par la fonction
        affichage=parent_str+position_str           #Concaténation
        return affichage