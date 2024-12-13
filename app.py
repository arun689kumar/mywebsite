from flask import Flask, render_template, request

app = Flask(__name__)

# Updated menu data with Cool Drinks (Thums Up, Maaza, Pepsi)
menu_data = {
    'Biryani': [
        {'id': '1', 'name': 'Chicken Biryani', 'price': '₹250'},
        {'id': '2', 'name': 'Mutton Biryani', 'price': '₹400'},
        {'id': '3', 'name': 'Egg Biryani', 'price': '₹180'},
        {'id': '4', 'name': 'Tandoori Chicken Biryani', 'price': '₹300'},
        {'id': '5', 'name': 'Prawn Biryani', 'price': '₹250'}
    ],
    'Starters': [
        {'id': '6', 'name': 'Paneer Tikka', 'price': '₹150'},
        {'id': '7', 'name': 'Veg Pakora', 'price': '₹120'}
    ],
    'Curries': [
        {'id': '8', 'name': 'Butter Chicken', 'price': '₹350'},
        {'id': '9', 'name': 'Dal Makhani', 'price': '₹180'}
    ],
    'Desserts': [
        {'id': '10', 'name': 'Gulab Jamun', 'price': '₹100'},
        {'id': '11', 'name': 'Ras Malai', 'price': '₹120'}
    ],
    'Cool Drinks': [
        {'id': '12', 'name': 'Thums Up', 'price': '₹60'},
        {'id': '13', 'name': 'Maaza', 'price': '₹60'},
        {'id': '14', 'name': 'Pepsi', 'price': '₹60'}
    ]
}
@app.route("/staff-login", methods=["GET", "POST"])
def staff_login():
    if request.method == "POST":
        # Get the email and password entered by the user
        email = request.form['website@gmail.com']
        password = request.form['website123']
        
        # For simplicity, hardcoding a sample email and password (in real applications, use a database)
        if email == "staff@hotel.com" and password == "staff123":
            # Redirect to staff dashboard after successful login
            return redirect("/staff-dashboard")
        else:
            return "<h2>Invalid credentials, please try again.</h2>"

    # Render the login form when the page is loaded
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Staff Login</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
            }
            .login-container {
                margin-top: 50px;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                width: 300px;
                margin-left: auto;
                margin-right: auto;
            }
            .login-container input {
                padding: 10px;
                margin: 10px 0;
                width: 100%;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .login-container button {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .login-container button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Staff Login</h1>
        <div class="login-container">
            <form method="POST">
                <input type="email" name="email" placeholder="Enter Email" required><br>
                <input type="password" name="password" placeholder="Enter Password" required><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </body>
    </html>
    '''
@app.route("/staff-dashboard")
def staff_dashboard():
    # Sample staff data (replace with database queries for a real system)
    staff_profile = {
        'name': 'John Doe',
        'email': 'staff@hotel.com',
        'role': 'Manager'
    }
    
    # Sample order details (replace with actual order data)
    order_details = [
        {'id': '101', 'dish': 'Chicken Biryani', 'status': 'Pending'},
        {'id': '102', 'dish': 'Butter Chicken', 'status': 'Completed'}
    ]
    
    # Generate order details HTML
    orders_html = ""
    for order in order_details:
        orders_html += f'''
        <div class="order-card">
            <p>Order ID: {order['id']}</p>
            <p>Dish: {order['dish']}</p>
            <p>Status: {order['status']}</p>
        </div>
        '''
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Staff Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
            }}
            .dashboard-container {{
                margin-top: 50px;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                width: 80%;
                margin-left: auto;
                margin-right: auto;
            }}
            .order-card {{
                background-color: #f9f9f9;
                padding: 20px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }}
            .order-card p {{
                font-size: 18px;
            }}
            .button {{
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin: 10px;
            }}
            .button:hover {{
                background-color: #45a049;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome, {staff_profile['name']}!</h1>
        <div class="dashboard-container">
            <h2>Staff Profile</h2>
            <p><strong>Name:</strong> {staff_profile['name']}</p>
            <p><strong>Email:</strong> {staff_profile['email']}</p>
            <p><strong>Role:</strong> {staff_profile['role']}</p>
            
            <h2>Orders</h2>
            <div>
                {orders_html}
            </div>
            
            <div>
                <button class="button" onclick="window.location.href='/update-menu'">Update Menu</button>
            </div>
        </div>
    </body>
    </html>
    '''
@app.route("/update-menu")
def update_menu():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Update Menu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
            }
            .update-container {
                margin-top: 50px;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                width: 50%;
                margin-left: auto;
                margin-right: auto;
            }
            .update-container input {
                padding: 10px;
                margin: 10px 0;
                width: 100%;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .update-container button {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .update-container button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Update Menu</h1>
        <div class="update-container">
            <form method="POST">
                <input type="text" name="dish_name" placeholder="Dish Name" required><br>
                <input type="text" name="dish_price" placeholder="Dish Price" required><br>
                <button type="submit">Update</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hotel Management System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 20px 0;
                font-size: 24px;
            }
            .container {
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin: 50px auto;
                width: 80%;
            }
            .hotel-image {
                width: 40%;
            }
            .buttons {
                display: flex;
                flex-direction: column;
                gap: 20px;
            }
            .button {
                padding: 15px 30px;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <header>
            <img src="/static/logo.jpg" alt="Hotel Logo" style="vertical-align: middle; width: 50px;">
            <span>Hotel Name</span>
        </header>
        <div class="container">
            <img src="/static/logo.jpg" alt="Hotel Picture" class="hotel-image">
            <div class="buttons">
                <button class="button" onclick="window.location.href='/staff-login'">Staff Login</button>
                <button class="button" onclick="window.location.href='/customer-login'">Customer Login</button>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route("/customer-login")
def customer_login():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Customer Dashboard</title>
    </head>
    <body>
        <h1 style="text-align:center;">Hotel Name</h1>
        <div style="text-align:center;">
            <img src="/static/logo.jpg" alt="Hotel Logo" style="width: 10%; margin-top: 20px;">
        </div>
        <div style="text-align:center; margin-top: 20px;">
            <h2>Customer Dashboard</h2>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
            <button style="margin: 10px; padding: 10px 20px; background-color: #63a4ff; border: none; color: white;" onclick="window.location.href='/menu'">Show Menu</button>
            <button style="margin: 10px; padding: 10px 20px; background-color: #76d7c4; border: none; color: white;">Order Items</button>
            <button style="margin: 10px; padding: 10px 20px; background-color: #45b39d; border: none; color: white;">Review Items</button>
            <button style="margin: 10px; padding: 10px 20px; background-color: #28a745; border: none; color: white;" onclick="window.location.href='/'">Exit</button>
        </div>
    </body>
    </html>
    '''

@app.route("/menu")
def show_menu():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Menu</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 20px 0;
                font-size: 24px;
            }
            .menu-container {
                display: flex;
                justify-content: space-between;
                margin: 30px;
            }
            .categories {
                width: 20%;
                text-align: left;
                padding-right: 20px;
            }
            .categories button {
                margin: 10px 0;
                padding: 15px 30px;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .categories button:hover {
                background-color: #45a049;
            }
            .dish-grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                width: 75%;
            }
            .dish-card {
                width: 200px;
                padding: 10px;
                background-color: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                text-align: center;
            }
            .dish-card img {
                width: 100%;
                height: auto;
                border-radius: 5px;
            }
            .dish-card h3 {
                margin-top: 10px;
                font-size: 18px;
            }
            .dish-card p {
                margin-top: 5px;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <header>
            <img src="/static/logo.jpg" alt="Hotel Logo" style="vertical-align: middle; width: 50px;">
            <span>Hotel Name</span>
        </header>
        <h2>Select a Category</h2>
        <div class="menu-container">
            <!-- Left-side categories -->
            <div class="categories">
                <button onclick="window.location.href='/category/biryani'">Biryani</button>
                <button onclick="window.location.href='/category/starters'">Starters</button>
                <button onclick="window.location.href='/category/curries'">Curries</button>
                <button onclick="window.location.href='/category/desserts'">Desserts</button>
                <button onclick="window.location.href='/category/cooldrinks'">Cool Drinks</button>
            </div>
            
            <!-- Right-side dishes -->
            <div class="dish-grid">
                <!-- Dishes will be dynamically inserted here -->
            </div>
        </div>
    </body>
    </html>
    '''

@app.route("/category/<category_name>")
def category_page(category_name):
    category_data = menu_data.get(category_name.capitalize(), [])
    
    if not category_data:
        return f"<h2>No dishes found for category: {category_name}</h2>"
    
    dishes_html = ""
    for dish in category_data:
        dishes_html += f'''
        <div class="dish-card">
            <img src="/static/{dish['id']}.jpg" alt="{dish['name']}">
            <h3>{dish['name']}</h3>
            <p>{dish['price']} <br> ID: {dish['id']}</p>
            <button onclick="alert('Added {dish['name']} to cart')">Add</button>
        </div>
        '''
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{category_name.capitalize()} - Menu</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            header {{
                background-color: #4CAF50;
                color: white;
                padding: 20px 0;
                font-size: 24px;
            }}
            .menu-container {{
                display: flex;
                justify-content: space-between;
                margin: 30px;
            }}
            .categories {{
                width: 20%;
                text-align: left;
                padding-right: 20px;
            }}
            .categories button {{
                margin: 10px 0;
                padding: 15px 30px;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }}
            .categories button:hover {{
                background-color: #45a049;
            }}
            .dish-grid {{
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                width: 75%;
            }}
            .dish-card {{
                width: 200px;
                padding: 10px;
                background-color: white;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                text-align: center;
            }}
            .dish-card img {{
                width: 100%;
                height: auto;
                border-radius: 5px;
            }}
            .dish-card h3 {{
                margin-top: 10px;
                font-size: 18px;
            }}
            .dish-card p {{
                margin-top: 5px;
                font-size: 16px;
            }}
            .dish-card button {{
                margin-top: 10px;
                padding: 10px 20px;
                background-color: #007bff;
                border: none;
                color: white;
                cursor: pointer;
                border-radius: 5px;
            }}
            .dish-card button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <header>
            <img src="/static/logo.jpg" alt="Hotel Logo" style="vertical-align: middle; width: 50px;">
            <span>Hotel Name</span>
        </header>
        <h2>{category_name.capitalize()} Menu</h2>
        <div class="menu-container">
            <div class="categories">
                <button onclick="window.location.href='/category/biryani'">Biryani</button>
                <button onclick="window.location.href='/category/starters'">Starters</button>
                <button onclick="window.location.href='/category/curries'">Curries</button>
                <button onclick="window.location.href='/category/desserts'">Desserts</button>
                <button onclick="window.location.href='/category/cooldrinks'">Cool Drinks</button>
            </div>
            <div class="dish-grid">
                {dishes_html}
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
