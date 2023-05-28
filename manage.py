from app import create_app
from flask.cli import FlaskGroup
import coverage
import unittest


app = create_app()
cli = FlaskGroup(create_app=create_app)
COV = coverage.coverage(omit=['app/tests/*'], include='app/*')
COV.start()


@cli.command()
def test():
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    
    if result.wasSuccessful():
        
        return 0
    return 1


@cli.command()
def cov():
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    
    if result.wasSuccessful():
        COV.stop()
        print('Coverage summary:')
        COV.report(show_missing=True)
        
        return 0
    return 1


if __name__ == '__main__':
    cli()
