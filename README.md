# BestBuy RDMS: Seth Cram, Chadwick Goodall


## **Setup for personal use:**
1. Install XAMPP and get PHPMyAdmin working
2. Create a database called "BestBuy_RD"
3. Setup a virtual environment if on Windows
4. Download Django and Python
5. Install all packages specified below
6. Clone this repo into a folder under your virtual environment
7. Activate the virtual environment
8. Run "makemigrations" and "migrate" them 
9. Then, "runserver"
10. Navigate to "http://127.0.0.1:8000/BestBuySearch/products/" in your browser
11. Can run the "createdata" command with an integer argument to create some test data

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

## **Technologies:**
- Host = ?
- Database Server = PHPMyAdmin run with XAMPP
- IDEs = Spyder, Visual Studio, VSCode
- Version Control = Git
- Packages = mysqlclient, python-decouple, pillow, faker, faker-ecommerce
- Backend = Django
- Backend Languages = Python, SQL 
- Frontend = Bootstrap
- Frontend Languages = HTML, CSS, JS

**Development Stages:**
- Phase 1 project report about the ER diagram modeling on March 8th, 2022
- Phase 11 project report concerning normalization and itermediate demo on April 21st  
- Phase 111 comprehensive project report and final demo on May 5th, 2022 
