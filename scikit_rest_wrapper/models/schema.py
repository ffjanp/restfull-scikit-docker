import marshmallow
from ..util import Loader
from ..exceptions.http import SchemaNotValid, SchemaNotPresent

class Schema(object):
    def __init__(self):
        pass

    def get(self):
        # TODO: handle errors here
        try:
            schema = Loader().get_module('schema').ModelSchema(
                strict=True
            )
        except ModuleNotFoundError:
            raise SchemaNotPresent()

        if not self.validate(schema):
            raise SchemaNotValid()

        return schema

    def validate(self, schema):
        return isinstance(
            schema,
            marshmallow.Schema
        )

    def status(self):
        try:
            self.get()
        except (SchemaNotValid, SchemaNotPresent):
            return 'not ok'
        return 'ok'

    def has_descr(self, schema):
        return hasattr(schema, 'describe')

