
from project import app, db  # new
from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)

# new
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()



if __name__ == '__main__':
    cli()