from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random


class MemberConnect:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "Member Connect")
        self.root.geometry("1360x700+0+0")
        #self.root.config(bg="lightBlue")

        MemID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Gender = StringVar()
        Mtype = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Search = StringVar()
        MemIDBar = StringVar()

        # ========================MainFrame========================
        MainFrame = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="lightBlue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1340, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)

        SearchFrame = Frame(MainFrame, bd=5, width=1340, height=50, relief=RIDGE)
        SearchFrame.grid(row=1, column=0)

        MiddleFrame = Frame(MainFrame, bd=5, width=1340, height=700, relief=RIDGE)
        MiddleFrame.grid(row=2, column=0)

        MembersDetailsFrame = Frame(MiddleFrame, bd=5, padx=6, pady=4, width=1340, height=180, relief=RIDGE)
        MembersDetailsFrame.grid(row=0, column=0)

        TreeViewFrame = Frame(MiddleFrame, bd=5, padx=2, width=1340, height=400, relief=RIDGE)
        TreeViewFrame.grid(row=1, column=0)

        ButtonFrame = Frame(MiddleFrame, bd=7, width=1340, height=50, relief=RIDGE, bg="lightBlue")
        ButtonFrame.grid(row=2, column=0)

        # ========================TitleFrame========================
        self.lblTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text="Member Connection", bd=7)
        self.lblTitle.grid(row=0, column=0, padx=400)
        self.lblMemberID = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Member ID", bd=7, anchor=W, justify=LEFT)
        self.lblMemberID.grid(row=0, column=0, sticky=W, padx=5)
        self.txtMemberID = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=MemID)
        self.txtMemberID.grid(row=0, column=1, padx=5)
        self.lblFirstname = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Firstname", bd=7, anchor=W, justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5)
        self.txtFirstname = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Firstname)
        self.txtFirstname.grid(row=1, column=1, padx=5)
        self.lblSurname = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, anchor=W, justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5)
        self.txtSurname = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Surname)
        self.txtSurname.grid(row=2, column=1, padx=5)
        self.lblAddress = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Address", bd=7, anchor=W, justify=LEFT)
        self.lblAddress.grid(row=0, column=3, sticky=W, padx=5)
        self.txtAddress = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Address)
        self.txtAddress.grid(row=0, column=4, padx=5)
        self.lblPostCode = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Post Code", bd=7, anchor=W, justify=LEFT)
        self.lblPostCode.grid(row=1, column=3, sticky=W, padx=5)
        self.txtPostCode = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=PostCode)
        self.txtPostCode.grid(row=1, column=4, padx=5)
        self.lblGender = Label(MembersDetailsFrame, font=('arial',12,'bold'),text="Gender",bd=7,anchor=W,justify=LEFT)
        self.lblGender.grid(row=2,column=3,sticky=W,padx=5)
        self.cboGender = ttk.Combobox(MembersDetailsFrame,font=('arial',12,'bold'),width=31,state='readonly',textvariable=Gender)
        self.cboGender['values'] = ('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=2,column=4,padx=5)
        self.lblMtype = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Member Type", bd=7, anchor=W, justify=LEFT)
        self.lblMtype.grid(row=0, column=5, sticky=W, padx=5)
        self.cboMtype = ttk.Combobox(MembersDetailsFrame, font=('arial', 12, 'bold'), width=31, state='readonly', textvariable=Mtype)
        self.cboMtype['values'] = ('', 'Full', 'Off Peak', 'Student', 'Over 60')
        self.cboMtype.current(0)
        self.cboMtype.grid(row=0, column=6, padx=5)
        self.lblMobile = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Mobile", bd=7, anchor=W, justify=LEFT)
        self.lblMobile.grid(row=1, column=5, sticky=W, padx=5)
        self.txtMobile = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Mobile)
        self.txtMobile.grid(row=1, column=6, padx=5)
        self.lblEmail = Label(MembersDetailsFrame, font=('arial', 12, 'bold'), text="Email", bd=7, anchor=W, justify=LEFT)
        self.lblEmail.grid(row=2, column=5, sticky=W, padx=5)
        self.txtEmail = Entry(MembersDetailsFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Email)
        self.txtEmail.grid(row=2, column=6, padx=5)

        scroll_y = Scrollbar(TreeViewFrame, orient= VERTICAL)

        self.member_records = ttk.Treeview(TreeViewFrame,height= 12,columns=("memid","firstname","surname","address","postcode","gender","mobile",
                                                                              "email","mtype"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.member_records.heading("memid",text="Member ID")
        self.member_records.heading("firstname",text="Firstname")
        self.member_records.heading("surname",text="Surname")
        self.member_records.heading("address",text="Address")
        self.member_records.heading("postcode",text="Post Code")
        self.member_records.heading("gender",text="Gender")
        self.member_records.heading("mobile",text="Mobile")
        self.member_records.heading("email",text="Email")
        self.member_records.heading("mtype",text="Member Type")

        self.member_records['show'] = 'headings'

        self.member_records.column("memid",width=120)
        self.member_records.column("firstname",width=140)
        self.member_records.column("surname",width=140)
        self.member_records.column("address",width=212)
        self.member_records.column("postcode",width=120)
        self.member_records.column("gender",width=120)
        self.member_records.column("mobile",width=120)
        self.member_records.column("email",width=200)
        self.member_records.column("mtype",width=120)

        self.member_records.pack(fill=BOTH,expand=1)

        #-========================================Buttons Frame========================================================
        self.lblBarCode = Label(SearchFrame, font=('arial', 12, 'bold'), text="Bar Code")
        self.lblBarCode.grid(row=0, column=0, sticky=W, padx=4)
        self.txtBarCode = Entry(SearchFrame, font=('CCode39', 13, 'bold'), bd=5, width=26, justify=CENTER, textvariable=MemIDBar)
        self.txtBarCode.grid(row=0, column=1, padx=39)
        self.txtSearch = Entry(SearchFrame, font=('arial', 12, 'bold'), bd=5, width=33, justify=LEFT, textvariable=Search)
        self.txtSearch.grid(row=0, column=2)
        self.btnSearch = Button(SearchFrame,pady=1,padx=29,bg="lightblue", text="Search", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnSearch.grid(row=0, column=3, padx=5)
        self.btnAddNew = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Add New", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnAddNew.grid(row=0, column=0, padx=5)
        self.btnDisplay = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Display", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnDisplay.grid(row=0, column=1, padx=5)
        self.btnUpdate = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Update", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnUpdate.grid(row=0, column=2, padx=5)
        self.btnDelete = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Delete", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnDelete.grid(row=0, column=3, padx=5)
        self.btnClear = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Clear", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnClear.grid(row=0, column=4, padx=5)
        self.btnExit = Button(ButtonFrame, pady=1, padx=29, bg="lightblue", text="Exit", font=('arial', 16, 'bold'), height=1, width=10, bd=4)
        self.btnExit.grid(row=0, column=5, padx=5)



if __name__ == '__main__':
    root = Tk()
    application = MemberConnect(root)
    root.mainloop()
