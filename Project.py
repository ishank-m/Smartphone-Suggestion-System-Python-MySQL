import mysql.connector as mysql, pickle, os    #importing necessary modules

mycon = mysql.connect(host="localhost",user="root",passwd="12345")  #connecting to the locally installed MySQL with localhost as host, root as username and 12345 as password
cursor = mycon.cursor()

#password for the administrator to access the admin menu.
admin_pass='12345'
temp=[]

def main():
    cursor.execute("CREATE DATABASE IF NOT EXISTS db")        #creating and using the database on the local 
    cursor.execute("USE db")                                  #machine if it doesn't already exist automatically.
    mycon.commit()
    global admin_pass
    while True:
        print("Select one of the following:\n1. Admin Section\n2. Viewer Section\n3. Exit")
        ch = int(input("Enter choice(1-3): "))
        if ch == 1:
            while True:
                password = input("Enter Administrator Password: ")
                if password == admin_pass:
                    print("----Logging In----")
                    while True:
                        print("1. Create table on current system\n2. View all Records\n3. Add Record\n4. Modify Record\n5. Delete Record\n6. View Viewers' requests\n7. Change current Admin Password\n8. Back")
                        choice = int(input("Enter choice(1-8): "))
                        if choice==1:
                            create_table()
                            continue
                        elif choice == 2:
                            display_records()
                            continue                        
                        elif choice==3:
                            add_data()
                            continue
                        elif choice==4:
                            modify_data()
                            continue
                        elif choice==5:
                            delete_data()
                            continue
                        elif choice==6:
                            view_requests()
                            continue
                        elif choice==7:            #changing the admin password by modifying the value of admin_pass in this .py file in place using text file handling logic. 
                            admin_pass = input("Enter New Password: ")
                            with open(__file__, "r") as file:
                                lines = file.readlines()
                            with open(__file__, "w") as file:
                                for line in lines:
                                    if line.startswith("admin_pass="):
                                        file.write(f"admin_pass='{admin_pass}'\n")
                                    else:
                                        file.write(line)
                            print("----Password Updated Successfully----")
                        elif choice==8:
                            break
                        else:
                            print("----Invalid Choice----")
                            continue
                    break
                else:
                    print("----Incorrect Password-----")
                    continue
        elif ch == 2:
            while True:
                print("1. Suggest me a Phone!\n2. Request a Phone's data\n3. Back")
                cho= int(input("Enter Your Choice(1-3): "))
                if cho==1:
                    suggestive()
                    break
                elif cho==2:
                    request()
                    continue
                elif cho==3:
                    break
                else:
                    print("----Invalid Choice----")
                    continue
            continue
        elif ch==3:
            break
        else:
            print("----Invalid Choice----")
            continue

######### Admin Menu Functions #########

