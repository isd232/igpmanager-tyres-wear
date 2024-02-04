import tkinter as tk
from tkinter import simpledialog, messagebox

def oblicz_zuzycie_opon():
    # Zapytanie użytkownika o wartość
    user_input = simpledialog.askstring(title="Zużycie Opon",
                                        prompt="Wprowadź zużycie na okrążenie (w procentach np. 9):")
    if user_input is None:  # Sprawdzanie czy użytkownik nie kliknął "Cancel"
        return
    try:
        y = float(user_input)
    except ValueError:  # Obsługa błędnej wartości
        messagebox.showerror("Błąd", "Proszę wprowadzić poprawną wartość liczbową.")
        return

    x = 100
    i = 0
    results = ""
    while x > 10:
        z = x * y /100
        x = x - z

        i += 1
        results += f"Okrążenie {i}, stan opon: {x:.2f}%\n"

        # Wyświetlanie wyników
    messagebox.showinfo("Wyniki", results)

def main():
    root = tk.Tk()
    root.title("Kalkulator Zużycia Opon")
    root.geometry("300x200")

    tk.Button(root, text="Oblicz Zużycie Opon", command=oblicz_zuzycie_opon).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()