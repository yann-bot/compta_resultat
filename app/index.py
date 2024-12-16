import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from resultat import Compte

class InterfaceCompte:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Compte")

        # Variables pour les champs de saisie
        self.nom = tk.StringVar()
        self.marchandise = tk.StringVar()
        self.quantite = tk.IntVar()
        self.pvunitaire = tk.DoubleVar()
        self.capital = tk.DoubleVar()
        self.prixAchat = tk.DoubleVar()
        self.reste = tk.DoubleVar()
        self.dette1 = tk.DoubleVar()
        self.depenseUnitaire = tk.DoubleVar()

        # Configuration des champs d'entrée
        tk.Label(root, text="Nom").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.nom).grid(row=0, column=1)

        tk.Label(root, text="Marchandise").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.marchandise).grid(row=1, column=1)

        tk.Label(root, text="Quantité").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.quantite).grid(row=2, column=1)

        tk.Label(root, text="Prix Vente Unitaire").grid(row=3, column=0)
        tk.Entry(root, textvariable=self.pvunitaire).grid(row=3, column=1)

        tk.Label(root, text="Capital").grid(row=4, column=0)
        tk.Entry(root, textvariable=self.capital).grid(row=4, column=1)

        tk.Label(root, text="Prix Achat").grid(row=5, column=0)
        tk.Entry(root, textvariable=self.prixAchat).grid(row=5, column=1)

        tk.Label(root, text="Reste").grid(row=6, column=0)
        tk.Entry(root, textvariable=self.reste).grid(row=6, column=1)

        tk.Label(root, text="Dette").grid(row=7, column=0)
        tk.Entry(root, textvariable=self.dette1).grid(row=7, column=1)

        tk.Label(root, text="Dépense Unitaire").grid(row=8, column=0)
        tk.Entry(root, textvariable=self.depenseUnitaire).grid(row=8, column=1)

        # Bouton pour calculer et afficher les résultats
        tk.Button(root, text="Calculer", command=self.calculer).grid(row=9, column=0, columnspan=2)

        # Bouton pour exporter les résultats
        tk.Button(root, text="Exporter", command=self.exporter).grid(row=10, column=0, columnspan=2)

        # Zone pour afficher les résultats
        self.resultats = tk.Text(root, height=10, width=50)
        self.resultats.grid(row=11, column=0, columnspan=2)

    def calculer(self):
        # Création de l'objet Compte
        compte = Compte(
            nom=self.nom.get(),
            marchandise=self.marchandise.get(),
            quantite=self.quantite.get(),
            pvunitaire=self.pvunitaire.get(),
            capital=self.capital.get(),
            prixAchat=self.prixAchat.get(),
            reste=self.reste.get(),
            dette1=self.dette1.get(),
            depenseUnitaire=self.depenseUnitaire.get(),
        )

        # Calculs
        compte.calcul_prix_vente()
        compte.calcul_resultat_brut()
        compte.calcul_depense_totale()
        compte.calcul_dette()
        compte.calcul_benefice()
        compte.calcul_resultat_final()

        # Affichage des résultats
        self.resultats.delete(1.0, tk.END)
        self.resultats.insert(tk.END, f"Prix de vente total: {compte.prixvente}\n")
        self.resultats.insert(tk.END, f"Résultat brut: {compte.res_brut}\n")
        self.resultats.insert(tk.END, f"Dépenses totales: {compte.dep_total}\n")
        self.resultats.insert(tk.END, f"Dette totale: {compte.dette_total}\n")
        self.resultats.insert(tk.END, f"Bénéfice: {compte.benefice}\n")
        self.resultats.insert(tk.END, f"Résultat final: {compte.res_final}\n")

        self.compte = compte  # Sauvegarde l'objet pour l'exportation

    def exporter(self):
        if not hasattr(self, 'compte'):
            messagebox.showerror("Erreur", "Aucun calcul effectué !")
            return

        fichier = asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
        if fichier:
            self.compte.exporter_resultats(fichier)
            messagebox.showinfo("Succès", f"Résultats exportés dans {fichier}")

# Lancement de l'application
root = tk.Tk()
app = InterfaceCompte(root)
root.mainloop()
