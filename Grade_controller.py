from flask import jsonify, request
from models import Assignment

class GradeController:
    def grade_assignment(self):
        assignment_id = request.json['assignment_id']
        grade = request.json['grade']
        assignment = Assignment.query.get(assignment_id)
        assignment.grade = grade
        db.session.commit()
        return jsonify({'message': 'Assignment graded successfully'})
