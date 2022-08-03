################################################################################
"""
Test the Nice Number Theorem Formula.
"""
################################################################################

import sys
from pathlib import Path
import pytest

# Add the Main Python file to Path
backend_path = Path(__file__).parent.parent.joinpath("backend").as_posix()
print(backend_path)
sys.path.insert(0, backend_path)

# Import the Function from the Main File
from main import nice_number_theorem, travel_cost

@pytest.mark.parametrize('data', [
    # Input, Round-Down-Control, Expectation
    (1,      True,               0),
    (3,      True,               0),
    (4,      True,               0),
    (5,      True,               5),
    (6,      True,               5),
    (9,      True,               5),
    (10,     True,               10),
    (10,     False,              10),
    (9,      False,              10),
])
def test_niceNumberTheorem(data):
    """Ensure that the Nice Number Theorem is Satisfied."""
    x, round_down, expectation = data
    assert int(expectation) == nice_number_theorem(x=x, round_down=round_down)

@pytest.mark.parametrize('data', [
    # Input, Expectation
    (0,      0),
    (3,      0),
    (25,     0),
    (25.5,   0),
    (27.5,   5),
    (50,     50),
])
def test_travelCosts(data):
    """Ensure that the Travel Costs are Calculated Correctly."""
    distance, expectation = data
    assert int(expectation) == travel_cost(distance)

# END
