from questions import MARKETING_QUESTIONS
from evaluator import evaluate_answer
from state import add_question, add_answer, add_evaluation, add_follow_up


def ask_question(question_text: str) -> str:
    print("\n" + "-" * 60)
    print("Question:")
    print(question_text)
    print("-" * 60)
    return input("Your answer: ").strip()


def print_evaluation(evaluation: dict):
    print("\nEvaluation Summary:")
    print(f"Relevance: {evaluation.get('relevance')}/10")
    print(f"Clarity: {evaluation.get('clarity')}/10")
    print(f"Creativity: {evaluation.get('creativity')}/10")
    print(f"Communication: {evaluation.get('communication')}/10")
    print(f"Overall Score: {evaluation.get('overall_score')}/10")

    print("Strengths:")
    strengths = evaluation.get("strengths", [])
    if strengths:
        for item in strengths:
            print("-", item)
    else:
        print("- None identified")

    print("Weaknesses:")
    weaknesses = evaluation.get("weaknesses", [])
    if weaknesses:
        for item in weaknesses:
            print("-", item)
    else:
        print("- None identified")


def run_interview(state: dict):
    print("\nWelcome to the AI Marketing Interview Agent")

    MAX_QUESTIONS = 5

    for i, question_data in enumerate(MARKETING_QUESTIONS):
        if i >= MAX_QUESTIONS:
            break

        add_question(state, question_data)

        answer = ask_question(question_data["question"])
        add_answer(state, answer)

        evaluation = evaluate_answer(
            topic=question_data["topic"],
            question=question_data["question"],
            answer=answer
        )
        add_evaluation(state, evaluation)

        print_evaluation(evaluation)

        if evaluation.get("follow_up_needed") and evaluation.get("follow_up_question"):
            follow_up_q = evaluation["follow_up_question"]
            print("\nFollow-up Question:")
            print(follow_up_q)

            follow_up_answer = input("Your follow-up answer: ").strip()

            add_follow_up(state, {
                "topic": question_data["topic"],
                "question": follow_up_q,
                "answer": follow_up_answer
            })

    return state