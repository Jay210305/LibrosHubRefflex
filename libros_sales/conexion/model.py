import reflex as rx

class Product(rx.Model, table=True):
    id: int
    title: str
    author: str
    category: str 
    price: float
    description: str
    rating: float
    image: str

class ProductState(rx.State):
    products: list[Product] = []

    def get_products(self):
        with rx.session() as session:
            self.products = session.exec(
                Product.select()
            ).all()

    def get_products_by_category(self, category: str):
        with rx.session() as session:
            self.products = session.exec(
                Product.select().where(
                    Product.category == category
                )
            ).all()

    def add_product(self, form_data: dict):
        with rx.session() as session:
            session.add(
                Product(**form_data)
            )
            session.commit()

    def delete_product(self, id: int):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    Product.id == id
                )
            ).first()
            session.delete(product)
            session.commit()