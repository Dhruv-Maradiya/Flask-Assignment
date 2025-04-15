from bson import ObjectId
from flask import jsonify

from db import products_collection
from schemas.product_schema import ProductSchema


def add_product_service(data):
    try:
        product = ProductSchema(**data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    products_collection.insert_one(product.model_dump())
    return jsonify({"message": "Product added successfully!"}), 201


def get_products_service(page, per_page):
    skip = (page - 1) * per_page
    products = list(products_collection.find().skip(skip).limit(per_page))
    for product in products:
        product["_id"] = str(product["_id"])
    return jsonify(products)


def get_product_service(product_id):
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


def update_product_service(product_id, data):
    try:
        product = ProductSchema(**data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    result = products_collection.update_one(
        {"_id": ObjectId(product_id)}, {"$set": product.model_dump()}
    )
    if result.matched_count:
        return jsonify({"message": "Product updated successfully!"}), 200
    return jsonify({"error": "Product not found"}), 404


def delete_product_service(product_id):
    result = products_collection.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count:
        return jsonify({"message": "Product deleted successfully!"}), 200
    return jsonify({"error": "Product not found"}), 404


def search_products_service(name, category):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if category:
        query["category"] = {"$regex": category, "$options": "i"}
    products = list(products_collection.find(query))
    for product in products:
        product["_id"] = str(product["_id"])
    return jsonify(products)
