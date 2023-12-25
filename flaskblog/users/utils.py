from flask import url_for, current_app
from flaskblog import mail
from flask_mail import Message
from PIL import Image, ImageOps
import secrets
import os


# * Resize and save image into the file system
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f'{random_hex}{f_ext}'
    picture_path = os.path.join(current_app.root_path, 'static', 'profile_pic', picture_fn)

    output_size = (125, 125)
    #  * This method looks nice on the output image
    i = Image.open(form_picture)
    ImageOps.fit(i, output_size).save(picture_path)

    #  ! Method used previously, deprecated as it doesn't look as nice as the one implemented
    # i.thumbnail(output_size)
    # i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request, then simply ignore this message.
'''
    mail.send(msg)