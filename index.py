# This is vercel stuff
from flask import Flask
from flask_bootstrap import Bootstrap4 as Bootstrap
from socket import gethostname

template_folder_path = "Templates"
static_folder_path = "static"
    
app = Flask(__name__, template_folder=template_folder_path, static_folder=static_folder_path)
app.config['SECRET_KEY'] = '93688a56-2e91-4c5e-8a47-5c97e47024f5'
Bootstrap(app)

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
