import pytest
from controllers import GradeController
from models import Assignment

def test_grade_assignment():
    grade_controller = GradeController()
    assignment = Assignment.query.get(1)
    grade_controller.grade_assignment(assignment.id, 'A')
    assert assignment.grade == 'A'

def test_grade_assignment_invalid_grade():
    grade_controller = GradeController()
    assignment = Assignment.query.get(1)
    with pytest.raises(ValueError):
        grade_controller.grade_assignment(assignment.id, 'Invalid Grade')

def test_regrade_assignment():
    grade_controller = GradeController()
    assignment = Assignment.query.get(1)
    grade_controller.grade_assignment(assignment.id, 'B')
    assert assignment.grade == 'B'
