import builtins
import importlib
import os
import sys

import pytest


def test_calculator(monkeypatch, capsys):
    question = (
        "What volume of CO2 is needed to fill an 0.5 moles tank to a pressure of 150.0 atm at 27.0 Celsius?"
    )
    monkeypatch.setattr(builtins, "input", lambda _: question)
    monkeypatch.setattr("time.sleep", lambda _ : None)

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    import Ideal_Gas_Laws_Calculator
    importlib.reload(Ideal_Gas_Laws_Calculator)

    Ideal_Gas_Laws_Calculator.calculator()
    output = capsys.readouterr().out.strip().splitlines()
    assert output[-1] == "The answer is 0.08214105 Liters"


def test_calculator_concatenated_units(monkeypatch, capsys):
    question = (
        "What volume of CO2 is needed to fill an 0.5moles tank to a pressure of 150.0atm at 27C?"
    )
    monkeypatch.setattr(builtins, "input", lambda _: question)
    monkeypatch.setattr("time.sleep", lambda _ : None)

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    import Ideal_Gas_Laws_Calculator
    importlib.reload(Ideal_Gas_Laws_Calculator)

    Ideal_Gas_Laws_Calculator.calculator()
    output = capsys.readouterr().out.strip().splitlines()
    assert output[-1] == "The answer is 0.08214105 Liters"


def test_calculator_kpa(monkeypatch, capsys):
    question = (
        "What volume of CO2 is needed to fill an 0.5 moles tank to a pressure of 101.3 kPa at 27 Celsius?"
    )
    monkeypatch.setattr(builtins, "input", lambda _: question)
    monkeypatch.setattr("time.sleep", lambda _ : None)

    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    import Ideal_Gas_Laws_Calculator
    importlib.reload(Ideal_Gas_Laws_Calculator)

    Ideal_Gas_Laws_Calculator.calculator()
    output = capsys.readouterr().out.strip().splitlines()
    assert output[-1] == "The answer is 12.3211575 Liters"
