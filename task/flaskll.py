from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import json


class LoginForm(FlaskForm):
    id_member = StringField('Id астронавта', validators=[DataRequired()])
    password_member = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

list_num = [1, 2, 3]


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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/distribution')
def distribution():
    members = [
        'Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин', 'Прог Длюкич'
    ]
    return render_template('distribution.html', people=members)


@app.route('/table/<gender>/<age>')
def room_table(gender, age):
    if int(age) < 21:
        ok = True
    else:
        ok = False
    return render_template('table_room.html', gender=gender, age=ok)


@app.route('/galery', methods=['POST', 'GET'])
def slider():
    global list_num
    if request.method == 'GET':
        return render_template('galery.html', first_pic=f'img/mars{list_num[-1]}.jpg',
                               second_pic=f'img/mars{list_num[-2]}.jpg',
                               third_pic=f'img/mars{list_num[-3]}.jpg')
    elif request.method == 'POST':
        list_num.append(list_num[-1] + 1)
        request.files['file'].save(f'static/img/mars{list_num[-1]}.jpg')
        return render_template('galery.html', first_pic=f'img/mars{list_num[-1]}.jpg',
                               second_pic=f'img/mars{list_num[-2]}.jpg',
                               third_pic=f'img/mars{list_num[-3]}.jpg')


@app.route('/member')
def member():
    with open('templates/josn.json') as file:
        json = file.read()
    return render_template('member.html', json=json)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

