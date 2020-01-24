from flask import Flask, request, render_template, redirect
from surveys import satisfaction_survey, personality_quiz

app = Flask(__name__)
form_responses = []
# go off len


@app.route("/")
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template(
        "index.html",
        survey_title=title,
        survey_instructions=instructions
        # satisfaction_survey=satisfaction_survey
    )


@app.route("/questions/<int:question_num>")
def show_question(question_num):
    question = satisfaction_survey.questions[question_num].question
    choices = satisfaction_survey.questions[question_num].choices

    return render_template("question-form.html",
                           question=question,
                           choices=choices,
                           )
    # question_num=question_num


@app.route('/answer', methods=['POST'])
def handle_answer():
    answer = request.form.get('choice')
    form_responses.append(answer)

    # REDIRECT to question/num
    return redirect(f"/questions/{len(form_responses)}")
    # question=question, choices=choices