#When the program runs on a machine for the first time, this function creates on the system a default MySQL table comprising 50 smartphone records.
def create_table():
    cursor.execute("DROP TABLE IF EXISTS smartphones")
    create="CREATE TABLE smartphones(brand_name VARCHAR(30),model VARCHAR(50),price INT,rating INT,has_5g VARCHAR(5),has_nfc VARCHAR(5),processor_name VARCHAR(50),processor_brand VARCHAR(30),num_cores INT,battery_capacity INT,ram_capacity INT,internal_memory INT,refresh_rate INT,primary_camera_rear INT,primary_camera_front INT)"
    cursor.execute(create)
    insert="INSERT INTO smartphones VALUES('oneplus', 'OnePlus Nord CE 2 Lite 5G', '18999', '81', 'TRUE', 'FALSE', 'Snapdragon 695', 'snapdragon', '8', '5000', '6', '128', '120', '64', '16'),('samsung', 'Samsung Galaxy A14 5G', '16499', '75', 'TRUE', 'FALSE', 'Exynos 1330', 'exynos', '8', '5000', '4', '64', '90', '50', '13'),('samsung', 'Samsung Galaxy F23 5G', '16999', '80', 'TRUE', 'TRUE', 'Snapdragon  750G', 'snapdragon', '8', '5000', '6', '128', '120', '50', '8'),('motorola', 'Motorola Moto G62 5G', '14999', '81', 'TRUE', 'FALSE', 'Snapdragon  695', 'snapdragon', '8', '5000', '6', '128', '120', '50', '16'),('realme', 'Realme 10 Pro Plus', '24999', '82', 'TRUE', 'FALSE', 'Dimensity 1080', 'dimensity', '8', '5000', '6', '128', '120', '108', '16'),('apple', 'Apple iPhone 14', '66999', '81', 'TRUE', 'TRUE', 'Bionic A15', 'bionic', '6', '3279', '6', '128', '60', '12', '12'),('xiaomi', 'Xiaomi Redmi Note 12 Pro Plus', '29999', '86', 'TRUE', 'FALSE', 'Dimensity 1080', 'dimensity', '8', '4980', '8', '256', '120', '200', '16'),('oppo', 'Oppo A78', '18999', '79', 'TRUE', 'TRUE', 'Dimensity 700 5G', 'dimensity', '8', '5000', '8', '128', '90', '50', '8'),('oneplus', 'OnePlus Nord 2T 5G', '28900', '84', 'TRUE', 'TRUE', 'Dimensity  1300', 'dimensity', '8', '4500', '8', '128', '90', '50', '32'),('samsung', 'Samsung Galaxy A23', '18499', '79', 'FALSE', 'FALSE', 'Snapdragon  680', 'snapdragon', '8', '5000', '6', '128', '60', '50', '8'),('realme', 'Realme 10 Pro', '18999', '82', 'TRUE', 'FALSE', 'Snapdragon 695', 'snapdragon', '8', '5000', '6', '128', '120', '108', '16'),('xiaomi', 'Xiaomi Redmi Note 12 Pro 5G', '24789', '79', 'TRUE', 'FALSE', 'Dimensity 1080', 'dimensity', '8', '5000', '6', '128', '120', '50', '16'),('nothing', 'Nothing Phone 1', '26749', '85', 'TRUE', 'TRUE', 'Snapdragon 778G Plus', 'snapdragon', '8', '4500', '8', '128', '120', '50', '16'),('vivo', 'Vivo T1 5G', '16990', '80', 'TRUE', 'FALSE', 'Snapdragon  695', 'snapdragon', '8', '5000', '6', '128', '120', '50', '16'),('apple', 'Apple iPhone 13', '61999', '79', 'TRUE', 'TRUE', 'Bionic A15', 'bionic', '6', '3240', '4', '128', '60', '12', '12'),('vivo', 'Vivo Y16', '9999', '65', 'FALSE', 'FALSE', 'Helio P35', 'helio', '8', '5000', '3', '32', '60', '13', '5'),('xiaomi', 'Xiaomi Redmi Note 12', '17849', '76', 'TRUE', 'FALSE', 'Snapdragon 4 Gen 1', 'snapdragon', '8', '5000', '4', '128', '120', '48', '13'),('vivo', 'Vivo V25 Pro 5G', '35999', '85', 'TRUE', 'FALSE', 'Dimensity 1300', 'dimensity', '8', '4830', '8', '128', '120', '64', '32'),('oneplus', 'OnePlus 10R 5G', '32999', '86', 'TRUE', 'TRUE', 'Dimensity 8100 Max', 'dimensity', '8', '5000', '8', '128', '120', '50', '16'),('samsung', 'Samsung Galaxy S20 FE 5G', '31266', '88', 'TRUE', 'TRUE', 'Snapdragon 865', 'snapdragon', '8', '4500', '8', '128', '120', '12', '32'),('vivo', 'Vivo Y22', '14499', '72', 'FALSE', 'FALSE', 'Helio G70', 'helio', '8', '5000', '4', '64', '60', '50', '8'),('oneplus', 'OnePlus Nord CE 2 Lite 5G', '21999', '84', 'TRUE', 'FALSE', 'Snapdragon 695', 'snapdragon', '8', '5000', '8', '128', '120', '64', '16'),('poco', 'Poco X4 Pro 5G', '14999', '80', 'TRUE', 'FALSE', 'Snapdragon 695', 'snapdragon', '8', '5000', '6', '64', '120', '64', '16'),('realme', 'Realme 10 Pro', '19999', '84', 'TRUE', 'FALSE', 'Snapdragon 695', 'snapdragon', '8', '5000', '8', '128', '120', '108', '16'),('vivo', 'Vivo V25 5G', '27999', '83', 'TRUE', 'FALSE', 'Dimensity  900', 'dimensity', '8', '4500', '8', '128', '90', '64', '50'),('samsung', 'Samsung Galaxy M33 5G', '17390', '81', 'TRUE', 'TRUE', 'Exynos  1280', 'exynos', '8', '6000', '6', '128', '120', '50', '8'),('apple', 'Apple iPhone 14 Pro Max', '129990', '76', 'TRUE', 'TRUE', 'Bionic  A16', 'bionic', '6', '4323', '6', '128', '120', '48', '12'),('samsung', 'Samsung Galaxy M53 5G', '23980', '85', 'TRUE', 'FALSE', 'Dimensity  900 5G', 'dimensity', '8', '5000', '6', '128', '120', '108', '32'),('apple', 'Apple iPhone 11', '38999', '73', 'FALSE', 'TRUE', 'A13 Bionic', 'a13', '6', '3110', '4', '64', '60', '12', '12')"
    cursor.execute(insert)
    mycon.commit()
    print("----Table successfully created on the system----")

