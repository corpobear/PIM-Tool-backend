from flask import Flask


def create_app():
    app = Flask(__name__)
    
    
    
    
    @app.route('/test')
    def test():
        return {"message": "ok"}, 200
    
    
    return app
