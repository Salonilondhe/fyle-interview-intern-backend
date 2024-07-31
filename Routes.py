from flask import Blueprint
from controllers.assignments_controller import AssignmentsController
from controllers.teachers_controller import TeachersController
from controllers.grade_controller import GradeController

principal_blueprint = Blueprint('principal', __name__)

assignments_controller = AssignmentsController()
teachers_controller = TeachersController()
grade_controller = GradeController()

@principal_blueprint.route('/principal/assignments', methods=['GET'])
def get_assignments():
    return assignments_controller
