from flask_marshmallow import Marshmallow
from marshmallow import fields
from .models import Department, Colaborator, Dependent

ma = Marshmallow()

def config(app):
    ma.init_app(app)

class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Department

class ColaboratorSchema(ma.SQLAlchemySchema):
    id = fields.Integer()
    full_name = fields.String()
    department_id = fields.Integer()
    have_dependents = fields.Method('have_dependent')

    def have_dependent(self, obj):
        return True if len(obj.dependents) > 0 else False

class DependentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dependent
        include_relationships = True
