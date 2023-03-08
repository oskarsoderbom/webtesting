from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv('AAPL-2.csv')
    plt.plot(data['Date'], data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Stock Data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/stock_graph.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
