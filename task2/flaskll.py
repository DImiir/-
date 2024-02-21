from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


@app.route('/list_prof/<list>')
def listing(list):
    prof_list = [
        'инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'климатолог', 'гляциолог', 'штурман',
        'инженер по терраформированию', 'специалист по информационной защите', 'киберинженер', 'астрогеолог'
    ]
    return render_template('list.html', lst=prof_list, type=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

