# ACME Vita

API para sistema de cadastro de colaboradores da ACME Vita.

Instalação das bibliotecas:
```
pip install -r requirements.txt
```
Configuração do sistema:
```
export FLASK_APP=app
flask shell
app.db.create_all() #Criando banco de dados
quit()
```
Executando:
```
flask run
```

## Endpoints
#### /departments/
| URL | Método | Descrição | Campos obrigatórios |
| ------ | ------ | ------ | ------ |
| /departments/list/ | GET | Lista todos os departamentos cadastrados | |
| /departments/<id>/ | GET | Retorna detalhes sobre o departamento |  |
| /departments/insert/ | POST | Registra um departamento | name -> Nome do departamento |

#### /colaborators/
| URL | Método | Descrição | Campos obrigatórios |
| ------ | ------ | ------ | ------ |
| /colaborators/list/ | GET | Lista todos os colaboradores | |
| /colaborators/<id>/dependents/ | GET | Retorna a lista de dependentes do colaborador |  |
| /colaborators/insert/ | POST | Registra um novo colaborador | full_name -> Nome completo do colaborador, department_id -> ID do departamento |

#### /dependents
| URL | Método | Descrição | Campos obrigatórios |
| ------ | ------ | ------ | ------ |
| /dependents/list/ | GET | Lista os dependentes | |
| /dependents/insert/ | POST | Registra um dependente | full_name -> Nome completo do colaborador, colaborator_id -> ID do colaborador |

## Realizando testes
```
pytest -v
```
