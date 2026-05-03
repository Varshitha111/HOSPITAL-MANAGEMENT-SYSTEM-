import mysql.connector as con
connection=con.connect(
    host="localhost",
    user="root",
    password="root",
    database="pdbc_project"
)
cursor=connection.cursor()
def view_products():
    cursor.execute('''select * from products''')
    data=cursor.fetchall()
    for i in data:
        print(i[0],i[1],i[2],i[3])
def add_product(data):
    cursor.execute(''' insert into products(product_name,price,stock) values (%s,%s,%s)''',data)
    connection.commit()
    print("Data inserted successfully")
def update_product(data):
    cursor.execute('''update products set stock=%s where p_id=%s''',data)
    connection.commit()
def delete_prod(data):
    cursor.execute('''delete from products where p_id=%s''',data)
    connection.commit()
def order_prod(data):
    # pid=data[0]
    # pstock=(data[1])
    cursor.execute('''select * from products where p_id=%s''',(data[0],))
    # res=cursor.fetchone()
    available_stock=cursor.fetchone()
    if available_stock is None:
        print("Not Available!")
        return
    else:
        prod_price=available_stock[1]
        prod_stock=int(available_stock[2])
        if data[1]>prod_stock:
            print("stock not available")
            return
        total_price=data[1]*prod_price
        final_stock=prod_stock-data[1]
        print("your total price is ",total_price)
        cursor.execute('''update products set stock=%s where p_id=%s''',(final_stock,data[0]))
        connection.commit()
        data1=(data[0],data[1],total_price)
        cursor.execute('''insert into orders(p_id,quantity,total_price) values(%s,%s,%s)''',data1)
        connection.commit()



#user inputs
while True:
    role=int(input("who are you?1.Admin\n 2.User\n 3. Exit"))
    if role==1:
        password=int(input("enter password"))
        if password==1234:
        #Add Product Update Product Delete Product View Products
            while True:
                Admin_choice=int(input("Enter your choice\n 1. Add Product 2. Update Product\n 3. Delete Product\n4. View Products\n 5. Exit\n"))
                if Admin_choice==1:
                    product_name=input("product name")
                    price=float(input("enter price"))
                    stock=int(input("enter stock"))
                    data=(product_name,price,stock)
                    add_product(data)
                elif Admin_choice==2:
                    view_products()
                    p_id=int(input("Enter id to update"))
                    p_stock=int(input("enter stock to update"))
                    data=(p_stock,p_id)
                    update_product(data)
                    view_products()
                elif Admin_choice==3:
                    view_products()
                    del_id=int(input("enter product id to delete"))
                    data=(del_id,)
                    delete_prod(data)
                    view_products()
                elif Admin_choice==4:
                    print("The product details are:\n")
                    view_products()
                elif Admin_choice==5:
                    break
                else:
                    print("Enter correct choice")
            
        else:
            print("wrong password!")
        
    elif role==2:
        # View Products place Order Exit
        while True:
            User_choice=int(input("Enter your choice\n1. View Products \n2. place Order \n3. Exit"))
            if User_choice==1:
                view_products()
            elif User_choice==2:
                view_products()
                o_id=int(input("enter id to place order"))
                o_stock=int(input("enter number of products"))
                
                data=(o_id,o_stock)
                                
                # data=(o_id,o_stock)
                order_prod(data)
            elif User_choice==3:
                break
            else:
                print("Enter correct choice!")
    elif(role==3):
        break;
    else:
        print("wrong choice")