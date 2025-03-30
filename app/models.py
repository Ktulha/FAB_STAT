from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()


class Fabric(db.Model):
    __tablename__ = 'fabric'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    picture = db.Column(db.String(150), nullable=True)
    width = db.Column(db.Double, nullable=True)
    density = db.Column(db.Double, nullable=True)
    amount = db.Column(db.Double, nullable=True, default=0)
    speed = db.Column(db.Double, nullable=True)
    stock = db.Column(db.Double, nullable=True)
    active = db.Column(db.Boolean, default=True)
    # Additional attributes can be added here as needed

    def __str__(self):
        return f"{self.name}"


class ProductSchema(db.Model):
    __tablename__ = 'product_schema'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    fabric_id = db.Column(db.Integer, db.ForeignKey(
        'fabric.id'), nullable=False)
    fabric = db.relationship(
        'Fabric', backref=db.backref('product_schemas', lazy=True))
    product = db.relationship(
        'Product', backref=db.backref('product_schemas', lazy=True))
    fabric_cost = db.Column(db.Double, nullable=False)
    __table_args__ = (UniqueConstraint(
        product_id, fabric_id, name='_schema_name'),)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feature_name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    barcode = db.Column(db.String(30), nullable=False)

    active = db.Column(db.Boolean, default=True)
    __table_args__ = (UniqueConstraint(
        'name', 'feature_name', 'barcode', name='_full_product_name'),)


class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(
        'Product', backref=db.backref('sales', lazy=True))
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    active = db.Column(db.Boolean, default=True)


class Shipment(db.Model):
    __tablename__ = 'shipment'
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)
    plan_date = db.Column(db.DateTime, nullable=False)
    fact_date = db.Column(db.DateTime, nullable=True)
    active = db.Column(db.Boolean, default=True)


class ShipmentItem(db.Model):
    __tablename__ = 'shipment_item'
    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipment.id'))
    shipment = db.relationship(
        'Shipment', backref=db.backref('items', lazy=True))
    fabric_id = db.Column(db.Integer, db.ForeignKey('fabric.id'))
    fabric = db.relationship(
        'Fabric', backref=db.backref('shipment_items', lazy=True))
    quantity = db.Column(db.Integer, nullable=False)
    __table_args__ = (UniqueConstraint(
        'shipment_id', 'fabric_id', name='_shipment_item_name'),)


class ConfigRecord(db.Model):
    __tablename__ = 'config_record'
    id = db.Column(db.Integer, primary_key=True)
    config_name = db.Column(db.String(100), nullable=False, unique=True)
    config_value = db.Column(db.String(100), nullable=False)
