from resultat import Compte

# Création d'une instance de la classe Compte
mon_compte = Compte(
    nom="Entreprise ABC",
    marchandise="Produits A",
    quantite=100,
    pvunitaire=50,
    capital=10000,
    prixAchat=3000,
    reste=500,
    dette1=1000,
    depenseUnitaire=10
)

# Calculs principaux
print("---- CALCULS ----")
mon_compte.calcul_prix_vente()
mon_compte.calcul_resultat_brut()
mon_compte.calcul_depense_totale()
mon_compte.calcul_dette()
mon_compte.calcul_benefice()
mon_compte.calcul_resultat_final()
mon_compte.afficher_resultats()

# Calcul de la marge bénéficiaire
print("\n---- MARGE BÉNÉFICIAIRE ----")
marge = mon_compte.calcul_marge_beneficiaire()
print(f"Marge bénéficiaire : {marge:.2f}%")

# Simulation d'évolution financière
print("\n---- SIMULATION D'ÉVOLUTION DU CAPITAL ----")
capital_simule = mon_compte.simuler_evolution_capital(periodes=5, taux_croissance=0.05)
print(f"Capital après 5 périodes avec un taux de croissance de 5% : {capital_simule:.2f}")

# Enregistrement de transactions
print("\n---- TRANSACTIONS ----")
mon_compte.enregistrer_transaction("vente", 5000, "Vente de produits A")
mon_compte.enregistrer_transaction("achat", 2000, "Achat de marchandises")
mon_compte.afficher_historique()

# Exportation des résultats
print("\n---- EXPORTATION ----")
mon_compte.exporter_resultats("resultats_compte.txt")

# Alerte sur les dettes
print("\n---- ALERTE DETTE ----")
mon_compte.alerter_si_dette_elevee(seuil=2000)

# Calcul de la rentabilité unitaire
print("\n---- RENTABILITÉ UNITAIRE ----")
rentabilite = mon_compte.calcul_rentabilite_unitaire()
print(f"Rentabilité unitaire : {rentabilite:.2f}")

