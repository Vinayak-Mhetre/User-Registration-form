from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import logout
import mysql.connector as sql
 
curr_user='default'
un=''
em=''
pwd1=''
pwd2=''
 

def HomePage(request):
    global em
    m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
    cursor=m.cursor()
    c="select * from web_login_table where email='{}' ".format(em)
    cursor.execute(c)
    t = list(cursor.fetchall())
     
    context = {
        'uname':t[0][0],
        'email':t[0][1]
    }
   
    return render (request,'home.html',context)


 



def signupfunction(request):
    global un,pwd2,em,pwd1
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="uname":
                un=value
            if key=="email":
                em=value
            if key=="password1":
                pwd1=value
            if key=="password2":
                pwd2=value
        
        if pwd1!=pwd2:
            return HttpResponse("Your password and confrom password are not Same, Try Again!! ")
        else:
            c="insert into web_login_table Values('{}','{}','{}','{}')".format(un,em,pwd1,pwd2)
            cursor.execute(c)
            m.commit()
            return redirect('login')

    return render(request,'signup.html')



 


def loginfunction(request):
    global em,m,pwd1,curr_user
    if request.method=="POST":
         
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
       
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="p1":
                pwd1=value
        
        c="select * from web_login_table where email='{}' and pass1='{}'".format(em,pwd1)
        cursor.execute(c)
        
        t=list(cursor.fetchall())
        if(len(t) == 0):
            return HttpResponse("Username or Password is incorrect :(  Or If you have not created Account then Signup first. ") 
        else:
            curr_user=t[0][0]
            em = t[0][1]
            return redirect('home')

    return render(request,'login.html')


def change_un_pwd(request):
    if request.method == 'POST':
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        c="select * from web_login_table where email='{}'".format(em)
        cursor.execute(c)
        t = list(cursor.fetchall())
       
        if (t[0][2]==request.POST['old password'] and t[0][0]==request.POST['old username']):
            if(request.POST['new password']==request.POST['confrom password'] and request.POST['new username']==request.POST['confrom username']):
                c="update web_login_table set pass1='{}' where email='{}'".format(request.POST['new password'],em)
                cursor = m.cursor()
                cursor.execute(c)
                m.commit()
                c="update web_login_table set uname='{}' where email='{}'".format(request.POST['new username'],em)
                cursor = m.cursor()
                cursor.execute(c)
                m.commit()
                # print(t)
                return redirect('login')
            else:
                return HttpResponse("(Conform & New Username) OR (Conform & New Password)  are not matching, Try again!")
        else:
            return HttpResponse("Wrong Old Username  OR  Wrong Old Password Entered, Try again!")
    return render(request,'changep.html')




def LogoutPage(request):
    logout(request)
    return redirect('login')

