from flask import render_template, jsonify, request
from app import app

results = [
	{'id': 1, 'content': "Reachel is hot"},
	{'id': 2, 'content': "Reachel is cute"},
	{'id': 3, 'content': "Reachel is bald"},
	{'id': 4, 'content': "Reachel is virgin"}
]

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
	query = request.args.get('q', '')
	return jsonify({'results': results, 'search': query})

@app.route('/posts', methods=['POST'])
def create_post():
	if request.json and 'content' in request.json:
		post = {
			'id': results[-1]['id'] + 1,
			'content': request.json['content']
		}
		results.append(post)
		return jsonify({'post': post}), 201
	return jsonify({'error': 'No content provided'}), 400

@app.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
	post = [post for post in results if post['id'] == post_id]
	if len(post) == 0:
		return jsonify({'error': 'No post found'}), 404
	if not request.json:
		return jsonify({'error': 'No data to update'}), 400
	if 'content' not in request.json:
		return jsonify({'error': 'Invalid content'}), 400
	post[0]['content'] = request.json.get('content', post[0]['content'])
	return jsonify({'task': post[0]})

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
	post = [post for post in results if post['id'] == post_id]
	if len(post) == 0:
		return jsonify({'error': 'No post found'}), 404
	results.remove(post[0])
	return jsonify({'result': True})