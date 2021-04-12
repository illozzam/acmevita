from flask import Blueprint, request, current_app, make_response, jsonify
from ..models import Department, Colaborator
from ..schemas import DepartmentSchema, ColaboratorSchema

bp = Blueprint('departments', __name__, url_prefix='/departments')

def response(error):
    return make_response(jsonify(dict(error=error, ok=True if not error else False)))

@bp.route('/list/', methods=['GET'])
def list():
    '''Listagem de departamentos'''

    query = Department.query.all()
    return DepartmentSchema(many=True).dumps(query)

@bp.route('/<int:id>/', methods=['GET'])
def details(id):
    '''Recebe o id de um departamento e retorna os colaboradores que pertencem a ele.'''

    error = None
    query = Colaborator.query.filter(Colaborator.department_id==id)

    if not query:
        error = 'Departamento não cadastrado ou sem colaboradores.'

    if not error:
        return ColaboratorSchema(many=True).dumps(query)
    return response(error)

@bp.route('/insert/', methods=['POST'])
def insert():
    '''Inserção de departamentos

    Campo obrigatório:
        name -> Nome do departamento
    '''
    error = None

    if not 'name' in request.form.to_dict().keys():
        error = 'Campo \'name\' é obrigatório.'

    if not error:
        current_app.db.session.add(Department(**request.form))
        current_app.db.session.commit()
    return response(error)
