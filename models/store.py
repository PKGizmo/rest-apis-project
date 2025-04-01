from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # value of back_populates must be identical to models/item.py after Here! comment
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
    # value of back_populates must be identical to models/tag.py after Here! comment
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
