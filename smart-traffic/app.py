from flask import Flask, render_template, request
from model import predict_traffic

app = Flask(__name__)

def calculate_signal_time(traffic):
    if traffic > 100:
        return "Green: 60 sec | Red: 30 sec"
    elif traffic > 60:
        return "Green: 40 sec | Red: 40 sec"
    else:
        return "Green: 20 sec | Red: 60 sec"

@app.route('/', methods=['GET', 'POST'])
def index():
    traffic = None
    signal_time = None

    if request.method == 'POST':
        hour = int(request.form['hour'])
        traffic = predict_traffic(hour)
        signal_time = calculate_signal_time(traffic)

    return render_template('index.html', traffic=traffic, signal_time=signal_time)

if __name__ == '__main__':
    app.run(debug=True)
