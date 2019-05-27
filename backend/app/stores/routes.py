from flask import Blueprint, jsonify, request
from app import mongo


stores = Blueprint("users", __name__)


@stores.route("/api/stores", methods=["GET"])
def get_stores():
    stores = mongo.db.stores

    output = []
    cursor = stores.find()

    for document in cursor:
        document.pop("_id")
        output.append(document)
    return jsonify(output)


@stores.route("/api/stores", methods=["POST"])
def insert_store():
    stores = mongo.db.stores

    try:
        name = request.json["name"]
        start_url = request.json["start_url"]

        if not name or not start_url:
            raise KeyError
        elif stores.find({"name": name}).count() > 0:
            output = {"message": "store name matches existing document."}
            return jsonify(output)
        else:
            single_product_tile = request.json["single_product_tile"]
            single_product_name = request.json["single_product_name"]
            single_product_dollar = request.json["single_product_dollar"]
            single_product_cents = request.json["single_product_cents"]
            bundle_product_tile = request.json["bundle_product_tile"]
            bundle_product_title = request.json["bundle_product_title"]
            bundle_product_names = request.json["bundle_product_names"]
            bundle_product_prices = request.json["bundle_product_prices"]

            store_id = stores.insert(
                {
                    "name": name,
                    "start_url": start_url,
                    "single_product_tile": single_product_tile,
                    "single_product_name": single_product_name,
                    "single_product_dollar": single_product_dollar,
                    "single_product_cents": single_product_cents,
                    "bundle_product_tile": bundle_product_tile,
                    "bundle_product_title": bundle_product_title,
                    "bundle_product_names": bundle_product_names,
                    "bundle_product_prices": bundle_product_prices,
                }
            )
            new_store = stores.find_one({"_id": store_id})

            output = {
                "name": new_store["name"],
                "start_url": new_store["start_url"],
                "single_prodcut_tile": new_store["single_product_tile"],
                "single_product_name": new_store["single_product_name"],
                "single_product_dollar": new_store["single_product_dollar"],
                "single_product_cents": new_store["single_product_cents"],
                "bundle_product_tile": new_store["bundle_product_tile"],
                "bundle_product_title": new_store["bundle_product_title"],
                "bundle_product_names": new_store["bundle_product_names"],
                "bundle_product_prices": new_store["bundle_product_prices"],
            }
            return jsonify(output)

    except KeyError:
        output = {"message": "store name or start_url cannot be blank."}
        return jsonify(output)
