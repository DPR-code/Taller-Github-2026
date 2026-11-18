"""Interfaz con tkinter. Las cuentas viven en calc.core; aquí solo se dibuja."""

import tkinter as tk

from calc.core import OPERATIONS, calculate, format_result, parse_number

BUTTON_COLUMNS = 4
EMPTY_RESULT = "—"
FONT = ("TkDefaultFont", 14)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora ETSIIT Tech Club")
        root.resizable(False, False)

        frame = tk.Frame(root, padx=16, pady=16)
        frame.pack()

        self.entry_a = self._add_input(frame, row=0, label="a")
        self.entry_b = self._add_input(frame, row=1, label="b")

        # Un botón por operación registrada: basta con añadir una entrada
        # a OPERATIONS para que aparezca un botón nuevo aquí.
        first_button_row = 2
        for index, symbol in enumerate(OPERATIONS):
            button = tk.Button(
                frame,
                text=symbol,
                width=5,
                font=FONT,
                command=lambda s=symbol: self.on_operation(s),
            )
            button.grid(
                row=first_button_row + index // BUTTON_COLUMNS,
                column=index % BUTTON_COLUMNS,
                padx=2,
                pady=2,
            )

        next_row = first_button_row + (len(OPERATIONS) - 1) // BUTTON_COLUMNS + 1
        self.result_label = tk.Label(
            frame, text=EMPTY_RESULT, font=("TkDefaultFont", 26, "bold")
        )
        self.result_label.grid(row=next_row, column=0, columnspan=BUTTON_COLUMNS, pady=(12, 0))

        self.status_label = tk.Label(frame, text="", fg="gray")
        self.status_label.grid(row=next_row + 1, column=0, columnspan=BUTTON_COLUMNS)

    def _add_input(self, frame, row, label):
        tk.Label(frame, text=label, font=FONT).grid(row=row, column=0, sticky="e")
        entry = tk.Entry(frame, width=16, font=FONT, justify="right")
        entry.grid(row=row, column=1, columnspan=BUTTON_COLUMNS - 1, pady=4, sticky="we")
        return entry

    def on_operation(self, symbol):
        try:
            a = parse_number(self.entry_a.get())
            b = parse_number(self.entry_b.get())
            result = calculate(a, symbol, b)
        except (ValueError, ZeroDivisionError) as error:
            self.result_label.config(text=EMPTY_RESULT)
            self.status_label.config(text=str(error), fg="red")
            return
        self.result_label.config(text=format_result(result))
        self.status_label.config(text="", fg="gray")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()
