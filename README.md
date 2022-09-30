# BestBuy RDMS: Seth Cram, Chadwick Goodall

Active Website: https://sethcram.pythonanywhere.com/BestBuySearch/login/

## **How to use:**
- Upon navigating to the website, you'll be prompted to login to an account
- Choose to create an account as a customer or vendor
- Login to the account you created
- Once logged on, either user type can view vendor posted products through exact, similar, and requirement searches or logout 
- Once logged on, a customer can add vendor products to their cart and look at products being recommended to them
- Once logged on, a vendor can post, edit, and delete items

## **Scheme:**

Legend: 
- **bold** = primary key
- *italicized* = foreign key

User:
- **id** (primary key)
- **username** (primary key)
- password
- is_vendor
- is_customer

Vendor:
- *VID* (foreign key)
- brand
- *PID* (foreign key)

Customer:
- *CID* (foreign key)
- *PID* (foreign key)

VendorProduct:
- **PID** (primary key)
- name
- cost
- category
- quantity
- payment_type
- product_description
- brief_description
- big_image
- small_image
- publish_date
- update_date
- VID

## **Setup for personal use:**
1. Install XAMPP
2. Get PHPMyAdmin working through running XAMPP MySQL and Apache modules
3. Create a database called "BestBuy_RDMS" through PHPMyAdmin
4. Install Python
5. Setup a virtual environment if on Windows
6. Clone this repo into a folder under your virtual environment
7. Activate the virtual environment
8. Navigate into outermost "mysite" folder
9. Install all dependencies by running "pip install -r requirements.txt"
10. Run "python manage.py makemigrations" and "python manage.py migrate" to consolidate and apply DB changes 
11. To get the SECRET_KEY and DB_PASS, request access from the repo owner
12. Can run the "python manage.py createdata" command with an integer argument to create some test data
13. Then, "python manage.py runserver"
14. Navigate to "http://127.0.0.1:8000/BestBuySearch/products/" in your browser
15. Refer to above "How to use" section for further instruction

## **Technologies:**
- Database Server = PHPMyAdmin run with XAMPP
- IDEs = Spyder, Visual Studio, VSCode
- Version Control = Git
- Packages = mysqlclient, python-decouple, pillow, faker, faker-ecommerce, etc.
- Backend = Django
- Backend Languages = Python, SQL 
- Frontend = Bootstrap
- Frontend Languages = HTML, CSS, JS
- Host = PythonAnywhere