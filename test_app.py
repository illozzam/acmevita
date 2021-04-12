import pytest, app

@pytest.fixture
def client():
    api = app.create_app()
    api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    api.config['TESTING'] = True

    with api.test_client() as client:
        with api.app_context():
            api.db.create_all()
        yield client

def test_department(client):
    #Cadastrando um departamento
    req_ins = client.post('/departments/insert/', data={'name': 'Financeiro'})

    #Listando os departamentos
    req_list = client.get('/departments/list/')

    #Cadastrando um colaborador
    client.post('/colaborators/insert/', data=dict(full_name='Sakura Nakamoto', department_id=1))

    #Detalhes do departamento (Testa o have_dependents)
    req_details = client.get('/departments/1/')

    #Cadastrando um dependente
    client.post('/dependents/insert/', data=dict(full_name='Natoshi Nakamoto', colaborator_id=1))

    #Detalhes do departamento (com dependente)
    req_details_dependent = client.get('/departments/1/')

    #Testes
    assert b'"ok":true' in req_ins.data #Insert
    assert b'"name": "Financeiro"' in req_list.data #List
    assert b'"have_dependents": false' in req_details.data #Details
    assert b'"have_dependents": true' in req_details_dependent.data #Details com dependente

def test_colaborator(client):
    #Cadastrando um departamento
    client.post('/departments/insert/', data=dict(name='Limpeza'))

    #Cadastrando um colaborador
    req_ins = client.post('/colaborators/insert/', data=dict(full_name='Fugiro Nakombi', department_id=1))

    #Listando os colaboradores
    req_list = client.get('/colaborators/list/')

    #Testes
    assert b'"ok":true' in req_ins.data #Insert
    assert b'"full_name":"Fugiro Nakombi"' in req_list.data #List

def test_dependent(client):
    #Cadastrando um departamento
    client.post('/departments/insert/', data=dict(name='Contabilidade'))

    #Cadastrando um colaborador
    client.post('/departments/insert/', data=dict(full_name='Contador Caolho', department_id=1))

    #Cadastrando um dependente
    req_ins = client.post('/dependents/insert/', data=dict(full_name='Filho do Contador Caolho', colaborator_id=1))
    #Listando os dependentes

    req_list = client.get('/dependents/list/')

    #Testes
    assert b'"ok":true' in req_ins.data #Insert
    assert b'"full_name":"Filho do Contador Caolho"' in req_list.data #List
