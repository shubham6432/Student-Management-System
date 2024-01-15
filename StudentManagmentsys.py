#Student Management System

import MySQLdb
conn = MySQLdb.connect('localhost','root','root','db')
curs = conn.cursor()

while True:
    ch = int(input("\n\nEnter Choice: \n1. Add Student\t\t2.Show All Student\n3. Update Student\t\t4. Delete Student\n5. Sort Students\t\t6. Search a Student \n7. Exit"))
    match ch:
        case 1:
            print("Add Student")
            r = int(input("Enter Roll No"))
            n = input("Enter Name of Student")
            m = float(input("Enter Marks of Student"))
            curs.execute(f"insert into stud values({r},'{n}',{m})")
            conn.commit()
            print("Student Added")

        case 2:
            print("Show All Students")
            curs.execute("Select * from stud")
            print("Rn\t Name\tMarks")
            for row in curs:
                print(row[0],'\t',row[1],'\t',row[2])

        case 3:
            print("Update a Student")
            ch4 = int(input("\nWhat do you want to update: \n1. Update Roll No \t2. Update Marks\n3. Update Name"))
            match ch4:
                case 1:
                    print("Update Roll No of Student")
                    r1 = int(input("Enter New Roll No of Student"))
                    r2 = int(input("Enter Old Roll No of Student"))
                    curs.execute(f"update stud set rn = {r1} where rn = {r2}")
                    if curs.rowcount == 0:
                        print("\nRoll no is not available, Please Enter Valid Roll No")
                    else:
                        conn.commit()

                        print("Student Updated")
                        
                case 2:
                    print("Update Marks of Student")
                    m1 = float(input("Enter New Marks of Student"))
                    m2 = float(input("Enter Old Marks of Student"))
                    curs.execute(f"update stud set marks = {m1} where marks = {m2}")
                    if curs.rowcount == 0:
                        print("\nMarks is not available, Please Enter Valid Marks")
                    else:
                        conn.commit()
                        print("Student Updated")
                        
                case 3:
                    print("Update Name of Student")
                    n1 = input("Enter New Name of Student")
                    n2 = input("Enter Old Name of Student")
                    curs.execute(f"update stud set sname = '{n1}' where sname = '{n2}' ")
                    if curs.rowcount == 0:
                        print("\nName is not available, Please Enter Valid Name")
                    else:
                       conn.commit()
                       print("Student Updated")
                case _:
                    print("Invalid Choice...")

        case 4:
            print("Delete a Student")
            r = int(input("Enter roll no to delete"))
            curs.execute(f"Delete from stud where rn = {r}")
            if curs.rowcount == 0:
                        print("\tRoll no is not available, Please Enter Valid Roll No")
            else:
                conn.commit()
                print("Student Deleted")

        case 5:
            print("Sort Students")
            ch2 = int(input("1. Sort by roll no \t\t2. Sort by Desc Roll No\n3. Sort by Marks\t\t4. Sort by Desc Marks\n5.Sort by Name\t\t6. Sort by Des Name"))
            match ch2:
                case 1:
                    print("Sort by Roll No (Ascending) ")
                    curs.execute("Select * from stud order by rn")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])

                case 2:
                    print("Sort by Roll No (Descending) ")
                    curs.execute("Select * from stud order by rn desc")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])

                case 3:
                    print("Sort by Marks")
                    curs.execute("Select * from stud order by marks")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])

                case 4:
                    print("Sort by Desc Marks")
                    curs.execute("Select * from stud order by marks desc")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])

                case 5:
                    print("Sort by Name")
                    curs.execute("Select * from stud order by sname")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])

                case 6:
                    print("Sort by Desc Name")
                    curs.execute("Select * from stud order by sname desc")
                    print("roll no\tname\tmarks")
                    for row in curs:
                        print(row[0],'\t',row[1],'\t',row[2])
                case _:
                    print("Invalid Choice")

        case 6:
            print("Search a Student")
            ch3 = int(input("1. Search by roll no\t2. Search by Name\n3. Search by Marks"))
            match ch3:
                case 1:
                    print("Search by roll no")
                    r = int(input("enter roll no to search: "))
                    
                    curs.execute(f"select * from stud where rn = {r}")
                    if curs.rowcount == 0:
                        print("\nRoll no is not available, Please Enter Valid Roll No")
                    else:
                        print("roll no\tname\tmarks")
                        for row in curs:
                            print(row[0],'\t',row[1],'\t',row[2])

                case 2:
                    print("Search by Name")
                    n = input("enter name to search: ")
                                        
                    curs.execute(f"select * from stud where sname = '{n}' ")
                    if curs.rowcount == 0:
                        print("\nName is not available, Please Enter Valid Name")
                    else:
                        print("roll no\tname\tmarks")
                        for row in curs:
                            print(row[0],'\t',row[1],'\t',row[2])

                case 3:
                    print("Search by marks")
                    m = float(input("enter marks to search: "))
                    
                    curs.execute(f"select * from stud where marks = {m}")
                    if curs.rowcount == 0:
                        print("\nMarks is not available, Please Enter Valid Marks")
                    else:
                        print("roll no\tname\tmarks")
                        for row in curs:
                            print(row[0],'\t',row[1],'\t',row[2])

                case _:
                    print("invalid choice")

        case 7:
                print("Exiting...")
                break

        case _:
                print("Invalid Choice")          

                
conn.close()
