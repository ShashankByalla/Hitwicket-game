# Hitwicket-game
```markdown
# Hitwicket Turn-Based Chess-like Game

This project is a turn-based chess-like game developed as part of the Hitwicket coding challenge. The game uses a server-client architecture with WebSocket-based real-time communication. The server is implemented using Python and Flask, and the client is a simple HTML page.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [How to Play](#how-to-play)
- [License](#license)

## Project Structure

```
hitwicket-game/
│
├── client/
│   └── index.html            # Frontend code for the game
├── server/
│   ├── game_logic.py         # Game logic implementation
│   └── server.py             # WebSocket server handling game state and communication
├── requirements.txt          # Python dependencies
└── venv/                     # Python virtual environment
```

## Features

- **Turn-Based Gameplay**: A two-player turn-based game where players can interact with the board.
- **Real-Time Communication**: Uses WebSocket for real-time updates between server and client.
- **Simple UI**: A minimalistic HTML-based user interface.

## Requirements

- Python 3.7+
- Flask 2.3.2
- websockets 11.0.3
- A modern web browser (e.g., Chrome, Firefox)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd hitwicket-game
```

### 2. Set Up the Python Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the WebSocket Server

Navigate to the `server` directory and run the server:

```bash
cd server
python server.py
```

The server will start on `ws://localhost:8765`.

### 2. Open the Client

Open the `client/index.html` file in your web browser. You can either double-click the file to open it directly or serve it using a local web server.

If you're using Python, you can start a simple HTTP server with:

```bash
cd client
python -m http.server
```

Then, navigate to `http://localhost:8000` in your browser to open the game.

## How to Play

- **Objective**: Players take turns to make moves on a 5x5 grid.
- **Winning Condition**: The simplified example checks if a player occupies the center of the grid.
- **Making a Move**: Click on an empty cell to place your mark (Player 1 or Player 2).
- **Turn Management**: The game will prompt the current player's turn in the UI.

## License

This project is for the Hitwicket coding challenge and is intended for educational purposes. Feel free to use and modify the code as needed.
```

### How to Use This `README.md` File:

1. Replace `<your-repo-url>` with the actual URL of your GitHub repository.
2. Ensure all instructions match the final state of your project.
3. Include any additional information if your game has more features or requirements.

This `README.md` file provides clear instructions for setting up and running the project, making it easy for anyone to get started.
