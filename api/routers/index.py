from . import orders, order_details, customer, promotions


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(customer.router)
    app.include_router(promotions.router)
