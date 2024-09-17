# tic-tac-teo-game
Tic-Tac-Toe Game Web Application
Overview
I have developed a web-based Tic-Tac-Toe/ Tick-Cross game using Flask. The game implements a minimax algorithm with alpha-beta pruning for the AI and includes adjustable difficulty settings.
Key Features
1.	Game Mode Selection:
o	Players can choose between Two-Player Mode or Play with AI. In AI mode, difficulty levels (Easy, Medium, Hard) are available.
2.	Interactive Gameplay:
o	Players engage in real-time matches, either against another player or the AI. Moves are instantly reflected on the board, ensuring a smooth, seamless gaming experience.
3.	AI Opponent:
o	The AI uses an optimized minimax algorithm with alpha-beta pruning for efficient decision-making, offering a more challenging experience in higher difficulty levels.
4.	Winning & Draw Detection:
o	The game automatically detects when a player wins, loses, or when a draw occurs, highlighting winning combinations for clarity.
5.	Game Reset:
o	Players can reset the game board at any point with a button click, starting a new game without needing to refresh the page.
6.	Responsive User Interface:
o	The game board is designed to work smoothly across devices and screen sizes, with color-coded moves that differentiate human from AI interactions.
7.	Error Handling:
o	Invalid moves are handled gracefully, ensuring the game remains smooth and user-friendly even if errors occur.

User Interaction

•	Move Making: Players click on board cells to place their move, and in AI mode, the AI's move follows instantly.
•	Game Mode Selection: Players select between Two-Player and AI Mode, with adjustable difficulty in AI Mode.
•	Difficulty Adjustment: Players can challenge the AI by selecting Easy, Medium, or Hard.
•	Game Reset: A reset button enables starting a new game instantly.

Technical Details

•	Backend: Flask handles game logic, move processing, and difficulty adjustments.
•	AI Algorithm: Minimax with alpha-beta pruning is used to compute the best possible move for the AI.
•	Frontend: HTML, CSS, and JavaScript manage the game board’s appearance and interactivity, ensuring a responsive design and real-time updates.
