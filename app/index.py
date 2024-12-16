import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
from datetime import datetime

class ComptabiliteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application de Comptabilité")
        self.root.geometry("800x600")
        
        # Variables
        self.transactions = []
        self.solde = 0

        # Frame des entrées
        self.frame_entrées = tk.Frame(root)
        self.frame_entrées.pack(pady=10, fill=tk.X)

        tk.Label(self.frame_entrées, text="Montant:").grid(row=0, column=0, padx=5)
        self.entry_montant = tk.Entry(self.frame_entrées)
        self.entry_montant.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_entrées, text="Catégorie:").grid(row=0, column=2, padx=5)
        self.entry_categorie = tk.Entry(self.frame_entrées)
        self.entry_categorie.grid(row=0, column=3, padx=5)

        tk.Label(self.frame_entrées, text="Type:").grid(row=0, column=4, padx=5)
        self.type_var = tk.StringVar(value="Revenu")
        ttk.Combobox(self.frame_entrées, textvariable=self.type_var, values=["Revenu", "Dépense"]).grid(row=0, column=5, padx=5)

        tk.Label(self.frame_entrées, text="Date (YYYY-MM-DD):").grid(row=0, column=6, padx=5)
        self.entry_date = tk.Entry(self.frame_entrées)
        self.entry_date.grid(row=0, column=7, padx=5)

        self.btn_ajouter = tk.Button(self.frame_entrées, text="Ajouter", command=self.ajouter_transaction)
        self.btn_ajouter.grid(row=0, column=8, padx=5)

        # Solde
        self.label_solde = tk.Label(root, text="Solde actuel: 0.00 €", font=("Arial", 16))
        self.label_solde.pack(pady=10)

        # Historique
        self.tableau = ttk.Treeview(root, columns=("Montant", "Catégorie", "Type", "Date"), show="headings")
        self.tableau.heading("Montant", text="Montant")
        self.tableau.heading("Catégorie", text="Catégorie")
        self.tableau.heading("Type", text="Type")
        self.tableau.heading("Date", text="Date")
        self.tableau.pack(pady=10, fill=tk.BOTH, expand=True)

        # Boutons de gestion
        self.frame_gestion = tk.Frame(root)
        self.frame_gestion.pack(pady=10)

        tk.Button(self.frame_gestion, text="Sauvegarder", command=self.sauvegarder_transactions).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_gestion, text="Charger", command=self.charger_transactions).pack(side=tk.LEFT, padx=5)

    def ajouter_transaction(self):
        try:
            montant = float(self.entry_montant.get())
            categorie = self.entry_categorie.get()
            type_transaction = self.type_var.get()
            date_str = self.entry_date.get()
            date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if type_transaction == "Dépense":
                montant = -montant

            self.transactions.append((montant, categorie, type_transaction, date))
            self.solde += montant
            self.mise_a_jour_ui()
        except ValueError as e:
            messagebox.showerror("Erreur", "Veuillez entrer des données valides.")

    def mise_a_jour_ui(self):
        self.label_solde.config(text=f"Solde actuel: {self.solde:.2f} €")
        for row in self.tableau.get_children():
            self.tableau.delete(row)
        for transaction in self.transactions:
            self.tableau.insert("", tk.END, values=transaction)

    def sauvegarder_transactions(self):
        fichier = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if fichier:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Montant", "Catégorie", "Type", "Date"])
                writer.writerows(self.transactions)
            messagebox.showinfo("Succès", "Transactions sauvegardées avec succès.")

    def charger_transactions(self):
        fichier = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if fichier:
            with open(fichier, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                self.transactions = []
                self.solde = 0
                for row in reader:
                    montant, categorie, type_transaction, date_str = row
                    self.transactions.append((float(montant), categorie, type_transaction, datetime.strptime(date_str, "%Y-%m-%d").date()))
                    self.solde += float(montant)
            self.mise_a_jour_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = ComptabiliteApp(root)
    root.mainloop()
