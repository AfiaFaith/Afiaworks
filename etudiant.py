# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:12:33 2022

@author: Afia Faith
"""

class etudiant():

    def __init__(self,nom,dateNaissance,nbNote):
        self.nom = nom
        self.dateNaissance = dateNaissance
        self.nbNote =  nbNote
        
    def getnom(self):
        return self.nom
            
    def getdateNaissance(self):
        return self.dateNaissance
            
    def getNote(self):
        return self.nbNote
        
    def set_etudiant(self):
        self.nom = input('Entrer le nom de l eleve')
        self.dateNaissance = input('Entrer la date de naissance de l eleve')
        self.nbNote=input('Entrer la note de l eleve')
        
    def __str__(self):
        message = f'Bonjour, l eleve s appelle {self.nom}.Il est ne le {self.dateNaissance} et il {self.nbNote} comme note'
        return message


if __name__ == '__main__':
        work = etudiant('nom','dateNaissance', 'nbNote')
        work.set_etudiant()
        print(work)
        print(f'Bonjour, l eleve s appelle {work.getnom()}')
        print(f'Bonjour, l eleve est nee le {work.getdateNaissance()}')
        print(f'Bonjour, l eleve a {work.getNote()} comme note')
