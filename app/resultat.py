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
        self.historique = []

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

    def calcul_marge_beneficiaire(self):
        if self.prixvente > 0:
            marge = (self.benefice / self.prixvente) * 100
            return marge
        else:
            return 0

    def simuler_evolution_capital(self, periodes, taux_croissance):
        capital_projection = self.capital
        for _ in range(periodes):
            capital_projection += capital_projection * taux_croissance
        return capital_projection

    def enregistrer_transaction(self, type_transaction, montant, description):
        transaction = {
            "type": type_transaction,
            "montant": montant,
            "description": description
        }
        self.historique.append(transaction)

    def afficher_historique(self):
        for transaction in self.historique:
            print(transaction)

    def exporter_resultats(self, nom_fichier):
        with open(nom_fichier, "w") as fichier:
            fichier.write(f"Propriétaire ={self.nom}\n")
            fichier.write(f"Marchandise = {self.marchandise}\n")  
            fichier.write(f"Quantite = {self.quantite}\n")  
            fichier.write(f"Prix de vente total = {self.prixvente}\n")
            fichier.write(f"Résultat brut = {self.res_brut}\n")
            fichier.write(f"Dépenses totales = {self.dep_total}\n")
            fichier.write(f"Dette totale = {self.dette_total}\n")
            fichier.write(f"Bénéfice = {self.benefice}\n")
            fichier.write(f"Résultat final = {self.res_final}\n")
        print(f"Résultats exportés dans {nom_fichier}")

    def alerter_si_dette_elevee(self, seuil):
        if self.dette_total > seuil:
            print(f"Attention : la dette totale ({self.dette_total}) dépasse le seuil de {seuil}.")

    def calcul_rentabilite_unitaire(self):
        if self.prixAchat > 0:
            return (self.pvunitaire - (self.prixAchat / self.quantite))
        else:
            return 0

    def afficher_resultats(self): 
        print("Propriétaire du compte =", self.nom)
        print("Marchandise =", self.marchandise)
        print("Quantité =", self.quantite)
        print("Prix de vente total =", self.prixvente)
        print("Résultat brut =", self.res_brut)
        print("Dépenses totales =", self.dep_total)
        print("Dette totale =", self.dette_total)
        print("Bénéfice =", self.benefice)
        print("Résultat final =", self.res_final)

