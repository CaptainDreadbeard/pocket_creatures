📦 Pocket Creatures
A tiny creature‑raising game written in Python.
Feed them, play with them, watch them grow — and try not to let them burn down your house.

🐉 Overview
Pocket Creatures is a lightweight, terminal‑based virtual pet game.
You choose a creature, interact with it, manage hunger and happiness, and unlock special actions depending on the species.

It’s designed to be:

beginner‑friendly

easy to extend

cleanly structured as a Python package

fun to hack on and customize

Perfect for learning Python classes, modules, imports, and package structure.

🧬 Features
Multiple creature types:

Slime — squishy, friendly, easy to care for

Dragon — powerful, fiery, occasionally destructive

(Add your own creatures easily!)

Persistent save system

ASCII art creature portraits

Simple menu‑based gameplay

Clean modular architecture:

main.py — game entry point

game.py — main game loop

pet.py — base class

slime.py / dragon.py — creature subclasses

save_manager.py — load/save system

ascii_art.py — creature art

📁 Project Structure
Code
pocket_creatures/
│
├── ascii_art.py
├── dragon.py
├── game.py
├── main.py
├── pet.py
├── save_manager.py
├── slime.py
└── __init__.py
▶️ How to Run
From the parent directory (important):

Code
python -m pocket_creatures.main
If your PATH is still being repaired, use your full Python path:

Code
"C:\Users\Robin\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m pocket_creatures.main
🛠️ Requirements
Python 3.10+ (3.14 works great)

No external dependencies

🧩 Extending the Game
Adding a new creature is easy:

Create a new file, e.g. goblin.py

Subclass Pet

Add custom behaviors

Import it in __init__.py

Add it to the creature selection menu in main.py

The project is intentionally simple so you can experiment freely.
