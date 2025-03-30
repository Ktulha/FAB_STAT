import pandas as pd
from app.models import db, Product, Fabric


def bulk_upload_fabric_csv(file_path):
    print("Starting bulk upload...")

    try:
        # Read the CSV file
        data = pd.read_csv(file_path, sep=';', engine='python')

        # Iterate through the rows of the DataFrame
        for index, row in data.iterrows():
            # Create Fabric instance
            fabric = Fabric(name=row['fabric'], amount=row['amount'],
                            width=row['width'])
            db.session.add(fabric)

        # Commit the session to save the data
        db.session.commit()
        print("Bulk upload successful! Verifying inserted data...")

    except Exception as e:
        db.session.rollback()
        print(f"An error occurred during bulk upload: {e}")


def bulk_upload_product_csv(file_path):
    print("Starting bulk upload...")
    try:
        # Read the CSV file
        data = pd.read_csv(file_path, sep=';', engine='python')
        for index, row in data.iterrows():
            fabric = db.session.query(Fabric).filter_by(
                name=row['fabric_name']).first()
            if not fabric:
                fabric = Fabric(
                    name=row['fabric_name'])
                db.session.add(fabric)
                db.session.commit()
            product = db.session.query(Product).filter_by(
                name=row['product_name'], feature_name=row['feature_name'], barcode=row['barcode']).first()

            if not product:
                product = Product(name=row['product_name'], feature_name=row['feature_name'],
                                  barcode=row['barcode'])

                db.session.add(product)
                db.session.commit()
            else:
                product.fabric = fabric
                product.fabric_cost = row['fabric_cost']
                db.session.commit()

        print("Bulk upload successful! Verifying inserted data...")
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred during bulk upload: {e}")
