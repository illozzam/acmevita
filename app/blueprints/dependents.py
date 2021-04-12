from flask import Blueprint, request, current_app
from ..models import Dependent
from ..schemas import DependentSchema

from .departments import response

bp = Blueprint('dependents', __name__, url_prefix='/dependents')

@bp.route('/list/', methods=['GET'])
def list():
    '''Listagem de dependentes'''

    query = Dependent.query.all()
    return DependentSchema(many=True).jsonify(query)

@bp.route('/insert/', methods=['POST'])
def insert():
    '''Inserção de dependentes

    Campo obrigatório:
        full_name -> Nome completo do dependente
        colaborator_id -> ID do colaborador
    '''
    error = None

    k = request.form.to_dict().keys()
    if not 'full_name' in k or not 'colaborator_id' in k:
        error = 'Os campos \'full_name\' e \'colaborator_id\' são obrigatórios.'

    if not error:
        current_app.db.session.add(Dependent(**request.form))
        current_app.db.session.commit()
    return response(error)
