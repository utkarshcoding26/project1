# Student Performance & Attendance Tracker

A command-line Python application designed to process and track student performance across terms, sections, and subjects without relying on external libraries or packages.

---

## 📌 Features

* **Multi-Section Support:** Manages student records across 5 sections (`Section A` to `Section E`).
* **Comprehensive Mark Processing:** Tracks and calculates Unit Tests (UT), Class Tests (CT), and Final Exams across key subjects (*Maths, Computer, English, Science, EVS*).
* **Attendance Tracking:** Computes attendance percentages and validates passing thresholds.
* **Soft Skills & Conduct:** Collects and evaluates qualitative soft-skill ratings.
* **Term Progression & Pass/Fail Analysis:** Automates pass/fail status calculations and summarizes student performance per term and section.

---

## 🛠️ Built With

* **Python 3** (Pure Standard Library — built without external modules or dependencies)

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your machine.

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/utkarshcoding26/project1.git](https://github.com/utkarshcoding26/project1.git)
   cd project1
Run the script:

Bash
python main.py
Usage:
Follow the interactive console prompts to input attendance, test marks, and grades for students across terms and sections.

⚙️ How It Works
UTmarks_CTmarks_finalmarks1_attendance(): Collects raw input for unit tests, class tests, final exams, and total days present. Calculates weighted subject scores and percentage criteria.

grades(): Evaluates soft-skill parameters and conduct grades.

Control Flow Loops: Iterates through each section to aggregate pass counts and term reports.
function calling :like def grades also used which is one of the most fascinating concepts of python

Scope of changes:this code can also be reduced using dictionaries and defining function with parameters but this project is to showcase the usage of some concepts to show their usage in real world

Importance:this code will give you a touch of application of coding in real world

Challenges faced by programmer:it also challenges the programmer to enter the inputs very carefully such that it does not pass the threshold value like total marks=70 and total sections=3 .

📜 Author
Utkarsh Agarwal - utkarshcoding26
