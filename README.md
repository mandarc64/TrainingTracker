# TrainingTracker

## Overview

TrainingTracker is a Python console application that processes training data from JSON files and generates insightful reports. It focuses on counting training completions, identifying completions within a specific fiscal year, and flagging trainings that are about to expire or have recently expired.

## Features

- **Completion Counts**: Outputs the number of completions for each training.
- **Fiscal Year Completions**: Reports on individuals who completed specified trainings within a defined fiscal year.
- **Expiring Trainings**: Alerts for trainings that are expiring or have expired within a month of a given date.

## Getting Started

### Prerequisites

You need Python 3.6 or higher installed on your machine to run this application.

### Installation

Clone this repository to set up the project on your local machine:

```bash
  git clone https://github.com/mandarc64/TrainingTracker.git
  cd TrainingTracker
```
### Usage

Run the script from the project directory:

```bash
python process_trainings.py
```

## Make sure that the trainings.txt file, which should contain the JSON formatted training data, is located in the root of the project directory.

## Outputs
The application generates three JSON output files:

- **training_completion_counts.json**: Counts of how many people have completed each training.
- **fiscal_year_completions.json**: Details of individuals who completed specified trainings in a given fiscal year.
- **expiring_trainings.json**: Information on individuals with trainings expiring soon or already expired, as of a specified reference date.
