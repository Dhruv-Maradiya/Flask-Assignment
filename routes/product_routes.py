from flask import Blueprint, render_template, request

from services.product_service import (
    add_product_service,
    delete_product_service,
    get_product_service,
    get_products_service,
    search_products_service,
    update_product_service,
)

product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/", methods=["POST"])
def add_product():
    data = request.json
    return add_product_service(data)


@product_routes.route("/", methods=["GET"])
def get_products():
    page = int(request.args.get("page", 1))  # Default page is 1
    per_page = int(request.args.get("per_page", 10))  # Default page size is 10
    return get_products_service(page, per_page)


@product_routes.route("/<product_id>", methods=["GET"])
def get_product(product_id):
    return get_product_service(product_id)


@product_routes.route("/<product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    return update_product_service(product_id, data)


@product_routes.route("/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    return delete_product_service(product_id)


@product_routes.route("/search", methods=["GET"])
def search_products():
    name = request.args.get("name")
    category = request.args.get("category")
    return search_products_service(name, category)


@product_routes.route("/add")
def add_product_page():
    return render_template("add_product.html")


@product_routes.route("/update/<int:product_id>")
def update_product_page(product_id):
    return render_template("update_product.html", product_id=product_id)
