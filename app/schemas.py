from marshmallow import Schema, fields

class PostsSchema(Schema):
	id = fields.Str()
	content = fields.Str()
