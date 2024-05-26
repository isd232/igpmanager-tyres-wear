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

        # Check for optional entries
        if 'I' in entries and entries['I'].get():
            tire_wear_rates['I'] = float(entries['I'].get())
        if 'W' in entries and entries['W'].get():
            tire_wear_rates['W'] = float(entries['W'].get())

        for wear_rate in tire_wear_rates.values():
            if wear_rate <= 0 or wear_rate > 100:
                raise ValueError("Wear rate must be between 0 and 100")
    except ValueError as e:
        messagebox.showerror("Błąd", f"Proszę wprowadzić poprawną wartość liczbową dla wszystkich opon. {str(e)}")
        return

    results = {}
    recommendations = {}
    for tire, wear_rate in tire_wear_rates.items():
        x = 100  # Initial tire condition
        i = 0
        tire_results = ""
        recommended_lap = None
        while x > 10:
            z = x * wear_rate / 100
            x -= z
            i += 1
            if x < 50 and recommended_lap is None:
                recommended_lap = i
            if x >= 40:
                tire_results += f"Okrążenie {i}, stan opon {tire}: {x:.2f}%\n"
        results[tire] = tire_results
        recommendations[tire] = recommended_lap if recommended_lap is not None else "No recommendation"

    # Show results in a new window with dynamic text widgets
    result_window = tk.Toplevel()
    result_window.title("Wyniki Zużycia Opon")
    result_window.geometry("800x400")

    # Dynamically create text widgets for each tire type
    for tire, tire_results in results.items():
        frame = tk.Frame(result_window)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text = tk.Text(frame, height=15, width=30)
        text.pack(fill=tk.BOTH, expand=True)
        text.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
        recommendation = f"Zalecana ilość okrążeń dla {tire}: {recommendations[tire]}\n\n"
        text.insert(tk.INSERT, recommendation, "bold")
        text.insert(tk.INSERT, tire_results if tire_results else 'No data')
        text.config(state=tk.DISABLED)


def add_optional_entry(entry_frame, entries, label):
    row = len(entries) + 1
    tk.Label(entry_frame, text=f"Zużycie opon {label} (w procentach):").grid(row=row, column=0, sticky=tk.W)
    entry = tk.Entry(entry_frame)
    entry.grid(row=row, column=1, sticky=tk.W)
    entries[label] = entry


def apply_template(entries, template):
    for tire, value in template.items():
        entries[tire].delete(0, tk.END)
        entries[tire].insert(0, str(value))


def main():
    root = tk.Tk()
    root.title("Kalkulator Zużycia Opon")
    root.geometry("400x400")
    root.resizable(False, False)  # Prevent automatic resizing

    labels = ['SS', 'S', 'M', 'H']
    entries = {}

    # Organize input fields in a grid
    input_frame = tk.Frame(root)
    input_frame.grid(row=0, column=0, padx=20, pady=20)

    for i, label in enumerate(labels):
        tk.Label(input_frame, text=f"Zużycie opon {label} (w procentach):").grid(row=i, column=0, sticky=tk.W)
        entry = tk.Entry(input_frame)
        entry.grid(row=i, column=1, sticky=tk.W)
        entries[label] = entry

    # Buttons to add optional entries
    optional_frame = tk.Frame(root)
    optional_frame.grid(row=1, column=0, padx=20, pady=20)

    tk.Button(optional_frame, text="Dodaj opony I", command=lambda: add_optional_entry(input_frame, entries, 'I')).grid(row=0, column=0, pady=5)
    tk.Button(optional_frame, text="Dodaj opony W", command=lambda: add_optional_entry(input_frame, entries, 'W')).grid(row=0, column=1, pady=5)

    # Buttons to apply templates
    template_frame = tk.Frame(root)
    template_frame.grid(row=2, column=0, padx=20, pady=20)

    tk.Button(template_frame, text="Szablon1", command=lambda: apply_template(entries, {'SS': 11, 'S': 7, 'M': 5, 'H': 4})).grid(row=0, column=0, pady=5)
    tk.Button(template_frame, text="Szablon2", command=lambda: apply_template(entries, {'SS': 12, 'S': 8, 'M': 6, 'H': 4})).grid(row=0, column=1, pady=5)

    tk.Button(root, text="Oblicz Zużycie Opon", command=lambda: oblicz_zuzycie_opon(entries)).grid(row=3, column=0, pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