# Admin can add a new record in the MySQL Table.
def add_data():
    while True:
        name=input("Enter the brand name- ")
        model=input("Enter the model- ")
        price=int(input("Enter the price in INR- "))
        rating=int(input("Enter the rating- "))
        has_5g=input("Does the phone has 5g, TRUE/FALSE?- ")
        has_nfc=input("Does the phone has nfc, TRUE/FALSE?- ")
        processor_name=input("Enter the processor name- ")
        processor_brand=input("Enter the processor brand- ")
        num_cores=int(input("Enter the number of cores- "))
        battery_capacity=int(input("Enter the battery capacity in mAh- "))
        ram_capacity=int(input("Enter the ram in GB- "))
        internal_memory=int(input("Enter the internal memory of the phone in GB- "))
        refresh_rate=int(input("Enter the refresh rate in Hz- "))
        primary_camera_rear=int(input("Enter megapixels of rear camera- "))
        primary_camera_front=int(input("Enter megapixels of front camera- "))
        query="insert into smartphones values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(name,model,price,rating,has_5g.upper(),has_nfc.upper(),processor_name,processor_brand,num_cores,battery_capacity,ram_capacity,internal_memory,refresh_rate,primary_camera_rear,primary_camera_front))
        mycon.commit()
        print("----Data added succesfully----")
        c=input("Do you want to enter more data? (yes/no): ")
        if c.lower()=="no":
            break
        elif c.lower()=="yes":
            continue
            
