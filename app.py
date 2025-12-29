from flask import Flask, render_template, request
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import io, base64
from flask import send_from_directory

app = Flask(__name__)

def lotka_volterra(t, z, alpha, beta, delta, gamma):
    x, y = z
    return [alpha*x - beta*x*y, delta*x*y - gamma*y]

@app.route('/', methods=['GET','POST'])
def index():
    img = None
    if request.method == 'POST':
        alpha = float(request.form['alpha'])
        beta  = float(request.form['beta'])
        delta = float(request.form['delta'])
        gamma = float(request.form['gamma'])

        t = np.linspace(0,50,500)
        sol = solve_ivp(lotka_volterra,(0,50),[0.5,0.5],args=(alpha,beta,delta,gamma),t_eval=t)

        plt.figure(figsize=(6,4))
        plt.plot(sol.t, sol.y[0], label="Polusi")
        plt.plot(sol.t, sol.y[1], label="Cuaca")
        plt.legend(); plt.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()

    return render_template('index.html', img=img)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        'static',
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )


if __name__ == '__main__':
    app.run(debug=True)