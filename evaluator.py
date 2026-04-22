import json
import ollama

EVALUATION_SCHEMA = {
    "type": "object",
    "properties": {
        "topic": {"type": "string"},
        "relevance": {"type": "integer"},
        "clarity": {"type": "integer"},
        "creativity": {"type": "integer"},
        "communication": {"type": "integer"},
        "overall_score": {"type": "integer"},
        "strengths": {
            "type": "array",
            "items": {"type": "string"}
        },
        "weaknesses": {
            "type": "array",
            "items": {"type": "string"}
        },
        "follow_up_needed": {"type": "boolean"},
        "follow_up_question": {"type": "string"}
    },
    "required": [
        "topic",
        "relevance",
        "clarity",
        "creativity",
        "communication",
        "overall_score",
        "strengths",
        "weaknesses",
        "follow_up_needed",
        "follow_up_question"
    ]
}


def evaluate_answer(topic: str, question: str, answer: str) -> dict:
    prompt = f"""
You are a strict but fair marketing interviewer.

Evaluate the candidate's answer for a Marketing Intern interview.

Question: {question}
Answer: {answer}

Scoring rules:
- relevance: how well the answer addresses the question
- clarity: how clearly the answer is written
- creativity: how thoughtful or original the answer is
- communication: how professionally the answer is expressed
- overall_score: overall quality from 0 to 10

Be realistic. Do not give high scores unless clearly deserved.
Keep strengths and weaknesses short.
If the answer is too brief, vague, or missing examples, set follow_up_needed to true.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}],
        format=EVALUATION_SCHEMA,
        options={
            "temperature": 0.1
        }
    )

    return json.loads(response["message"]["content"])