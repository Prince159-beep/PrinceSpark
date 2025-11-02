from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


# ---------- Home ----------
@app.route("/")
def index():
    return render_template("index.html")


# ---------- Register ----------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("quiz.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return "Username already exists!"
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# ---------- Login ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("quiz.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["username"] = username
            # 👑 Special redirect for Prince
            if username.lower() == "prince":
                return redirect(url_for("admin"))
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials!"

    return render_template("login.html")


# ---------- Dashboard ----------
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["username"])


# ---------- Admin ----------
@app.route("/admin")
def admin():
    if "username" not in session or session["username"].lower() != "prince":
        return redirect(url_for("login"))
    return render_template("admin.html", username=session["username"])


# ---------- Difficulty Selection ----------
@app.route("/difficulty")
def difficulty():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("difficulty.html")


# ---------- Quiz ----------
@app.route("/quiz/<difficulty>")
def quiz(difficulty):
    if "username" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT id, question, option1, option2, option3, option4 FROM questions WHERE difficulty=? ORDER BY RANDOM() LIMIT 30", (difficulty,))
    questions = c.fetchall()
    conn.close()

    return render_template("quiz.html", questions=questions, difficulty=difficulty)


# ---------- Submit Quiz ----------
@app.route("/submit_quiz/<difficulty>", methods=["POST"])
def submit_quiz(difficulty):

    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]

    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("SELECT id, answer FROM questions WHERE difficulty=?", (difficulty,))
    answers = {str(row[0]): row[1] for row in c.fetchall()}
    conn.close()

    score = 0
    for qid, correct in answers.items():
        selected = request.form.get(f"q{qid}")
        if selected and int(selected) == int(correct):
            score += 1

    # Save score
    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    c.execute("INSERT INTO scores (username, score, difficulty) VALUES (?, ?, ?)",
              (username, score, difficulty))
    conn.commit()
    conn.close()

    return render_template("result.html", score=score, total=len(answers))


# ---------- Leaderboard ----------
@app.route("/leaderboard")
def leaderboard():
    if "username" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("quiz.db")
    c = conn.cursor()
    # Get top 10 scores per user
    c.execute("""
        SELECT username, MAX(score) as top_score, difficulty 
        FROM scores 
        GROUP BY username 
        ORDER BY top_score DESC 
        LIMIT 10
    """)
    rows = c.fetchall()
    conn.close()

    return render_template("leaderboard.html", rows=rows)


# ---------- Logout ----------
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

# ---------- Change Password ----------
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        username = session["username"]
        current_pw = request.form["current_password"]
        new_pw = request.form["new_password"]
        confirm_pw = request.form["confirm_password"]

        conn = sqlite3.connect("quiz.db")
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        row = c.fetchone()

        # Check if current password is correct
        if not row or row[0] != current_pw:
            conn.close()
            return "❌ Current password is incorrect!"

        # Check if new passwords match
        if new_pw != confirm_pw:
            conn.close()
            return "⚠️ New passwords do not match!"

        # Update new password
        c.execute("UPDATE users SET password=? WHERE username=?", (new_pw, username))
        conn.commit()
        conn.close()

        return "✅ Password changed successfully!"

    return render_template("change_password.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
