class Compte:
    def __init__(self, nom, marchandise, quantite, pvunitaire, capital, prixAchat, reste, dette1, depenseUnitaire):
        self.nom = nom
        self.marchandise = marchandise  
        self.quantite = quantite
        self.pvunitaire = pvunitaire
        self.capital = capital
        self.prixAchat = prixAchat
        self.reste = reste
        self.dette1 = dette1
        self.depenseUnitaire = depenseUnitaire
        self.prixvente = 0
        self.res_brut = 0  
        self.dep_total = 0
        self.dette_total = 0
        self.benefice = 0
        self.res_final = 0

    def calcul_prix_vente(self):
        self.prixvente = self.quantite * self.pvunitaire
        return self.prixvente

    def calcul_resultat_brut(self):
        self.res_brut = self.prixvente - self.prixAchat
        return self.res_brut

    def calcul_depense_totale(self):
        self.dep_total = self.quantite * self.depenseUnitaire
        return self.dep_total

    def calcul_dette(self):
        self.dette_total = self.dep_total + self.dette1 - self.reste
        return self.dette_total

    def calcul_benefice(self):
        self.benefice = self.res_brut - self.dette_total
        return self.benefice

    def calcul_resultat_final(self):
        self.res_final = self.capital + self.benefice
        return self.res_final

    def afficher_resultats(self):
        print("Prix de vente total =", self.prixvente)
        print("Résultat brut =", self.res_brut)
        print("Dépenses totales =", self.dep_total)
        print("Dette totale =", self.dette_total)
        print("Bénéfice =", self.benefice)
        print("Résultat final =", self.res_final)


