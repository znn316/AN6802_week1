from flask import Flask, render_template, request
import joblib
import os
from groq import Groq

model = joblib.load("foodexp.pkl")
#model.predict([[5000]])
#os.environ["GROQ_API_KEY"] = ""
#client = Groq()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
app = Flask(__name__)

@app.route("/", methods=["get","post"])
def index():
    return(render_template("index.html"))

@app.route('/main', methods=['get','post'])
def main():   
    return (render_template('main.html') )

@app.route('/ethics', methods=['get','post'])
def ethics():   
    return (render_template('ethics.html') )

@app.route("/wrong", methods=["GET", "POST"])
def wrong():
    return render_template("wrong.html")


@app.route("/correct", methods=["GET", "POST"])
def correct():
    return render_template("correct.html")

@app.route('/econ', methods=['get','post'])
def econ():   
    return (render_template('econ.html') )

@app.route("/foodExp",methods=["get","post"])
def foodExp():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    return(render_template("foodExp.html",r=r[0][0]))

@app.route("/chatbot",methods=["get","post"])
def chatbot():
    return(render_template("chatbot.html"))

@app.route("/roe",methods=["get","post"])
def roe():
    r = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {"role": "system", "content": "Please explain RoE in 20 words"}
        ]
    )
    return(render_template("roe.html",r=r.choices[0].message.content))

@app.route("/generalQuestion",methods=["get","post"])
def generalQuestion():
    return(render_template("generalQuestion.html"))

@app.route("/groqReply",methods=["get","post"])
def groqReply():
    q = request.form.get("q")
    r = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {"role": "system", "content": q}
        ]
    )
    return(render_template("groqReply.html",r=r.choices[0].message.content))

@app.route("/equity",methods=["get","post"])
def equity():
    return(render_template("equity.html"))

@app.route("/apple",methods=["get","post"])
def apple():
    return(render_template("apple.html"))

if __name__=="__main__":
    app.run()