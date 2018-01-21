
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('the_proj.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    result = request.form
    return render_template('exp.html', result = result)
    
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    v= request.form
    total = result.texpense-v.ex_amount
    print("This is the total",total)
    return render_template('exp.html',total=total)

if __name__ == "__main__":
    app.run(debug=True)   