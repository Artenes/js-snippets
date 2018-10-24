from flask import render_template, jsonify, request
from app import app, db
from app.models import Post
from app.schemas import PostsSchema

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
	query = request.args.get('q', '')
	posts = Post.query.filter(Post.content.like("%"+query+"%")).all()
	schema = PostsSchema(many=True)
	results = schema.dump(posts).data
	return jsonify({'results': results, 'search': query})

@app.route('/posts', methods=['POST'])
def create_post():
	if request.json and 'content' in request.json:
		content = request.json['content']
		post = Post(content=content)
		db.session.add(post)
		db.session.commit()
		schema = PostsSchema()
		return jsonify({'post': schema.dump(post).data}), 201
	return jsonify({'error': 'No content provided'}), 400

@app.route('/post/<string:post_id>', methods=['PUT'])
def update_post(post_id):
	post = Post.query.get(post_id)
	if not post:
		return jsonify({'error': 'No post found'}), 404
	if not request.json:
		return jsonify({'error': 'No data to update'}), 400
	if 'content' not in request.json:
		return jsonify({'error': 'Invalid content'}), 400
	post.content = request.json.get('content', post.content)
	db.session.commit()
	schema = PostsSchema()
	return jsonify({'task': schema.dump(post).data})

@app.route('/post/<string:post_id>', methods=['DELETE'])
def delete_post(post_id):
	post = Post.query.get(post_id)
	if not post:
		return jsonify({'error': 'No post found'}), 404
	db.session.delete(post)
	db.session.commit()
	return jsonify({'result': True})