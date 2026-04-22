def create_interview_state():
    return {
        "role": "Marketing Intern",
        "asked_questions": [],
        "answers": [],
        "evaluations": [],
        "follow_ups": []
    }


def add_question(state, question):
    state["asked_questions"].append(question)


def add_answer(state, answer):
    state["answers"].append(answer)


def add_evaluation(state, evaluation):
    state["evaluations"].append(evaluation)


def add_follow_up(state, follow_up):
    state["follow_ups"].append(follow_up)