from flask import Flask

from routes.product_routes import product_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(product_routes, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
