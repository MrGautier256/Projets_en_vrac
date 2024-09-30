import tkinter as tk
import random

class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jeu de Morpion")

        self.current_player = random.choice(['X', 'O'])
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Bouton pour recommencer la partie
        self.reset_button = tk.Button(self.window, text="Recommencer", font=('Arial', 15),
                                      command=self.reset_game)
        self.reset_button.grid(row=0, column=0, columnspan=3)

        # Créer la grille de boutons
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', font=('Arial', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i+1, column=j)  # Décaler la grille pour laisser de la place au bouton "Recommencer"
                self.buttons[i][j] = button

        # Afficher le joueur courant
        self.label = tk.Label(self.window, text=f"Tour du joueur : {self.current_player}", font=('Arial', 20))
        self.label.grid(row=4, column=0, columnspan=3)

        # Bouton "Rejouer" (invisible au départ)
        self.play_again_button = tk.Button(self.window, text="Rejouer", font=('Arial', 15),
                                           command=self.reset_game)
        self.play_again_button.grid(row=5, column=0, columnspan=3)
        self.play_again_button.grid_remove()

    def on_click(self, row, col):
        # Jouer le coup si la case est vide
        if self.board[row][col] == '-':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Vérifier si le joueur a gagné
            if self.is_winner(self.current_player):
                self.label.config(text=f"Le joueur {self.current_player} gagne la partie !")
                self.disable_buttons()
                self.play_again_button.grid()  # Afficher le bouton "Rejouer"
            # Vérifier si c'est un match nul
            elif self.is_draw():
                self.label.config(text="Match nul !")
                self.disable_buttons()
                self.play_again_button.grid()  # Afficher le bouton "Rejouer"
            else:
                # Changer de joueur
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.label.config(text=f"Tour du joueur : {self.current_player}")

    def is_winner(self, player):
        # Vérifier les lignes, colonnes, et diagonales pour voir si le joueur a gagné
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Vérifier les lignes
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Vérifier les colonnes
                return True
        # Vérifier les diagonales
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        # Vérifier si toutes les cases sont remplies sans gagnant
        return all(self.board[i][j] != '-' for i in range(3) for j in range(3))

    def disable_buttons(self):
        # Désactiver tous les boutons après la fin du jeu
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset_game(self):
        # Réinitialiser le plateau et les boutons pour recommencer la partie
        self.current_player = random.choice(['X', 'O'])
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)
        self.label.config(text=f"Tour du joueur : {self.current_player}")
        self.play_again_button.grid_remove()  # Cacher le bouton "Rejouer"

    def run(self):
        self.window.mainloop()

# Démarrer le jeu
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
