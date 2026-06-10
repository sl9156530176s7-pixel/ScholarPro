from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

notes = []
tasks = []
goals = []

WELCOME = """
<!DOCTYPE html>
<html>
<head>
<title>ScholarPro</title>
<style>
body{
margin:0;
font-family:Arial;
background:linear-gradient(135deg,#4f46e5,#06b6d4);
height:100vh;
display:flex;
justify-content:center;
align-items:center;
color:white;
text-align:center;
}
.logo{
font-size:100px;
animation:bounce 2s infinite;
}
button{
padding:15px 40px;
font-size:20px;
border:none;
border-radius:30px;
cursor:pointer;
}
@keyframes bounce{
0%,100%{transform:translateY(0);}
50%{transform:translateY(-15px);}
}
</style>
</head>
<body>

<div>
<div class="logo">🧠</div>
<h1>ScholarPro</h1>
<h3>Study Smarter, Achieve More</h3>
<p>Made by Soham Lokhande</p>
<br>
<a href="/home">
<button>ENTER</button>
</a>
</div>

</body>
</html>
"""

HOME = """
<!DOCTYPE html>
<html>
<head>
<title>ScholarPro Dashboard</title>
<style>
body{
font-family:Arial;
background:#f5f5f5;
padding:20px;
}
.card{
background:white;
padding:20px;
margin:20px 0;
border-radius:15px;
box-shadow:0 2px 10px rgba(0,0,0,.2);
}
input,textarea{
width:100%;
padding:10px;
margin:5px 0;
}
button{
padding:10px 20px;
}
h1{
color:#4f46e5;
}
</style>
</head>
<body>

<h1>📚 ScholarPro Dashboard</h1>

<div class="card">
<h2>📝 Add Note</h2>
<form action="/add_note" method="post">
<input name="title" placeholder="Note Title">
<textarea name="content" placeholder="Write note"></textarea>
<button>Add Note</button>
</form>
</div>

<div class="card">
<h2>📚 Notes</h2>
{% for n in notes %}
<h3>{{n.title}}</h3>
<p>{{n.content}}</p>
<hr>
{% endfor %}
</div>

<div class="card">
<h2>📅 Add Timetable Task</h2>
<form action="/add_task" method="post">
<input name="task" placeholder="Monday - Math 5 PM">
<button>Add Task</button>
</form>
</div>

<div class="card">
<h2>📅 Timetable</h2>
<ul>
{% for t in tasks %}
<li>{{t}}</li>
{% endfor %}
</ul>
</div>

<div class="card">
<h2>🎯 Add Study Goal</h2>
<form action="/add_goal" method="post">
<input name="goal" placeholder="Study Python 1 hour daily">
<button>Add Goal</button>
</form>
</div>

<div class="card">
<h2>🎯 Goals</h2>
<ul>
{% for g in goals %}
<li>{{g}}</li>
{% endfor %}
</ul>
</div>

<div class="card">
<h3>👨‍💻 Made by Soham Lokhande</h3>
</div>

</body>
</html>
"""

@app.route("/")
def welcome():
    return WELCOME

@app.route("/home")
def home():
    return render_template_string(
        HOME,
        notes=notes,
        tasks=tasks,
        goals=goals
    )

@app.route("/add_note", methods=["POST"])
def add_note():
    notes.append({
        "title": request.form["title"],
        "content": request.form["content"]
    })
    return redirect("/home")

@app.route("/add_task", methods=["POST"])
def add_task():
    tasks.append(request.form["task"])
    return redirect("/home")

@app.route("/add_goal", methods=["POST"])
def add_goal():
    goals.append(request.form["goal"])
    return redirect("/home")
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)