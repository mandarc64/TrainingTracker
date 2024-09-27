import json
from collections import defaultdict
from datetime import datetime

# Helper function to read data from a file
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to count completed trainings
def count_trainings(data):
    training_count = defaultdict(int)
    for person in data:
        seen_trainings = set()
        for training in person['completions']:
            if training['name'] not in seen_trainings:
                seen_trainings.add(training['name'])
                training_count[training['name']] += 1
    return training_count

# Function to find completions in a specific fiscal year
def trainings_in_fiscal_year(data, trainings, year):
    start_date = datetime(year - 1, 7, 1)
    end_date = datetime(year, 6, 30)
    results = {training: [] for training in trainings}

    for person in data:
        for completion in person['completions']:
            if completion['name'] in trainings:
                completion_date = datetime.strptime(completion['timestamp'], '%m/%d/%Y')
                if start_date <= completion_date <= end_date:
                    results[completion['name']].append(person['name'])
    return results

# Function to find expired or soon-to-expire trainings
def trainings_expiring_soon(data, reference_date):
    reference_datetime = datetime.strptime(reference_date, '%b %d, %Y')
    results = {}

    for person in data:
        person_results = []
        for training in person['completions']:
            if training['expires']:
                expires_datetime = datetime.strptime(training['expires'], '%m/%d/%Y')
                if expires_datetime < reference_datetime:
                    status = 'expired'
                elif (expires_datetime - reference_datetime).days <= 30:
                    status = 'expires soon'
                else:
                    continue
                person_results.append({
                    "name": training['name'],
                    "status": status
                })
        if person_results:
            results[person['name']] = person_results
    return results

# Main function to run your application
def main():
    data = read_data('trainings.txt')

    # Task 1: Count of completions per training
    completion_counts = count_trainings(data)
    with open('training_completion_counts.json', 'w') as file:
        json.dump(completion_counts, file, indent=4)

    # Task 2: Completions within a specific fiscal year
    fiscal_year_trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    fiscal_year = 2024
    fy_completions = trainings_in_fiscal_year(data, fiscal_year_trainings, fiscal_year)
    with open('fiscal_year_completions.json', 'w') as file:
        json.dump(fy_completions, file, indent=4)

    # Task 3: Expiring trainings
    check_date = 'Oct 1, 2023'
    expiring_trainings = trainings_expiring_soon(data, check_date)
    with open('expiring_trainings.json', 'w') as file:
        json.dump(expiring_trainings, file, indent=4)

if __name__ == "__main__":
    main()
