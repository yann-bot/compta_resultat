import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from resultat import Compte
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class InterfaceCompte:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Compte")
        self.root.configure(bg="green")

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

        # Configuration des champs d'entrée avec des couleurs et un layout responsive
        fields = [
            ("Nom", self.nom),
            ("Marchandise", self.marchandise),
            ("Quantité", self.quantite),
            ("Prix Vente Unitaire", self.pvunitaire),
            ("Capital", self.capital),
            ("Prix Achat", self.prixAchat),
            ("Reste", self.reste),
            ("Dette", self.dette1),
            ("Dépense Unitaire", self.depenseUnitaire),
        ]

        for i, (label_text, var) in enumerate(fields):
            tk.Label(root, text=label_text, bg="green", fg="white").grid(row=i, column=0, sticky="w", padx=10, pady=5)
            tk.Entry(root, textvariable=var).grid(row=i, column=1, sticky="ew", padx=10, pady=5)

        # Bouton pour calculer et afficher les résultats
        tk.Button(root, text="Calculer", command=self.calculer, bg="darkgreen", fg="white").grid(row=len(fields), column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Bouton pour exporter les résultats
        tk.Button(root, text="Exporter", command=self.exporter, bg="darkgreen", fg="white").grid(row=len(fields)+1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Zone pour afficher les résultats
        self.resultats = tk.Text(root, height=10, width=50, bg="lightgreen", fg="black")
        self.resultats.grid(row=len(fields)+2, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

        # Configuration du layout responsive
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.rowconfigure(len(fields)+2, weight=1)

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

        fichier = asksaveasfilename(defaultextension=".pdf", filetypes=[("Fichiers PDF", "*.pdf")])
        if fichier:
            try:
                c = canvas.Canvas(fichier, pagesize=letter)
                c.drawString(100, 750, f"Nom: {self.compte.nom}")
                c.drawString(100, 730, f"Marchandise: {self.compte.marchandise}")
                c.drawString(100, 710, f"Prix de vente total: {self.compte.prixvente}")
                c.drawString(100, 690, f"Résultat brut: {self.compte.res_brut}")
                c.drawString(100, 670, f"Dépenses totales: {self.compte.dep_total}")
                c.drawString(100, 650, f"Dette totale: {self.compte.dette_total}")
                c.drawString(100, 630, f"Bénéfice: {self.compte.benefice}")
                c.drawString(100, 610, f"Résultat final: {self.compte.res_final}")
                c.save()
                messagebox.showinfo("Succès", f"Résultats exportés dans {fichier}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'exportation: {str(e)}")

# Lancement de l'application
root = tk.Tk()
app = InterfaceCompte(root)
root.mainloop()
