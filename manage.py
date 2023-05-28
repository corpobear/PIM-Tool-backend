from app import create_app
from flask.cli import FlaskGroup


app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    # run our tests here
   pass


if __name__ == '__main__':
    cli()
