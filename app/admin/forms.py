from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, IntegerField, TextAreaField, FileField, SelectField, \
    SelectMultipleField, MultipleFileField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from app.models import User, Group
from app import Config


class ChangeWebhookForm(FlaskForm):
    url = StringField('Webhook URL', validators=[DataRequired()])
    submit = SubmitField('Если не знаешь зачем эта кнопка - не нажимай, пожалуйста')


class ScheduledMessageCreateForm(FlaskForm):
    message_type = SelectField('Тип сообщения', choices=[('text', 'Текст'), ('photo', 'Фото'), ('video', 'Видео'), ('poll', 'Опрос')])
    date_time = DateTimeField('Дата и время отправки')
    text = TextAreaField('Текст сообщения')
    content_link = FileField('Ссылка на вложение')
    group = SelectField('Группа адрессатов')
    submit = SubmitField('Запланировать')


class SendTGMessageForm(FlaskForm):
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class SendGroupTGMessageForm(FlaskForm):
    groups = SelectField('Группа', choices=[('всем', 'всем')])
    tags = SelectField('Атрибут', choices=[('всем', 'всем')])
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class CreateGroupForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class CreateModerForm(FlaskForm):
    from app import create_app
    app = create_app(config_class=Config)
    with app.app_context():
        group = SelectMultipleField('Группа',
                                    choices=[(g.id, g.name) for g in Group.query.order_by(Group.id).all()],
                                    )
        user = SelectField('Пользователь',
                           choices=[(u.id, u.first_name) for u in User.query.filter(User.role == 'admin').all()],
                           )
        submit = SubmitField('Добавить')



class SearchUserForm(FlaskForm):
    name = StringField('ФИО')
    search = SubmitField('Найти')
