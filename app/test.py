# Tests unitaires
import unittest


class TestCompte(unittest.TestCase):

    def setUp(self):
        # Configuration initiale d'un objet Compte pour les tests
        self.compte = Compte(
            nom="Testeur",
            marchandise="ProduitX",
            quantite=100,
            pvunitaire=50,
            capital=1000,
            prixAchat=3000,
            reste=500,
            dette1=200,
            depenseUnitaire=5
        )

    def test_calcul_prix_vente(self):
        self.assertEqual(self.compte.calcul_prix_vente(), 5000)

    def test_calcul_resultat_brut(self):
        self.compte.calcul_prix_vente()  # Assurez-vous que prixvente est calculé
        self.assertEqual(self.compte.calcul_resultat_brut(), 2000)

    def test_calcul_depense_totale(self):
        self.assertEqual(self.compte.calcul_depense_totale(), 500)

    def test_calcul_dette(self):
        self.compte.calcul_depense_totale()  # Assurez-vous que dep_total est calculé
        self.assertEqual(self.compte.calcul_dette(), 200)

    def test_calcul_benefice(self):
        self.compte.calcul_prix_vente()
        self.compte.calcul_resultat_brut()
        self.compte.calcul_depense_totale()
        self.compte.calcul_dette()
        self.assertEqual(self.compte.calcul_benefice(), 1800)

    def test_calcul_resultat_final(self):
        self.compte.calcul_prix_vente()
        self.compte.calcul_resultat_brut()
        self.compte.calcul_depense_totale()
        self.compte.calcul_dette()
        self.compte.calcul_benefice()
        self.assertEqual(self.compte.calcul_resultat_final(), 2800)

if __name__ == "__main__":
    unittest.main()
