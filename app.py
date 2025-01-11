from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load your trained model
try:
    model = pickle.load(open("ipl_pred_model.pkl", "rb"))
except FileNotFoundError:
    model = None  # Handle missing model during testing
    print("Warning: Model file not found!")

# Team color mapping
TEAM_COLORS = {
    "KKR": "purple",
    "CSK": "yellow",
    "SRH": "orange",
    "RR": "pink",
    "MI": "blue",
    "RCB": "red",
    "KXIP": "red",
    "DC": "blue",
    "LSG": "lightblue",
    "GT": "darkblue"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form data
        batting_team = request.form.get("batting_team", "Unknown Batting Team")
        bowling_team = request.form.get("bowling_team", "Unknown Bowling Team")
        runs_scored = int(request.form.get("runs_scored", 0))
        wickets_down = int(request.form.get("wickets_down", 0))
        current_over = int(request.form.get("current_over", 0))
        current_ball = int(request.form.get("current_ball", 0))
        target_runs = int(request.form.get("target_runs", 0))
        toss_winner = request.form.get("toss_winner", "Unknown Toss Winner")
        venue = request.form.get("venue", "Unknown Venue")

        # Derived features
        balls_left = 120 - (current_over * 6 + current_ball)
        wickets_remaining = 10 - wickets_down
        runs_left = target_runs - runs_scored
        crr = round(runs_scored / (current_over + current_ball / 6),2) if (current_over + current_ball / 6) > 0 else 0
        rrr = round(runs_left / (balls_left / 6),2) if balls_left > 0 else 0

        # Input DataFrame for the model
        input_data = pd.DataFrame({
            'BattingTeam': [batting_team],
            'BowlingTeam': [bowling_team],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets_remaining': [wickets_remaining],
            'target_runs': [target_runs],
            'crr': [crr],
            'rrr': [rrr],
            'toss_winner': [toss_winner],
            'venue': [venue]
        })

        # Dummy prediction for testing if model isn't available
        if model:
            prediction = model.predict_proba(input_data)
            batting_team_prob = round(prediction[0][1] * 100, 2)  # Probability for Batting Team
            bowling_team_prob = round(prediction[0][0] * 100, 2)  # Probability for Bowling Team
        else:
            batting_team_prob = 60.0  # Test data
            bowling_team_prob = 40.0  # Test data

        # Determine the outcome
        outcome = (
            f"{batting_team} are likely to win!"
            if batting_team_prob > bowling_team_prob
            else f"{bowling_team} are likely to win!"
        )

        # Team colors
        team_colors = {
            "KKR": "KKR",
            "CSK": "CSK",
            "SRH": "SRH",
            "RR": "RR",
            "MI": "MI",
            "RCB": "RCB",
            "KXIP": "KXIP",
            "DC": "DC",
            "LSG": "LSG",
            "GT": "GT"
        }
        batting_team_color = team_colors.get(batting_team, "default")
        bowling_team_color = team_colors.get(bowling_team, "default")

        return render_template(
            "result.html",
            batting_team=batting_team,
            bowling_team=bowling_team,
            prediction_text=batting_team_prob,
            prediction_text2=bowling_team_prob,
            prediction_outcome=outcome,
            batting_team_color=batting_team_color,
            bowling_team_color=bowling_team_color
        )
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "An error occurred. Check your input and try again.",500

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
