from flask import Flask, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work

@app.route('/articles/<int:id>')
def get_article(id):
    # Example article data (in a real app, you'd probably query the database)
    article = {
        'id': id,
        'title': f"Article {id}",
        'author': 'John Doe',  # Example author
        'content': 'This is a great article!',
    }

    # Initialize session['page_views'] using ternary logic
    session['page_views'] = session['page_views'] + 1 if 'page_views' in session else 1

    # If page_views exceed 3, return an error message
    if session['page_views'] > 3:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

    # Return the article information along with page views
    return jsonify({
        'title': article['title'],
        'author': article['author'],
        'content': article['content'],
        'page_views': session['page_views'],
    })

if __name__ == '__main__':
    app.run(debug=True)
