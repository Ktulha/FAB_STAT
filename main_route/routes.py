from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import desc
from app.models import db, Product, Fabric

user_route = Blueprint('main', __name__)

### FABRIC SECTION ###


@user_route.route('/fabric/delete/<int:fabric_id>', methods=['GET'])
def delete_fabric(fabric_id):
    fabric = Fabric.query.get_or_404(fabric_id)
    db.session.delete(fabric)
    db.session.commit()
    return redirect(url_for('.fabric_list'))


@user_route.route('/', methods=['GET'])
def fabric_list():
    fabrics = Fabric.query.filter_by(active=True).order_by(
        Fabric.amount, desc(Fabric.speed)).all()
    return render_template('index.html', fabrics=fabrics, template='fabric')


@user_route.route('/fabric/create', methods=['GET', 'POST'])
def create_fabric():
    if request.method == 'POST':
        fabric = Fabric(name=request.form['name'],
                        description=request.form['description'])
        db.session.add(fabric)
        db.session.commit()
        return redirect(url_for('.fabric_list'))
    return render_template('components/fabric_form.html')


@user_route.route('/fabric/<fabric_id>')
def edit_fabric(fabric_id):
    fabric = Fabric.query.get(fabric_id)
    return render_template('components/fabric_form.html', fabric=fabric)


@user_route.route('/save_fabric/<fabric_id>', methods=['GET', 'POST'])
def save_fabric(fabric_id):

    if int(fabric_id) == -1:
        fabric = Fabric(name=request.form['name'],
                        description=request.form['description'])
        db.session.add(fabric)
    else:
        fabric = Fabric.query.get(fabric_id)
        fabric.name = request.form['name']
        fabric.description = request.form['description']
    db.session.commit()
    return redirect(url_for('.fabric_list'))

### PRODUCT SECTION ###


@user_route.route('/product', methods=['GET'])
def product_list():
    products = Product.query.all()
    return render_template('index.html', products=products, template='product')


@user_route.route('/product/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            feature_name=request.form['feature_name'],
            description=request.form['description'],
            barcode=request.form['barcode'],
            picture=request.form['picture'],
            fabric_cost=request.form['fabric_cost'],
            active='active' in request.form
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('.product_list'))
    return render_template('components/product_form.html')
