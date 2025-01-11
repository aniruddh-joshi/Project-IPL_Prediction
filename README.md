# Project-IPL_Prediction
🏏 **IPL Winning Team Prediction**: A smart web app that uses machine learning to predict IPL match winners based on real-time stats and historical data! 📊⚡

## 🎥 Demo
![Image 1](image1.png) ![Image 2](image2.png)


---

## 📋 Project Goals
- **Predict IPL Match Winners**: Use historical match data and real-time stats to calculate probabilities.
- **User-Friendly Web App**: A sleek Flask-based interface for interactive predictions.
- **Deploy for Public Access**: Share predictions with the world via Render.

---

## 🔍 Features
### 1. Model Training
- **Algorithms Used**:
  - Logistic Regression
  - Random Forest Classifier (🌟 Best with 99% accuracy)
  - Gradient Boosting Classifier
- **Key Features in the Model**:
  - **Team Details**: BattingTeam, BowlingTeam
  - **Match Stats**: Runs left, Balls left, Wickets remaining
  - **Targets**: Target Runs, Current Run Rate (CRR), Required Run Rate (RRR)
  - **Match Metadata**: Venue, Toss Winner

### 2. Web Application
- **Input**: Match details like teams, venue, and in-match stats.
- **Output**: Probabilities of each team winning, displayed as progress bars for visual clarity.
- **Real-time and interactive predictions!** 🚀

---

## 🗂️ Repository Structure
| File/Directory                         | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `app.py`                               | Flask application handling user input and prediction results.               |
| `templates/`                           | Folder containing HTML templates.                                           |
| `templates/index.html`                 | Homepage where users can input match details.                               |
| `templates/result.html`                | Result page displaying prediction probabilities and outcomes.               |
| `static/`                              | Folder containing static assets (CSS and images).                           |
| `static/style.css`                     | General styling of the web application.                                     |
| `static/restyle.css`                   | Styling for the result page (`result.html`).                                |
| `static/background-img.webp`           | Background image for the web application's HTML pages.                      |
| `model.pkl`                            | Serialized trained machine learning model used in the Flask app.            |
| `requirements.txt`                     | List of Python dependencies required to run the project.                    |
| `Final_IPL_winner_prediction.ipynb`    | Jupyter Notebook containing the model training code.                        |
| `all_season_details.zip`               | Dataset containing detailed historical IPL match data.                      |
| `all_season_summary.zip`               | Dataset containing summary statistics of IPL matches.                       |
| `README.md`                            | Project documentation and setup guidelines.                                 |

---

## 🧑‍💻 Technologies Used

### Languages and Libraries:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit

---

## 🚀 Future Work
- **Expand Dataset**: Incorporate more seasons and detailed player statistics.
- **Advanced Modeling**: Explore deep learning models for prediction tasks.
- **Real-time Data**: Implement real-time data fetching and model updating.
- **Enhanced UI**: Develop a more interactive and user-friendly interface with dashboards.

---

## ⚠️ Disclaimer
This project is for educational purposes as part of an internship program. The data and analyses are based on available IPL datasets and are intended to demonstrate data analytics and visualization techniques.

---
