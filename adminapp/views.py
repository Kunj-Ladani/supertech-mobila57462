from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import mysql.connector
import datetime

def getdb():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="mobila_db")
    return mydb

def index(request):
    try:

        pendingorder = "select count(o.o_id) from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Pending' order by o.o_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(pendingorder)
        pendingorder = mycursor.fetchall()

        confirmorder = "select count(o.o_id) from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Confirm' order by o.o_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(confirmorder)
        confirmorder = mycursor.fetchall()

        completeorder = "select count(o.o_id) from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Complete' order by o.o_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(completeorder)
        completeorder = mycursor.fetchall()

        cancelorder = "select count(o.o_id) from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Cancel' order by o.o_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(cancelorder)
        cancelorder = mycursor.fetchall()

        Category= "select count(cat_id) from category_tb order by cat_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(Category)
        Category = mycursor.fetchall()

        Product = "select count(p_id) from product_tb,category_tb where category_tb.cat_id = product_tb.cat_id order by p_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(Product)
        Product = mycursor.fetchall()

        User = "select count(u_id) from user_tb order by u_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(User)
        User = mycursor.fetchall()
        
        Feedback = "select count(f_id) from feedback_tb order by f_id desc"
        mydb = getdb()
        mycursor = mydb.cursor() 
        mycursor.execute(Feedback)
        Feedback = mycursor.fetchall()
        



        alldata = {
            'pendingorder':pendingorder,
            'confirmorder':confirmorder,
            'completeorder':completeorder,
            'cancelorder':cancelorder,
            'Category':Category,
            'Product':Product,
            'User':User,
            'Feedback':Feedback

        }

        return render(request,'index.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def category(request):

    try:
        if request.POST:
            
            cat_name = request.POST.get("cat_name")

            cat_image = request.FILES["cat_image"]
            img = FileSystemStorage()
            cat_image = img.save(cat_image.name,cat_image)
            
            cat_status = request.POST.get("cat_status")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO `category_tb`(`cat_name`, `cat_image`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES ('"+str(cat_name)+"','"+str(cat_image)+"','"+str(cat_status)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("category")
        
        elif request.GET.get("cat_id")!= None:
            cat_id = request.GET.get("cat_id")

            cdel = "delete from category_tb where cat_id = '"+str(cat_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cdel)
            mydb.commit()
                    
            return redirect("category")
        else:

            csel = "select * from category_tb order by cat_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(csel)
            c_data = mycursor.fetchall()
            
            return render(request,'category.html',{'c_data':c_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def categoryedit(request):

    try:
        if request.POST:
            cat_id = request.GET.get("cat_id")
            cat_name = request.POST.get("cat_name")

            if request.POST.get("cat_image") != "":
                cat_image = request.FILES["cat_image"]
                img = FileSystemStorage()
                old_img = img.save(cat_image.name,cat_image)
            else:
                old_img = request.POST.get("old_img")



            cat_status = request.POST.get("cat_status")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "update category_tb set cat_name = '"+str(cat_name)+"',cat_image = '"+str(old_img)+"',cat_status = '"+str(cat_status)+"',cat_udate = '"+cdate+"' where cat_id = '"+str(cat_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("category")
        
       
        else:
            cat_id = request.GET.get("cat_id")

            csel = "select * from category_tb where cat_id = '"+str(cat_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(csel)
            c_data = mycursor.fetchall()
            
            return render(request,'categoryedit.html',{'c_data':c_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')



def product(request):

    try:
        if request.POST:
            
            cat_id = request.POST.get("cat_id")
            p_name = request.POST.get("p_name")
            p_mrp = request.POST.get("p_mrp")
            p_price = request.POST.get("p_price")
            p_details = request.POST.get("p_details")

            p_image1 = request.FILES["p_img1"]
            img = FileSystemStorage()
            p_image1 = img.save(p_image1.name,p_image1)

            p_image2 = request.FILES["p_img2"]
            img = FileSystemStorage()
            p_image2 = img.save(p_image2.name,p_image2)

            p_image3 = request.FILES["p_img3"]
            img = FileSystemStorage()
            p_image3 = img.save(p_image3.name,p_image3)

            p_descleminar = request.POST.get("p_descleminar")
          
            p_status = request.POST.get("p_status")

            p_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "INSERT INTO `product_tb`(`cat_id`,`p_name`,`p_mrp`, `p_price`,`p_details`,`p_img1`" \
            "`p_img2`,`p_img3`,`p_descleminar`, `p_status`, `p_cdate`, `p_udate`) VALUES ('"+str(cat_id)+"',"
            "'"+str(p_name)+"','"+str(p_mrp)+"','"+str(p_price)+"','"+str(p_details)+"','"+str(p_image1)+"','"+str(p_image2)+"',"
            "'"+str(p_image3)+"','"+str(p_descleminar)+"','"+str(p_status)+"','"+p_date+"','"+p_date+"')"
            
            mydb = getdb()
            mycursor = mydb.cursor() 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("product")
        
        elif request.GET.get("p_id")!= None:
            p_id = request.GET.get("p_id")

            pdel = "delete from product_tb where p_id = '"+str(p_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(pdel)
            mydb.commit()
                    
            return redirect("product")
        else:

            psel = "select * from product_tb,category_tb where category_tb.cat_id = product_tb.cat_id order by p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(psel)
            p_data = mycursor.fetchall()

            catsel = "select * from category_tb where cat_status = 'Active' order by cat_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(catsel)
            cdata = mycursor.fetchall()

            alldata = {
                'p_data' : p_data,
                'cdata' : cdata
            }
            
            return render(request,'product.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def productedit(request):

    try:
        if request.POST:
            p_id = request.GET.get("p_id")
            cat_id = request.POST.get("cat_id")
            p_name = request.POST.get("p_name")
            p_mrp = request.POST.get("p_mrp")
            p_price = request.POST.get("p_price")
            p_details = request.POST.get("p_details")


            if request.POST.get("p_img1") != "":
                p_image1 = request.FILES["p_img1"]
                img = FileSystemStorage()
                old_img1 = img.save(p_image1.name,p_image1)
                
            else:
                old_img1 = request.POST.get("old_img1")

            if request.POST.get("p_img2") != "":
                p_image2 = request.FILES["p_img2"]
                img = FileSystemStorage()
                old_img2 = img.save(p_image2.name,p_image2)
                
            else:
                old_img2 = request.POST.get("old_img2")

            if request.POST.get("p_img3") != "":
                p_image3 = request.FILES["p_img3"]
                img = FileSystemStorage()
                old_img3 = img.save(p_image3.name,p_image3)
                
            else:
                old_img3 = request.POST.get("old_img3")

            p_descleminar = request.POST.get("p_descleminar")

            p_status = request.POST.get("p_status")

            pdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ins = "update product_tb set cat_id = '"+str(cat_id)+"', p_name = '"+str(p_name)+"',p_mrp = '"+str(p_mrp)+"',p_price = '"+str(p_price)+"',p_details = '"+str(p_details)+"',p_img1 = '"+str(old_img1)+"',p_img2 = '"+str(old_img2)+"',p_img3 = '"+str(old_img3)+"',p_descleminar = '"+str(p_descleminar)+"',p_status = '"+str(p_status)+"',p_udate = '"+pdate+"' where p_id = '"+str(p_id)+"'"
        
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("product")
        
       
        else:
            p_id = request.GET.get("p_id")

            psel = "select * from product_tb where p_id = '"+str(p_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(psel)
            p_data = mycursor.fetchall()


            catsel = "select * from category_tb where cat_status = 'Active' order by cat_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(catsel)
            cdata = mycursor.fetchall()

            alldata = {
                'p_data' : p_data,
                'cdata' : cdata
            }


            
            return render(request,'productedit.html',alldata)
    except NameError:
        print("internal error")
    except:
        print('Error returned')



def vendor(request):

    try:
        if request.GET.get("v_id")!= None:
            v_id = request.GET.get("v_id")

            cdel = "delete from vendor_tb where v_id = '"+str(v_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cdel)
            mydb.commit()
                    
            return redirect("vendor")
        else:

            csel = "select * from vendor_tb order by v_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(csel)
            v_data = mycursor.fetchall()
            
            return render(request,'vendor.html',{'v_data':v_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def order(request):

    try:
        if request.POST:
            
            o_pincode = request.POST.get("o_pincode")
            o_address = request.POST.get("o_address")
            o_totalquntity = request.POST.get("o_address")
            o_totalprice=request.POST.get("o_totalprice")
            o_status = request.POST.get("o_status")
            o_cdate = request.POST.get("o_cdate")
            o_udate = request.POST.get("o_udate")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if ostatus =='Pending':
                ostatus = 'Confirm'
            elif ostatus =='Confirm':
                ostatus = 'Complete'
            elif ostatus =='Complete':
                ostatus = 'Cancel'
            else:
                ostatus ='Pending'

            ins = "INSERT INTO `order_tb`(`o_pincode`,`o_address`, `o_totalquntity`,`o_totalprice`, `o_status`, `o_cdate`, `o_udate`) VALUES ('"+str(o_pincode)+"','"+str(o_address)+"','"+str(o_totalquntity)+"','"+str(o_totalprice)+"','"+str(o_status)+"','"+str(o_cdate)+"','"+str(o_udate)+"','"+cdate+"','"+cdate+"')"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("order")
        
        elif request.GET.get("o_id")!= None:
            o_id = request.GET.get("o_id")

            odel = "delete from order_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(odel)
            mydb.commit()
                    
            return redirect("order")
        else:

            osel = "select * from order_tb order by o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()
            
            return render(request,'order.html',{'o_data':o_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')



def pendingorder(request):

    try:
        if request.GET.get("o_id")!= None:
            o_id = request.GET.get("o_id")

            odel = "delete from order_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(odel)
            mydb.commit()

            cartdel = "delete from cart_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cartdel)
            mydb.commit()
                    
            return redirect("pendingorder")
        
        elif request.GET.get("oid")!= None:
            oid = request.GET.get("oid")
            ostatus = request.GET.get("ostatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if ostatus =='Pending':
                ostatus = 'Confirm'
            elif ostatus =='Confirm':
                ostatus = 'Complete'
            elif ostatus =='Complete':
                ostatus = 'Cancel'
            else:
                ostatus ='Pending'

            ins = "update order_tb set o_status = '"+str(ostatus)+"',o_udate = '"+cdate+"' where o_id = '"+str(oid)+"'"
         
            mydb=getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(ins)
            mydb.commit()
                
            return redirect("pendingorder")

        else:

            osel = "select * from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Pending' order by o.o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()
            
            return render(request,'pendingorder.html',{'o_data':o_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def confirmorder(request):

    try:
        if request.GET.get("o_id")!= None:
            o_id = request.GET.get("o_id")

            odel = "delete from order_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(odel)
            mydb.commit()

            cartdel = "delete from cart_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cartdel)
            mydb.commit()
                    
            return redirect("confirmorder")
        
        elif request.GET.get("oid")!= None:
            oid = request.GET.get("oid")
            ostatus = request.GET.get("ostatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if ostatus =='Pending':
                ostatus = 'Confirm'
            elif ostatus =='Confirm':
                ostatus = 'Complete'
            elif ostatus =='Complete':
                ostatus = 'Cancel'
            else:
                ostatus ='Pending'

            ins = "update order_tb set o_status = '"+str(ostatus)+"',o_udate = '"+cdate+"' where o_id = '"+str(oid)+"'"
         
            mydb=getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(ins)
            mydb.commit()
                
            return redirect("confirmorder")

        else:

            osel = "select * from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Confirm' order by o.o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()
            
            return render(request,'confirmorder.html',{'o_data':o_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')



def completeorder(request):

    try:
        if request.GET.get("o_id")!= None:
            o_id = request.GET.get("o_id")

            odel = "delete from order_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(odel)
            mydb.commit()

            cartdel = "delete from cart_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cartdel)
            mydb.commit()
                    
            return redirect("completeorder")
        
        elif request.GET.get("oid")!= None:
            oid = request.GET.get("oid")
            ostatus = request.GET.get("ostatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if ostatus =='Pending':
                ostatus = 'Confirm'
            elif ostatus =='Confirm':
                ostatus = 'Complete'
            elif ostatus =='Complete':
                ostatus = 'Cancel'
            else:
                ostatus ='Pending'

            ins = "update order_tb set o_status = '"+str(ostatus)+"',o_udate = '"+cdate+"' where o_id = '"+str(oid)+"'"
         
            mydb=getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(ins)
            mydb.commit()
                
            return redirect("completeorder")

        else:

            osel = "select * from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Complete' order by o.o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()
            
            return render(request,'completeorder.html',{'o_data':o_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def cancelorder(request):

    try:
        if request.GET.get("o_id")!= None:
            o_id = request.GET.get("o_id")

            odel = "delete from order_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(odel)
            mydb.commit()

            cartdel = "delete from cart_tb where o_id = '"+str(o_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cartdel)
            mydb.commit()
                    
            return redirect("cancelorder")
        
        elif request.GET.get("oid")!= None:
            oid = request.GET.get("oid")
            ostatus = request.GET.get("ostatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if ostatus =='Pending':
                ostatus = 'Confirm'
            elif ostatus =='Confirm':
                ostatus = 'Complete'
            elif ostatus =='Complete':
                ostatus = 'Cancel'
            else:
                ostatus ='Pending'

            ins = "update order_tb set o_status = '"+str(ostatus)+"',o_udate = '"+cdate+"' where o_id = '"+str(oid)+"'"
         
            mydb=getdb()
            mycursor = mydb.cursor(dictionary=True)
            mycursor.execute(ins)
            mydb.commit()
                
            return redirect("cancelorder")

        else:

            osel = "select * from order_tb o,user_tb u where o.u_id = u.u_id and o.o_status = 'Cancel' order by o.o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()
            
            return render(request,'cancelorder.html',{'o_data':o_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def cart(request):

    try:
        cartid = request.GET.get("cart_id")

        osel = "select * from order_tb o,cart_tb c,product_tb p where o.o_id  = c.o_id and c.p_id = p.p_id and c.o_id = '"+str(cartid)+"' order by c.c_id desc"
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True) 
        mycursor.execute(osel)
        cart_data = mycursor.fetchall()
        
        return render(request,'cart.html',{'cart_data':cart_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def feedback(request):

    try:
        if request.GET.get("f_id")!= None:
            f_id = request.GET.get("f_id")

            cdel = "delete from feedback_tb where f_id = '"+str(f_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cdel)
            mydb.commit()
                    
            return redirect("feedback")
        
        elif request.GET.get("fid")!= None:
            fid = request.GET.get("fid")
            fstatus = request.GET.get("fstatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if fstatus == 'Active':
                fstatus = 'Deactive'
            else:
                fstatus = 'Active'


            ins = "update feedback_tb set f_status = '"+str(fstatus)+"',f_udate = '"+cdate+"' where f_id  = '"+str(fid)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("feedback")
        else:

            csel = "select * from feedback_tb order by f_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(csel)
            f_data = mycursor.fetchall()
            
            return render(request,'feedback.html',{'f_data':f_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def user(request):

    try:
        
        if request.GET.get("u_id")!= None:
            u_id = request.GET.get("u_id")

            cdel = "delete from user_tb where u_id = '"+str(u_id)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(cdel)
            mydb.commit()
                    
            return redirect("user")
        
        elif request.GET.get("uid")!= None:
            uid = request.GET.get("uid")
            ustatus = request.GET.get("ustatus")

            cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if ustatus == 'Active':
                ustatus = 'Deactive'
            else:
                ustatus = 'Active'


            ins = "update user_tb set u_status = '"+str(ustatus)+"',u_udate = '"+cdate+"' where u_id  = '"+str(uid)+"'"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(ins)
            mydb.commit()
                    
            return redirect("user")

        else:

            csel = "select * from user_tb order by u_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(csel)
            u_data = mycursor.fetchall()
            
            return render(request,'user.html',{'u_data':u_data})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def login(request):
    try:
        msg=""
        if request.POST:

            username = request.POST.get("username")
            password = request.POST.get("password")

            lsel = "select * from login_tb where username = '"+str(username)+"' and password = '"+str(password)+"'"
            mydb = getdb()
            mycursor = mydb.cursor() 
            mycursor.execute(lsel)
            l_data = mycursor.fetchall()
           
            if len(l_data) > 0:
                
                request.session["id"] = l_data[0][0]
                request.session["username"] = username
                request.session["image"] = l_data[0][3]
                request.session["time"] = str(l_data[0][4])

                return redirect("index")
            else:
                msg = "Invalid Username Or Password.!"
                return render(request,'login.html',{'msg':msg})
        else:
            return render(request,'login.html',{'msg':msg})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

def logout(request):
    try:
        aid = request.session["id"]
        cdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        update = "update login_tb set lastseen = '"+cdate+"' where id = '"+str(aid)+"'"
        mydb = getdb()
        mycursor = mydb.cursor(dictionary=True) 
        mycursor.execute(update)
        mydb.commit()

        request.session["id"] = None
        request.session["username"] = None
        request.session["image"] = None
        request.session["time"] = None

        return redirect("login")
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def orderreport(request):

    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")
            status = request.POST.get("status")

            osel = "select * from order_tb o,user_tb u where o.u_id = u.u_id and DATE(o.o_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' and o.o_status = '"+str(status)+"' order by o.o_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(osel)
            o_data = mycursor.fetchall()

            return render(request,'orderreport.html',{'o_data':o_data})
        else:

            return render(request,'orderreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def userreport(request):

    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")

            psel = "select * from user_tb where DATE(u_cdate) between '"+str(s_date)+"' and '"+str(e_date)+"' order by u_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(psel)
            u_data = mycursor.fetchall()

            return render(request,'userreport.html',{'u_data':u_data})
        else:

            return render(request,'userreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')


def productreport(request):

    try:
        if request.POST:
            s_date = request.POST.get("s_date")
            e_date = request.POST.get("e_date")

            psel = "select * from product_tb,category_tb where category_tb.cat_id = product_tb.cat_id and DATE(product_tb.p_cdate) between"" '"+str(s_date)+"' and '"+str(e_date)+"' order by p_id desc"
            mydb = getdb()
            mycursor = mydb.cursor(dictionary=True) 
            mycursor.execute(psel)
            p_data = mycursor.fetchall()

            return render(request,'productreport.html',{'p_data':p_data})
        else:

            return render(request,'productreport.html',{})
    except NameError:
        print("internal error")
    except:
        print('Error returned')

