def generate_final_report(state: dict) -> dict:
    evaluations = state.get("evaluations", [])

    if not evaluations:
        return {
            "average_score": 0,
            "verdict": "No interview data found.",
            "strengths": [],
            "weaknesses": []
        }

    total = sum(item.get("overall_score", 0) for item in evaluations)
    avg = round(total / len(evaluations), 2)

    # Collect strengths & weaknesses
    strengths = []
    weaknesses = []

    for item in evaluations:
        strengths.extend(item.get("strengths", []))
        weaknesses.extend(item.get("weaknesses", []))

    # Remove duplicates
    strengths = list(set(strengths))
    weaknesses = list(set(weaknesses))

    # Verdict logic
    if avg >= 8:
        verdict = "Strong Candidate"
        recommendation = "Ready for interviews. Keep refining advanced concepts."
    elif avg >= 6:
        verdict = "Moderate Fit"
        recommendation = "Good base, but needs improvement in clarity and depth."
    else:
        verdict = "Needs Improvement"
        recommendation = "Work on fundamentals, structured answers, and real-world examples."

    return {
        "average_score": avg,
        "verdict": verdict,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendation": recommendation
    }


def print_final_report(report: dict):
    print("\n" + "=" * 60)
    print("📊 FINAL INTERVIEW REPORT")
    print("=" * 60)

    print(f"\nAverage Score : {report['average_score']}/10")
    print(f"Verdict       : {report['verdict']}")

    print("\nTop Strengths:")
    if report["strengths"]:
        for s in report["strengths"]:
            print(f"- {s}")
    else:
        print("- No major strengths identified")

    print("\nAreas to Improve:")
    if report["weaknesses"]:
        for w in report["weaknesses"]:
            print(f"- {w}")
    else:
        print("- No major weaknesses identified")

    print("\nRecommendation:")
    print(report["recommendation"])

    print("\n" + "=" * 60)