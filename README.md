🎮 About
Octogun is a personal Python project inspired by classic arcade shooters. The core mechanic focuses on 8-directional movement (up, down, left, right, and diagonals) with dynamic bullet firing and reactive enemy behaviors.

This game was built for fun, experimentation, and learning. It's also a great example of structuring a game using Python modules like pygame.

🚀 Features
🔁 Full 8-directional movement

🔫 Bullet firing and tracking

👾 Functional enemy AI and tracking

🎯 Collision detection between bullets and enemies

🧠 Clean code architecture with modular Python classes

🛠️ Built With
Python 3.x

Pygame — library for building 2D games

Custom modules: player.py, enemy.py, bullet.py, settings.py

📁 File Structure
bash
Copy
Edit
Octogun/
├── main.py           # Game loop and initialization
├── player.py         # Player class: movement, shooting
├── enemy.py          # Enemy AI and movement
├── bullet.py         # Bullet mechanics
├── settings.py       # Game settings and constants
├── __pycache__/      # Python cache files
└── README.md         # This file
🕹️ How to Play
Install Python 3.8+ if you haven’t already.

Install dependencies:

bash
Copy
Edit
pip install pygame
Run the game:

bash
Copy
Edit
python main.py
Controls:

Move: Arrow keys or WASD

Shoot: Spacebar or auto-fire (based on implementation)
