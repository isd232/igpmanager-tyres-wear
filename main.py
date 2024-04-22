import tkinter as tk
from tkinter import messagebox


def oblicz_zuzycie_opon(entries):
    try:
        tire_wear_rates = {
            'SS': float(entries['SS'].get()),
            'S': float(entries['S'].get()),
            'M': float(entries['M'].get()),
            'H': float(entries['H'].get())
        }
        for wear_rate in tire_wear_rates.values():
            if wear_rate <= 0 or wear_rate > 100:
                raise ValueError("Wear rate must be between 0 and 100")
    except ValueError as e:
        messagebox.showerror("Błąd", f"Proszę wprowadzić poprawną wartość liczbową dla wszystkich opon. {str(e)}")
        return

    results = {}
    for tire, wear_rate in tire_wear_rates.items():
        x = 100  # Initial tire condition
        i = 0
        tire_results = ""
        while x > 10:
            z = x * wear_rate / 100
            x -= z
            i += 1
            if x >= 40:
                tire_results += f"Okrążenie {i}, stan opon {tire}: {x:.2f}%\n"
        results[tire] = tire_results

    # Show results in a new window with static text widgets
    result_window = tk.Toplevel()
    result_window.title("Wyniki Zużycia Opon")
    result_window.geometry("600x300")

    # Column 1 for SS and S
    column1 = tk.Frame(result_window)
    column1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    text1 = tk.Text(column1, height=15, width=30)
    text1.pack(fill=tk.BOTH, expand=True)
    text1.insert(tk.INSERT, results.get('SS', 'No data') + "\n\n" + results.get('S', 'No data'))
    text1.config(state=tk.DISABLED)

    # Column 2 for M and H
    column2 = tk.Frame(result_window)
    column2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    text2 = tk.Text(column2, height=15, width=30)
    text2.pack(fill=tk.BOTH, expand=True)
    text2.insert(tk.INSERT, results.get('M', 'No data') + "\n\n" + results.get('H', 'No data'))
    text2.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    root.title("Kalkulator Zużycia Opon")
    root.geometry("300x300")

    labels = ['SS', 'S', 'M', 'H']
    entries = {}

    for label in labels:
        tk.Label(root, text=f"Zużycie opon {label} (w procentach):").pack()
        entry = tk.Entry(root)
        entry.pack()
        entries[label] = entry

    tk.Button(root, text="Oblicz Zużycie Opon", command=lambda: oblicz_zuzycie_opon(entries)).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
