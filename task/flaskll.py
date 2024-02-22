from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_member = StringField('Id астронавта', validators=[DataRequired()])
    password_member = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('Id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

