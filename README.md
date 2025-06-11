# Ideal_Gas_Laws_Solver
This repository hosts the script that I wrote to solve word problems that are pasted into it. It is used specifically to solve ideal gas law problems that utilize the PV=nRT formula.

This script will take a text that is copied and pasted into the console and parse it out to find the correct values to assign to the corresponding variables from the formula listed above.
Units may be written immediately after numbers (e.g. `23C`) or separated by a space.

It will then solve for the missing variable.

## Usage
Run the calculator from the command line:

```bash
python Ideal_Gas_Laws_Calculator.py
```

After launching, paste an ideal gas law word problem at the prompt. For example:

```text
What volume of CO2 is needed to fill an 0.5 moles tank to a pressure of 150.0 atm at 27.0 Celsius?
```

The program parses the question, displays the values it detected and prints the answer:

```text
Welcome to the ideal gas laws calculator!
Copy and paste the Ideal Gas Law problem here that you want answered.
(Units can be written with or without a space, e.g. 23C or 23 C)
temperature is equal to 300.0 Kelvin
pressure is equal to 150.0 atm
mass is equal to 0.5 moles
The answer is 0.0821 Liters
```

## Running Tests
Install `pytest` and run the test suite from the repository root:

```bash
pytest
```

