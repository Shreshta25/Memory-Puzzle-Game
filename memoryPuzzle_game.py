import tkinter as tk
from tkinter import messagebox
import random

class MemoryPuzzleGame:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.buttons = []
        self.board = []
        # Initialize the game board
        self.initialize_board()
        # Create and place buttons on the GUI
        self.create_buttons()

    def initialize_board(self):
        # Generate a list of pairs for the game board
        pairs = [(i // 2) for i in range(self.rows * self.cols)]
        random.shuffle(pairs)
        # Create the game board
        self.board = [pairs[i:i + self.cols] for i in range(0, len(pairs), self.cols)]

    def create_buttons(self):
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                button = tk.Button(self.root, text="", width=5, height=2, command=lambda x=i, y=j: self.flip_card(x, y))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def flip_card(self, row, col):
        # Display the value of the card
        self.buttons[row][col].config(text=str(self.board[row][col]))
        # Check for a match
        if not hasattr(self, 'selected_card'):
            self.selected_card = (row, col)
        else:
            if self.board[row][col] == self.board[self.selected_card[0]][self.selected_card[1]] and (row, col) != self.selected_card:
                # Match found
                messagebox.showinfo("Match", "You found a match!")
                self.buttons[row][col].config(state=tk.DISABLED)
                self.buttons[self.selected_card[0]][self.selected_card[1]].config(state=tk.DISABLED)
            else:
                # No match
                messagebox.showinfo("No Match", "Try again!")
                self.buttons[row][col].config(text="")
                self.buttons[self.selected_card[0]][self.selected_card[1]].config(text="")
            # Reset selected card
            delattr(self, 'selected_card')

# Main function to start the game
def main():
    root = tk.Tk()
    root.title("Memory Puzzle Game")
    # Set the number of rows and columns for the game
    rows = 4
    cols = 4
    # Create the game instance
    game = MemoryPuzzleGame(root, rows, cols)
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
