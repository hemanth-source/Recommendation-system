from flask import Flask, render_template
import pickle

# Load your DataFrame
popular_df = pickle.load(open('popular.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values))   # Lowercased for consistency

if __name__ == '__main__':
    app.run(debug=True)
