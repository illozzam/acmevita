from flask import Blueprint, request, current_app
from ..models import Colaborator
from ..schemas import ColaboratorSchema, DependentSchema

from .departments import response

bp = Blueprint('colaborators', __name__, url_prefix='/colaborators')

@bp.route('/list/', methods=['GET'])
def list():
    '''Listagem de colaboradores'''

    query = Colaborator.query.all()
    return ColaboratorSchema(many=True).jsonify(query)

@bp.route('/insert/', methods=['POST'])
def insert():
    '''Inserção de colaboradores.

    Campos obrigatórios:
        full_name -> Nome completo do colaborador
        department_id -> ID do departamento do colaborador
    '''

    error = None

    k = request.form.to_dict().keys()
    if not 'full_name' in k or not 'department_id' in k:
        error = 'Os campos \'full_name\' e \'department_id\' são obrigatórios.'

    if not error:
        current_app.db.session.add(Colaborator(**request.form))
        current_app.db.session.commit()
    return response(error)

@bp.route('/<int:id>/dependents/', methods=['GET'])
def list_dependents(id):
    error = None
    query = Colaborator.query.get(id)

    if not query:
        error = 'Colaborador não cadastrado.'

    if len(query.dependents) == 0:
        error = 'Colaborador sem dependentes.'

    if not error:
        query = query.dependents
        return DependentSchema(many=True).jsonify(query)
    return response(error)
