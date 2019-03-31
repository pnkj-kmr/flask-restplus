#!/usr/bin/python
from core.api import api
from .utils import *

logger = getLogger(__name__)

class TodoDAO(object):

  def __init__(self):
    self.counter = 0
    self.todos = []

  def get(self, id):
    logger.info(f"Data fetched with id {id}")
    for todo in self.todos:
        if todo['id'] == id:
            return todo
    api.abort(404, "Todo {} doesn't exist".format(id))

  def create(self, data):
    logger.info(f"Data created with {data}")
    todo = data
    todo['id'] = self.counter = self.counter + 1
    self.todos.append(todo)
    return todo

  def update(self, id, data):
    logger.info(f"Data updated with {data}")
    todo = self.get(id)
    todo.update(data)
    return todo

  def delete(self, id):
    logger.info(f"Data deleted with id {id}")
    todo = self.get(id)
    self.todos.remove(todo)


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


