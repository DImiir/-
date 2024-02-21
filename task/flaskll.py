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


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    dct = {
        'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
        'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', title=dct['title'], surname=dct['surname'],
                           name=dct['name'], education=dct['education'], profession=dct['profession'], sex=dct['sex'],
                           motivation=dct['motivation'], ready=dct['ready'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

