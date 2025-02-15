""" Heure:  doit être dans l’intervalle 0  heure  23– Minute: doit être dans l’intervalle 0  minute  59- Seconde: doit être dans l’intervalle 0  seconde  59
 >>> temps1.setTemps(25,10,63)
 >>> temps1
 1:11:3
Appelez cette méthode dans __init__ aussi pour corriger les 
valeurs si elles ne sont pas correctes
Ajouter les méthodes suivantes à la classe Temps:
 • estAvant(t2)
 retourne True si le temps représenté par self est avant le 
temps de t2, sinon elle retourne False.
 • durée(t2)
 retourne un nouvel objet Temps avec le nombre d’heures, de 
minutes, et de secondes entre self et t2.
 • Testez vos méthodes dans l’interpréteur ou dans le programme 
principal
 >> t1 = Temps(12,4,0)
 >>> t1.estAvant(t2)
 False
 >>> t1.durée(t2)
 0:41:"""

class Temps(object):
    def __init__(self, hh=12, mm=0, s=0):
        '''(Temps)-> None'''
        self.setTemps(hh, mm, s)
    def setTemps(self, hh=12, mm=0, s=0):
        '''(Temps)-> None'''
        if hh>=0 and hh<24:
            self.heure = hh
        else:
            self.heure = hh - (24*(hh//24))
        if mm>=0 and mm<60:
            self.minute = mm
        else:
            self.heure += mm//60
            self.minute = mm - (60*(mm//60))
        if s>=0 and s<60:
            self.seconde = s
        else:
            self.minute += s//60
            self.seconde = s - (60*(s//60))
    def estAvant(self, object):
        return object.heure > self.heure or (object.heure==self.heure and (object.minute > self.minute or (object.minute == self.minute and object.seconde > self.seconde)))
    def duree(self, object):
        Temps_s = abs(object.heure*3600 - self.heure*3600) + abs(object.minute*60 - self.minute*60) + abs(object.seconde - self.seconde)
        final = Temps.setTemps(self, hh=0, mm=0, s=Temps_s)
        return str(self.heure) + ":" + str(self.minute) + ":" + str(self.seconde)
    def __eq__(self, autre):
        '''(Temps)-> bool'''
        return self.heure == autre.heure and self.minute == autre.minute and self.seconde == autre.seconde
    def __repr__(self):
        return (str(self.heure) +":" +str(self.minute) +":" +str(self.seconde))

temps1 = Temps(1,9,92)
temps2 = Temps(50, 20, 99)
print(temps1)
print(temps2)
print(temps1.estAvant(temps2))
print(temps1.duree(temps2))

