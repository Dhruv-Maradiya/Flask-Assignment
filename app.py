from flask import Flask, render_template

from routes.product_routes import product_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(product_routes, url_prefix="/products")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
