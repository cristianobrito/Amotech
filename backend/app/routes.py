from .controllers.health_controller import health

def register_routes(app):

    app.add_url_rule("/", "root", health)
    app.add_url_rule("/health", "health", health)