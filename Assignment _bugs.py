class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    grade = db.Column(db.String(1))  # Fix: changed from db.Integer to db.String(1)

    def to_dict(self):
        return {'id': self.id, 'student_id': self.student_id, 'teacher_id': self.teacher_id, 'grade': self.grade}
