import uuid
from app import db

class Post(db.Model):

	__tablename__ = 'posts'

	id = db.Column(db.String, primary_key=True, nullable=False)
	content = db.Column(db.String, nullable=False)
	tags = db.Column(db.String, nullable=False, comment='List of tags separated by comma')
	user_id = db.Column(db.String, nullable=True)
	public = db.Column(db.Boolean, nullable=False, default=False)

	def __init__(self, content="", tags="", user_id=None, puclic=False):
		self.id = str(uuid.uuid4())
		self.content = content
		self.tags = tags
		self.user_id = user_id
		self.puclic = puclic

	def __repr__(self):
		return '<Post {}>'.format(self.id)