# Admin can modify a particular record from the MySQL table by providing the name of the smartphone and what data about it is to be modified.
def modify_data():
    model = input("Enter the model name of the smartphone to modify: ")
    while True:
        print("Select what you want to modify:\n1. Price\n2. Rating\n3. 5g\n4. nfc\n5. processor name\n6. processor brand\n7. number of cores\n8. Battery Capacity\n9. RAM Capacity\n10. Internal Memory\n11. Refresh Rate\n12. primary camera rear\n13. primary camera front\n14. Back to Admin Menu")
        choice = int(input("Enter your choice (1-14): "))
        if choice == 1:
            new_price = int(input("Enter the new price: "))
            query = "UPDATE smartphones SET price = %s WHERE model = %s"
            cursor.execute(query, (new_price, model))
        elif choice == 2:
            new_rating = int(input("Enter the new rating: "))
            query = "UPDATE smartphones SET rating = %s WHERE model = %s"
            cursor.execute(query, (new_rating, model))
        elif choice == 3:
            N5g = input("Confirm if the phone is 5g or not(true/false): ")
            query = "UPDATE smartphones SET has_5g = %s WHERE model = %s"
            cursor.execute(query, (N5g.upper(), model))
        elif choice == 4:
            Nnfc = input("Confirm if the phone has nfc or not(true/false): ")
            query = "UPDATE smartphones SET has_nfc = %s WHERE model = %s"
            cursor.execute(query, (Nnfc.upper(), model))
        elif choice == 5:
            new_Pname = input("Enter the new processor name: ")
            query = "UPDATE smartphones SET processor_name = %s WHERE model = %s"
            cursor.execute(query, (new_Pname, model))
        elif choice == 6:
            new_Pbrand = input("Enter the new processor brand: ")
            query = "UPDATE smartphones SET processor_brand = %s WHERE model = %s"
            cursor.execute(query, (new_Pbrand, model))
        elif choice == 7:
            new_num_cores = int(input("Enter the new number of cores: "))
            query = "UPDATE smartphones SET num_cores = %s WHERE model = %s"
            cursor.execute(query, (new_num_cores, model))
        elif choice == 8:
            new_battery_capacity = int(input("Enter the Battery capacity (in mAh): "))
            query = "UPDATE smartphones SET battery_capacity = %s WHERE model = %s"
            cursor.execute(query, (new_battery_capacity, model))
        elif choice == 9:
            new_ram_capacity = int(input("Enter the new RAM Capacity(in GB): "))
            query = "UPDATE smartphones SET ram_capacity = %s WHERE model = %s"
            cursor.execute(query, (new_ram_capacity, model))
        elif choice == 10:
            new_internal_memory = int(input("Enter the new Internal Memory (in GB): "))
            query = "UPDATE smartphones SET internal_memory = %s WHERE model = %s"
            cursor.execute(query, (new_internal_memory, model))
        elif choice == 11:
            new_refresh_rate = int(input("Enter the new refresh_rate (in Hz): "))
            query = "UPDATE smartphones SET refresh_rate = %s WHERE model = %s"
            cursor.execute(query, (new_refresh_rate, model))
        elif choice == 12:
            new_camera_rear = int(input("Enter the new rear camera quality (in megapixels): "))
            query = "UPDATE smartphones SET primary_camera_rear = %s WHERE model = %s"
            cursor.execute(query, (new_camera_rear, model))
        elif choice == 13:
            new_camera_front = int(input("Enter the new front camera quality (in megapixels): "))
            query = "UPDATE smartphones SET primary_camera_front = %s WHERE model = %s"
            cursor.execute(query, (new_camera_front, model))
        elif choice == 14:
            print("Exiting modification menu.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        mycon.commit()
        print(f"Record for model '{model}' updated successfully.")
        more = input("Do you want to modify another record? (yes/no): ")
        if more.lower()=="no":
            break
        elif more.lower()=="yes":
            continue

# Displays all the records in the MySQL Table on the local machine.
def display_records():
    cursor.execute("SELECT * FROM smartphones")
    records = cursor.fetchall()
    for record in records:
        print(record)

# Deletes a particular smartphone record after taking input of the model name of the smartphone from the admin.
def delete_data():
    while True:
        mod=input("Enter the name of the model you want to delete: ")
        cursor.execute("SELECT * FROM smartphones WHERE model= %s",(mod,))
        rec = cursor.fetchone()
        if rec:
            cursor.execute("DELETE FROM smartphones WHERE model= %s", (mod,))
            mycon.commit()
            print("----Record deleted successfully!----")
        else:
            print("----Model not found----")
        more=input("Do you want to delete more records?(yes/no): ")
        if more.lower()=="no":
            break
        elif more.lower()=="yes":
            continue

# Can view viewers' request for a particular phone model by accessing a local binary file storing those requests in form of a list
def view_requests():
    while True:
        print("1. View all Requests\n2. Delete a Request\n3. Clear all Requests\n4. Back")
        ch= int(input("Enter Choice (1-3): "))
        if ch==1:
            try:                
                with open("Requests", "rb") as file:
                    requests = pickle.load(file)
                    print("----Requests----")
                    for i in requests:
                        print(i)
            except FileNotFoundError:
                print("----No Requests Yet----")
        elif ch==2:
            try:
                d=int(input("Enter the position(From Top) of the request to delete: "))
                with open("Requests", "rb+") as file:
                    l = pickle.load(file)
                    l.pop(d-1)
                    file.seek(0)
                    pickle.dump(l, file)
                print("----Deleted Successfully----")
            except FileNotFoundError:
                print("----No Requests Yet----")
        elif ch==3:
            try:
                os.remove("Requests")
                print("----Cleared all Requests----")
            except FileNotFoundError:
                print("----No Requests Yet----")
        elif ch==4:
            break
        else:
            print("----Invalid Choice----")
            continue



######### User/Viewer Menu Functions #########



# Function that filters and displays smartphone records from the table based on the user's desired specifications of the smartphone
def suggestive():
    global temp
    cursor.execute('SELECT DISTINCT brand_name FROM smartphones')
    print(cursor.fetchall())
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    brand=input('Preferred phone brand?: ')
    print('-'*70)
    cursor.execute("SELECT * FROM smartphones WHERE brand_name=%s",(brand,))
    super_list=cursor.fetchall()
    while True:
        ch=input("Do you prefer more than one brand? (yes/no): ").lower()
        if ch == "yes":
            print('-'*70)
            brand=input('Preferred phone brand?: ')
            print('-'*70)
            cursor.execute("SELECT * FROM smartphones WHERE brand_name=%s",(brand,))
            l = cursor.fetchall()
            super_list.extend(l)
            print('-'*70)
            print("Record Found!")
            print('-'*70)
            continue
        elif ch =="no":
            break
    

    # checking internal storage
    feature_list = []
    for i in super_list:
        if i[11] not in feature_list:
            feature_list.append(i[11])
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    storage=int(input('Preferred internal storage(in gb)?: '))
    print('-'*70)
    for phone_data in super_list:
        if storage==phone_data[11]:
            temp.append(phone_data)
    super_list = temp

    # checking processor
    feature_list = []
    for i in super_list:
        if i[7] not in feature_list:
            feature_list.append(i[7])
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    processor=input('Preferred processor brand?: ')
    print('-'*70)
    temp=[]
    for phone_data in super_list:
        if processor==phone_data[7]:
            temp.append(phone_data)
    super_list = temp


    #checking ram_capacity
    feature_list = []
    for i in super_list:
        if i[10] not in feature_list:
            feature_list.append(i[10])
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    ram=int(input('Preferred RAM(in gb)?: '))
    print('-'*70)
    temp=[]
    for phone_data in super_list:
        if ram==phone_data[10]:
            temp.append(phone_data)
    super_list = temp

    #checking primary_camera_rear        
    feature_list = []
    for i in super_list:
        if i[13] not in feature_list:
            feature_list.append(i[13])
        
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    rcam=int(input('Preferred megapixels of rear camera?: '))
    print('-'*70)
    temp=[]
    for phone_data in super_list:
        if rcam==phone_data[13]:
            temp.append(phone_data)
    super_list = temp

    #checking primary_camera_front
    feature_list = []
    for i in super_list:
        if i[14] not in feature_list:
            feature_list.append(i[14])
        
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    fcam=int(input('Preferred megapixels of front camera?: '))
    print('-'*70)
    temp=[]
    for phone_data in super_list:
        if fcam==phone_data[14]:
            temp.append(phone_data)
    super_list = temp
    print(super_list)

    #checking battery_capacity
    feature_list = []
    for i in super_list:
        if i[9] not in feature_list:
            feature_list.append(i[9])
        
    print('-'*70)
    print(feature_list)
    print('-'*70)
    print('CHOOSE ONE OF THE CATEGORIES GIVEN ABOVE!!!!')
    battery=int(input('Preferred battery capacity(in mah)?: '))
    print('-'*70)
    temp=[]
    for phone_data in super_list:
        if battery==phone_data[9]:
            temp.append(phone_data)
    super_list = temp
    #displaying possible match(es) to the user's desired specifications or displays appropriate message when no matches were found.
    if super_list:
        for record in super_list:
            print('-'*70)
            print(f"Model: {record[1]}\nPrice: {record[2]}\nRating: {record[3]}\n5G: {record[4]}\nNFC: {record[5]}\nProcessor: {record[6]}\nBattery: {record[9]}\nRam: {record[10]}\nStorage: {record[11]}\nScreen Refresh Rate: {record[12]}\nRear Camera: {record[13]} Megapixels\nFront Camera: {record[14]} Megapixels")
            print('-'*70)
    else:
        print('-'*70)
        print("----No match found----")
        print('-'*70)


# Function that takes user request of a particular smartphone model they would like to be added to the database, and stores it as a list in a binary file.
def request():
    a=input("Enter the requested model of smartphone: ")
    try:
        with open("Requests", "rb") as file:
            l=pickle.load(file)
            l.append([a])
        with open("Requests", "wb") as file:
            pickle.dump(l,file)
    except FileNotFoundError:
        with open("Requests", "wb") as file:
            pickle.dump([[a]], file)
    print("----Request Submitted Successfully----")


# Calls the main function when program is run from the terminal
if __name__=="__main__":
    main()
