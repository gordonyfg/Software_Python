import os

# Configuration
TOPICS = {
    "Arrays & Strings": ["problem_001_two_sum.py", "problem_242_valid_anagram.py"],
    "Linked Lists": ["problem_206_reverse_linked_list.py"],
    "Trees & Graphs": ["problem_102_binary_tree_level_order_traversal.py"],
    "Sorting & Searching": ["problem_215_kth_largest_element.py"],
    "Dynamic Programming": ["problem_322_coin_change.py"],
}

SOLUTIONS_DIR = "solutions"
PROGRESS_FILE = "progress.md"


def calculate_progress():
    progress = {}
    total_problems = 0
    solved_problems = 0

    for topic, problems in TOPICS.items():
        solved = sum(1 for problem in problems if os.path.exists(os.path.join(SOLUTIONS_DIR, problem)))
        total = len(problems)
        progress[topic] = (solved, total)
        total_problems += total
        solved_problems += solved

    overall_completion = round((solved_problems / total_problems) * 100, 2) if total_problems > 0 else 0
    return progress, overall_completion


def update_progress_file(progress, overall_completion):
    with open(PROGRESS_FILE, "w") as file:
        file.write("# Progress Tracker\n\n")
        file.write("| Topic            | Problems Solved | Total Problems | Completion (%) |\n")
        file.write("|------------------|-----------------|----------------|----------------|\n")
        for topic, (solved, total) in progress.items():
            completion = round((solved / total) * 100, 2) if total > 0 else 0
            file.write(f"| {topic} | {solved} | {total} | {completion}% |\n")
        file.write("\n")
        file.write(f"**Overall Completion:** {overall_completion}%\n")


if __name__ == "__main__":
    progress, overall_completion = calculate_progress()
    update_progress_file(progress, overall_completion)
    print("Progress tracker updated!")
