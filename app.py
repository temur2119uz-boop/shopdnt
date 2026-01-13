from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Bu funksiya templates papkasi ichidagi index.html ni ochadi
    return render_template('index.html')

if __name__ == '__main__':
    # Saytni lokal xostda ishga tushirish (http://127.0.0.1:5000)
    app.run(debug=True)
