from flask_restful import Resource
from littlekv.server import LittleKVManager

class LittleKVResource(Resource):
    def __init__(self, manager: LittleKVManager):
        super().__init__()
        self._manager = manager

    def get(self):
        return {}

    def put(self):
        return {}

    def delete(self):
        return {}