#!/usr/bin/python
from flask_restplus import Resource
from core.api import api
from .utils import *
from .api_models import *
from .controllers import DAO

logger = getLogger(__name__)
# Defining the namespace
ns = api.namespace(APP_ROUTE, description=APP_DESC)



@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        logger.info(f"List count of TodoList as : {len(DAO.todos)}")
        logger.debug(f"DEBUG - List count of TodoList as : {len(DAO.todos)}")
        return DAO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        logger.info("Create a new task")
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        logger.info("Fetch a given resource > id:", id)
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        logger.debug(f"Delete a task given its identifier > id:{id}")
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        logger.info(f"Update a task given its identifier > id:{id, api.payload}")
        return DAO.update(id, api.payload)
