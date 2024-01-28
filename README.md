# Voxlr Blog

## Setup:

- Install the dependancies in a virtual environment.

    ```
    > python -m venv venv

    > venv\Scripts\activate

    (venv) > pip install -r requirements.txt
    ```


- The `config.py` file has some environmental variables defined.

    - Generate a secret key.

        ```
        >>> import secrets
        >>> key = secrets.token_hex(16)
        ```

        ```
        SECRET_KEY --> key
        SQLALCHEMY_DATABASE_URI --> sqlite:///site.db
        ```

    - Also add the `EMAIL_USER` and `EMAIL_PASS` variables to enable password reset functionality.


- The database file is not uploaded to the repo for obvious reasons. So a database has to be initiated everytime the code is pulled to a new device.

    ```
    >>> from flaskblog.models import User, Post
    >>> from flaskblog import db
    >>> from run import app
    ```

    - Initailize the database.

        ```
        >>> db.create_all()
        ```

    - View `User` or `Post` data.

        ```
        >>> app.app_context().push()
        >>> User.query.all()
        >>> Post.query.all()
        ```

- Add Data For Testing Purposes

    - It's easier to add `User` data through the Registration Form.

    - For `Post` data, write a temporary python script to read through the test values in `data.json` and add them to the the database _(The test data assumes the existance of 2 users)_.

        ```python
        from flaskblog.models import Post
        from flaskblog import db
        from run import app
        import json


        with open('data.json', 'r') as f:
            posts = json.load(f)

        app.app_context().push()

        for post in posts:
            title = post['title']
            content = post['content']
            id = post['user_id']

            x = Post(title=title, content=content, user_id=id)
            db.session.add(x)

        db.session.commit()
        ```