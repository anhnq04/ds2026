# Lab 7 - Sudoku Game on Google App Engine

## Overview
A web-based Sudoku game built with Flask and deployed on Google App Engine.

## Files
- `main.py` - Flask backend application
- `app.yaml` - GAE configuration
- `requirements.txt` - Python dependencies
- `templates/index.html` - Game UI
- `07.sudoku.tex` - LaTeX report

## Features
- 🎮 Interactive 9x9 Sudoku grid
- 🎯 Three difficulty levels (Easy, Medium, Hard)
- ✅ Real-time board validation
- 🎨 Modern gradient UI design
- 📱 Mobile responsive
- ☁️ Cloud-hosted on Google App Engine

## Requirements
- Python 3.9+
- Flask 2.3.0
- gunicorn 21.2.0
- Google Cloud SDK (for deployment)

## Local Development

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python main.py
```

### 3. Open Browser
Navigate to `http://localhost:8080`

## Deploy to Google App Engine

### 1. Install Google Cloud SDK
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

### 2. Initialize gcloud
```bash
gcloud init
```

### 3. Create Project
```bash
gcloud projects create sudoku-game-YOUR-PROJECT-ID
gcloud config set project sudoku-game-YOUR-PROJECT-ID
```

### 4. Enable App Engine
```bash
gcloud app create --region=us-central
```

### 5. Deploy
```bash
gcloud app deploy
```

### 6. View Application
```bash
gcloud app browse
```

## How to Play

1. **Select Difficulty**: Choose Easy (30 cells), Medium (40 cells), or Hard (50 cells)
2. **New Game**: Click "New Game" to generate a new puzzle
3. **Fill Numbers**: Click on empty cells and enter numbers 1-9
4. **Validate**: Click "Validate" to check if your solution is correct
5. **Clear**: Click "Clear" to remove all your entries (keeps original puzzle)

## Game Logic

### Sudoku Generator
- Uses backtracking algorithm to generate complete board
- Removes cells based on difficulty level
- Ensures unique solution

### Validation Rules
- Each row must contain digits 1-9 without repetition
- Each column must contain digits 1-9 without repetition
- Each 3x3 box must contain digits 1-9 without repetition

## API Endpoints

### `GET /`
Serves the game UI (index.html)

### `POST /generate`
Generates a new Sudoku puzzle

**Request:**
```json
{
  "difficulty": 40
}
```

**Response:**
```json
{
  "board": [[5,3,0,...], [6,0,0,...], ...]
}
```

### `POST /validate`
Validates the current board state

**Request:**
```json
{
  "board": [[5,3,4,...], [6,7,2,...], ...]
}
```

**Response:**
```json
{
  "valid": true,
  "message": "Board is valid!"
}
```

## Project Structure

```
Lab7/
├── main.py                 # Flask app with game logic
├── app.yaml                # GAE configuration
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Game UI with CSS/JS
└── 07.sudoku.tex          # LaTeX report
```

## GAE Configuration

- **Runtime**: Python 3.9
- **Instance Class**: F1 (256MB RAM, 600MHz CPU)
- **Auto-scaling**: 1-10 instances
- **Target CPU**: 65%

## Cost Estimation

Google App Engine Free Tier includes:
- 28 instance hours per day
- 1 GB outbound data per day
- 5 GB Cloud Storage

This Sudoku app should stay within free tier for moderate usage.

## Troubleshooting

### Local Development Issues

**Port already in use:**
```bash
# Change port in main.py
app.run(host='0.0.0.0', port=8081, debug=True)
```

**Module not found:**
```bash
pip install -r requirements.txt
```

### Deployment Issues

**gcloud not found:**
```bash
# Reinstall Google Cloud SDK
curl https://sdk.cloud.google.com | bash
```

**Deployment fails:**
```bash
# Check app.yaml syntax
# Ensure requirements.txt is correct
# Check project billing is enabled
```

**App won't start:**
```bash
# Check logs
gcloud app logs tail -s default
```

## Features Breakdown

### Backend (Flask)
- Sudoku generation algorithm
- Board validation logic
- RESTful API endpoints
- Error handling

### Frontend (HTML/CSS/JS)
- Responsive grid layout
- Gradient background design
- Interactive cell input
- AJAX API calls
- Success/error messages

### Cloud (GAE)
- Automatic scaling
- Load balancing
- SSL/HTTPS
- Global CDN
- Zero server management

## Future Enhancements
- [ ] Save game progress
- [ ] Hint system
- [ ] Timer and scoring
- [ ] Multiplayer mode
- [ ] Leaderboard
- [ ] Daily challenges
- [ ] Undo/Redo functionality

## License
Educational project for Distributed Systems course.
