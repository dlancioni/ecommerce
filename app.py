from flask import Flask

def setup_database(app):
    pass
    
def create_app():
    app = Flask(__name__,
                static_url_path="",
                static_folder="web/static",
                template_folder="web/templates")
    
    setup_database(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()