from flask import Flask, request, render_template
from surveys import satisfaction_survey, personality_quiz

app = Flask(__name__)
responses = []


@app.route("/")
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    # print(fatisfaction_survey)
    # title = "HELOOOO"
    return render_template(
        "index.html",
        survey_title=title,
        survey_instructions=instructions
        # satisfaction_survey=satisfaction_survey
    )


@app.route("/questions/0")
def show_question():
    question = satisfaction_survey.questions[0].question
    print(question)
    return render_template("question-form.html", 
        question=question
    )

