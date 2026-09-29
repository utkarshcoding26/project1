# Student Performance & Attendance Tracker

It is a Python program for use in the command line which is intended to handle and monitor student performance over terms, sections, and subjects, and does not depend on any external libraries or packages.

---

## 📌 Features

* Support for multiple sections: The system handles student records for five sections (A through E).
* Comprehensive processing of marks: it records and computes the scores for Unit Tests (UT), Class Tests (CT), and Final Exams in the main subjects (Maths, Computer, English, Science, EVS).
* **Attendance Tracking:** It calculates attendance percentages and checks that the required thresholds are met.
**Soft Skills & Conduct:** Gathers and assesses the qualitative soft-skill ratings.
* **Analysis of Progression and Pass/Fail Status:** It automatically calculates the pass/fail status and provides a summary of student performance by term and section.

---

## 🛠️ Built With

* **Python 3** (Pure Standard Library — built without external modules or dependencies)

---

## 🚀 Getting Started

### Prerequisites

Python 3.x has been installed on your machine.

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/utkarshcoding26/project1.git](https://github.com/utkarshcoding26/project1.git)
   cd project1
Run the script:

Bash
python main.py
Usage:
Input the attendance, test scores, and grades for students in each term and section by following the prompts on the interactive console.

⚙️ How It Works
UTmarks_CTmarks_finalmarks1_attendance() gathers the original data relating to unit tests, class tests, final exams, and the total number of days attended. It computes the weighted subject scores and the percentage requirements.

grades(): Checks soft-skill factors and gives conduct grades.

The control flow loops go through each section in order to collect the pass counts and the term reports.
function calling :like def grades also used which is one of the most fascinating concepts of python

Scope of changes:this code can also be reduced using dictionaries and defining function with parameters but this project is to showcase the usage of some concepts to show their usage in real world

Importance:this code will give you a touch of application of coding in real world

The difficulties experienced by the programmer include having to enter the inputs very carefully in order that the threshold value is not passed, for example total marks equal 70 and total sections equal 3.

HELP:code would be very helpful for storing every type of data for multiple students for multiple sections

📜 Author
Utkarsh Agarwal - utkarshcoding26
