import json
import os
import random

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
    files = ['fragen.json', 'fragen2.json', 'fragen3.json', 'fragen4.json', 'fragen5.json']
    questions = load_questions(files)
    
    if not questions:
        print("No questions loaded. Exiting.")
        return

    # Shuffle for variety
    random.shuffle(questions)
    
    total_points = 0
    max_points = 0
    
    print(f"\nStarte das Quiz mit {len(questions)} Fragen!")
    print("-" * 50)
    
    for i, q in enumerate(questions, 1):
        print(f"\nFrage {i}: {q.get('question', 'No Question Text')}")
        
        options = q.get('options', {})
        sorted_keys = sorted(options.keys())
        for key in sorted_keys:
            print(f"  {key}) {options[key]}")
            
        points = q.get('points', 1.0)
        correct_answers = set(q.get('correct', []))
        max_points += points
        
        # User input handling
        user_input = input("\nDeine Antwort(en) (z.B. 'a' oder 'a, c'): ").lower()
        
        # Parse inputs like "a,b" or "a b"
        user_answers = set([x.strip() for x in user_input.replace(',', ' ').split() if x.strip()])
        
        if user_answers == correct_answers:
            print(f"Richtig! (+{points} Punkte)")
            total_points += points
        else:
            correct_str = ", ".join(sorted(list(correct_answers)))
            print(f"Falsch. Richtige Antwort(en): {correct_str}")
            
        print("-" * 30)
        
    print(f"\nQuiz beendet!")
    print(f"Ergebnis: {total_points} von {max_points} Punkten.")

if __name__ == "__main__":
    run_quiz()
