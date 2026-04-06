from flask import Flask, render_template, request, redirect
from main import App
from flask import jsonify

app = Flask(__name__)

system = App()


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/create_user", methods=["POST"])
def create_user():

    username = request.form["username"]
    password = request.form["password"]

    if system.register_user(username, password):

        return redirect("/")

    return "Usuário já existe"


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if system.validate_login(username, password):
        return redirect("/items")

    return "Login inválido"


@app.route("/items")
def list_items():

    current_list = system.shopping.get_current_list()

    if not current_list:
        return render_template("create_list.html")

    items = system.get_items()

    return render_template(
        "list_items.html",
        items=items,
        market=current_list.market,
        list_name=current_list.name
    )


@app.route("/add")
def add_item_page():

    current_list = system.shopping.get_current_list()

    if not current_list:
        return render_template("create_list.html")

    return render_template("add_item.html")


@app.route("/add_item", methods=["POST"])
def add_item():

    name = request.form["name"]
    barcode = request.form["barcode"]
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])

    system.add_item(name, barcode, price, quantity)

    return redirect("/items")


@app.route("/new_list", methods=["POST"])
def new_list():

    name = request.form["name"]
    market = request.form["market"]

    system.create_list(name, market)

    return redirect("/items")


@app.route("/get_item/<barcode>")
def get_item(barcode):

    item = system.get_item_by_barcode(barcode)

    if item:

        return jsonify({
            "name": item["name"],
            "price": item["price"],
            "quantity": item["quantity"]
        })

    return jsonify({
        "name": "",
        "price": "",
        "quantity": ""
    })

if __name__ == "__main__":
    app.run(debug=True)