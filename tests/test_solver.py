import builtins
import importlib
import os
import sys

import pytest


# Example 2 test: solve for temperature

def test_example2(monkeypatch, capsys):
    question = (
        "If I have 4 moles of gas at a pressure of 5.6 atm and a volume of 12 Liters, what is the temperature?"
    )
    monkeypatch.setattr(builtins, "input", lambda _: question)
    monkeypatch.setattr("time.sleep", lambda _ : None)

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    import Ideal_Gas_Laws_Calculator
    importlib.reload(Ideal_Gas_Laws_Calculator)

    Ideal_Gas_Laws_Calculator.calculator()
    output = capsys.readouterr().out.strip().splitlines()
    assert output[-1] == "The answer is 204.62850182704014 Kelvin"


# Example 3 test: solve for temperature

def test_example3(monkeypatch, capsys):
    question = (
        "At what temperature would 2.10 moles of N2 gas have a pressure of 1.25 atm and in a 25.0 L tank?"
    )
    monkeypatch.setattr(builtins, "input", lambda _: question)
    monkeypatch.setattr("time.sleep", lambda _ : None)

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    import Ideal_Gas_Laws_Calculator
    importlib.reload(Ideal_Gas_Laws_Calculator)

    Ideal_Gas_Laws_Calculator.calculator()
    output = capsys.readouterr().out.strip().splitlines()
    assert output[-1] == "The answer is 181.25398758772693 Kelvin"
