from state import create_interview_state
from interviewer import run_interview
from report import generate_final_report, print_final_report


def main():
    state = create_interview_state()
    updated_state = run_interview(state)
    report = generate_final_report(updated_state)
    print_final_report(report)


if __name__ == "__main__":
    main()