#!/usr/bin/python
from flask_restplus import fields
from core.api import api
from .utils import *


todo = api.model(API_MODEL, {
    'id': fields.Integer(readOnly=True, description=ID_FIELD_DESC),
    'task': fields.String(required=True, description=TASK_FIELD_DESC)
})