import tkinter as tk
import ClassInsta
def on_button_click():

    user_input = entry.get()
    InstaBot = ClassInsta.InstaJuju(user_input)
    label_scan_en_cours = tk.Label(root, text="Scan en cours...")
    label_scan_en_cours.pack()
    # Mettre à jour l'interface pour que le message s'affiche
    root.update()
    # Appeler attendre() de manière asynchrone
    res = InstaBot.Verif_Abo()
    # Mettre à jour l'interface pour que le message "Scan en cours" disparaisse
    root.after(1, lambda: label_scan_en_cours.pack_forget())
    # Afficher les résultats après que le scan est terminé
    label_resultat_scan = tk.Label(root, text=f"Résultat du scan de {user_input} :")
    label_resultat_scan.pack()
        # Créer un widget Text pour afficher les résultats
    text_widget = tk.Text(root, height=10, width=50)  # Ajustez la hauteur et la largeur selon vos besoins
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Ajouter les résultats au widget Text
    if isinstance(res, list):
        text_widget.insert(tk.END, f"Il y a {len(res)} personnes qui ne followback pas\n")
        for profil in res:
            text_widget.insert(tk.END, f"Le profil '{profil}' ne followback pas\n")

    else:
        text_widget.insert(tk.END, res)

    # Empêcher l'édition du texte
    text_widget.config(state=tk.DISABLED)

    # Ajouter une barre de défilement
    scrollbar = tk.Scrollbar(root, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=scrollbar.set)
    


# Créer une instance de la fenêtre principale
root = tk.Tk()
root.title('App INSTA by DELATTRE Julien')

# Ajouter un libellé pour afficher le texte saisi
label = tk.Label(root, text="Entrez un utlisateur instagram sans le '@'")
label.pack()

# Ajouter une entrée à la fenêtre
entry = tk.Entry(root)
entry.pack()

# Ajouter un bouton pour récupérer le texte saisi dans l'entrée
button = tk.Button(root, text="Lancer le scan", command=on_button_click)
button.pack()

# Lancer la boucle principale
root.mainloop()