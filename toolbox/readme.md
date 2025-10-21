# Dominic's Python Toolbox

A collection of Python scripts for generating warranty emails, performing date calculations, and other utilities through a simple menu interface.

## Tools Included

1. Warranty Email Generator - creates ready-to-copy rejection emails for accidental damage or out-of-warranty claims.
2. Date Adder/Subtractor - adds or subtracts a specified number of months from a given date.

## Project Structure

```
toolbox.py           <- Main menu script
framerejection.py    <- Warranty Email Generator
dateaddminus.py      <- Date Adder/Subtractor
venv/                <- Virtual environment (optional)
README.md            <- This file
```

## Setup Instructions

1. Clone the repository:
```
git clone <your-repo-url>
cd <repository-folder>
```

2. Create a virtual environment:
```
python3 -m venv venv
```

3. Activate the virtual environment:
```
source venv/bin/activate
```

4. Install required libraries:
```
pip install python-dateutil
```

## Running the Toolbox

With the virtual environment activated:
```
python toolbox.py
```
- Choose the tool by entering the corresponding number.
- Follow the prompts.
- Press Enter to return to the menu after each tool.

## Adding New Tools

1. Save the new Python script in the same folder.
2. Add a function in `toolbox.py` to run it:
```python
def my_new_tool():
    subprocess.run([sys.executable, "my_new_tool.py"])
    input("\nPress Enter to return to the menu...")
```
3. Add a menu option and corresponding if-statement.

## Notes

- Use the virtual environment to avoid conflicts with system Python.
- Packages installed inside the venv are persistent.
- Deactivate the environment when done:
```
deactivate
```

