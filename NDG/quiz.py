import json
import os
import random

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def load_questions(filenames):
    all_questions = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for filename in filenames:
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    questions = json.load(f)
                    if isinstance(questions, list):
                        all_questions.extend(questions)
                        print(f"Loaded {len(questions)} questions from {filename}")
                    else:
                        print(f"Warning: Content of {filename} is not a list.")
            except Exception as e:
                print(f"Error loading {filename}: {e}")
        else:
            print(f"File not found: {filename}")
            
    return all_questions

def run_quiz():
    files = ['fragen.json', 'fragen2.json', 'fragen3.json', 'fragen4.json', 'fragen5.json', 'fragen6.json', 'fragen7.json']
    questions = load_questions(files)
    
    if not questions:
        print("No questions loaded. Exiting.")
        return

    # Shuffle for variety
    random.shuffle(questions)
    
    total_points = 0
    max_points = 0
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}Starte das Quiz mit {len(questions)} Fragen!{Colors.ENDC}")
    print(f"{Colors.HEADER}" + "-" * 50 + f"{Colors.ENDC}")
    
    for i, q in enumerate(questions, 1):
        print(f"\n{Colors.CYAN}{Colors.BOLD}Frage {i}: {q.get('question', 'No Question Text')}{Colors.ENDC}")
        
        options = q.get('options', {})
        sorted_keys = sorted(options.keys())
        for key in sorted_keys:
            print(f"  {Colors.BLUE}{key}){Colors.ENDC} {options[key]}")
            
        points = q.get('points', 1.0)
        correct_answers = set(q.get('correct', []))
        max_points += points
        
        # User input handling
        user_input = input(f"\n{Colors.YELLOW}Deine Antwort(en) (z.B. 'a' oder 'a, c'): {Colors.ENDC}").lower()
        
        # Parse inputs like "a,b" or "a b"
        user_answers = set([x.strip() for x in user_input.replace(',', ' ').split() if x.strip()])
        
        if user_answers == correct_answers:
            print(f"{Colors.GREEN}{Colors.BOLD}Richtig! (+{points} Punkte){Colors.ENDC}")
            total_points += points
        else:
            correct_str = ", ".join(sorted(list(correct_answers)))
            print(f"{Colors.RED}{Colors.BOLD}Falsch.{Colors.ENDC} Richtige Antwort(en): {Colors.GREEN}{correct_str}{Colors.ENDC}")
            
        print(f"{Colors.HEADER}" + "-" * 30 + f"{Colors.ENDC}")
        
    print(f"\n{Colors.HEADER}Quiz beendet!{Colors.ENDC}")
    print(f"{Colors.BOLD}Ergebnis: {total_points} von {max_points} Punkten.{Colors.ENDC}")

if __name__ == "__main__":
    run_quiz()
