from flask import Flask, request, render_template, redirect, url_for, flash, session
from surveys import satisfaction_survey, personality_quiz

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

form_responses = []


@app.route("/")
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template(
        "index.html",
        survey_title=title,
        survey_instructions=instructions
    )


@app.route('/begin', methods=['POST'])
def begin():
    session['responses'] = []
    return redirect('/questions/0')


@app.route("/questions/<int:question_num>")
def show_question(question_num):
    form_responses = session.get('responses')

    if len(form_responses) != question_num:
        flash('You are accessing an invalid question!')
        return redirect(f"/questions/{len(form_responses)}")

    if len(form_responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')

    question = satisfaction_survey.questions[question_num].question
    choices = satisfaction_survey.questions[question_num].choices

    return render_template("question-form.html",
                           question=question,
                           choices=choices,
                           )


@app.route('/answer', methods=['POST'])
def handle_answer():
    answer = request.form.get('choice')
    # form_responses.append(answer)

    form_responses = session['responses']
    form_responses.append(answer)
    session['responses'] = form_responses

    if len(form_responses) == len(satisfaction_survey.questions):
        return redirect('/thanks')

    return redirect(f"/questions/{len(form_responses)}")


@app.route("/thanks")
def thanks():

    return render_template(
        "thanks.html")
