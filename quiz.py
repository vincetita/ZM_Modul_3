####ast

import tkinter as tk
from tkinter import ttk, messagebox
import random

# Quizfragen und Antworten
quiz_fragen = [
    {
        "frage": "Was ist der Unterschied zwischen '==' und 'is' in Python?",
        "optionen": [
            "A) '==' vergleicht Werte, 'is' vergleicht Objekt-Identität",
            "B) 'is' vergleicht Werte, '==' vergleicht Objekt-Identität",
            "C) Beide sind identisch",
            "D) 'is' existiert nicht in Python"
        ],
        "antwort": "A"
    },
    {
        "frage": "Was gibt [x**2 for x in range(5)] zurück?",
        "optionen": [
            "A) [0, 1, 4, 9, 16]",
            "B) [1, 4, 9, 16, 25]",
            "C) [0, 1, 2, 3, 4]",
            "D) Fehler"
        ],
        "antwort": "A"
    },
    {
        "frage": "Wie funktioniert die Methode .get() bei Dictionaries?",
        "optionen": [
            "A) Gibt den Wert für einen Schlüssel zurück oder None",
            "B) Löscht einen Schlüssel",
            "C) Fügt einen neuen Schlüssel hinzu",
            "D) Konvertiert das Dictionary zu einer Liste"
        ],
        "antwort": "A"
    },
    {
        "frage": "Was ist der Output von bool([])?",
        "optionen": [
            "A) True",
            "B) False",
            "C) None",
            "D) Error"
        ],
        "antwort": "B"
    },
    {
        "frage": "Welche Aussage über Lambda-Funktionen ist korrekt?",
        "optionen": [
            "A) Können nur einen Parameter haben",
            "B) Müssen immer einen Namen haben",
            "C) Können mehrere Ausdrücke enthalten",
            "D) Sind auf einen Ausdruck beschränkt"
        ],
        "antwort": "D"
    }
]

# Initialisierung der App
root = tk.Tk()
root.title("Python Quiz")
root.geometry("500x400")

# Punkte-Tracker
punkte = 0
frage_index = 0
ausgewählte_fragen = random.sample(quiz_fragen, len(quiz_fragen))  # Fragen mischen

def überprüfe_antwort(auswahl):
    global frage_index, punkte
    richtige_antwort = ausgewählte_fragen[frage_index]["antwort"]
    
    if auswahl == richtige_antwort:
        punkte += 1
        messagebox.showinfo("Ergebnis", "✅ Richtig!")
    else:
        messagebox.showerror("Ergebnis", f"❌ Falsch! Richtige Antwort: {richtige_antwort}")
    
    frage_index += 1
    if frage_index < len(ausgewählte_fragen):
        lade_frage()
    else:
        messagebox.showinfo("Quiz beendet", f"Dein Punktestand: {punkte}/{len(quiz_fragen)}")
        root.quit()

def lade_frage():
    frage = ausgewählte_fragen[frage_index]
    frage_label.config(text=frage["frage"])

    for i in range(4):
        buttons[i].config(text=frage["optionen"][i], command=lambda opt=chr(65+i): überprüfe_antwort(opt))

# UI-Elemente
frage_label = ttk.Label(root, text="", font=("Arial", 14), wraplength=450)
frage_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = ttk.Button(root, text="", width=40)
    btn.pack(pady=5)
    buttons.append(btn)

# Erste Frage laden
lade_frage()

# App starten
root.mainloop()
