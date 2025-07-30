from flask_marshmallow import Marshmallow
ma = Marshmallow()

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'course')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
