import sqlite3
from flask import Flask, render_template, request, json

app = Flask(__name__)


# opening login page
@app.route("/login")
def login():
    return render_template("login.html")


# updating sites information database
@app.route("/updateSites")
def updatesites():
    # call functions to update site

    return()


# logging ISP or Client Admin
@app.route("/ISP_admin_login_page1", methods=['POST'])
def reply():
    user = request.form['username']
    passwrd = request.form['password']

    if user == 'ISPAdmin1' and passwrd == 'ryerson':
        return render_template('ISP_admin_login_page1.html', usr=user)
    else:
        if user == 'ClientAdmin1' and passwrd == 'ryerson':
            updatesites()
            return render_template('Client_admin_login.html', usr=user)

    return 'wrong username/password'


# function to go to approve list of new vpn users
@app.route("/admin_approval_list")
def approveclientlist():
    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    # fetching VPN users
    sql = 'select * from table1_client1users'

    cursor.execute(sql)

    rows = cursor.fetchall()
    clientusers = []

    for row in rows:
        if row[2] == 0:
            clientusers.append(row[0])

    print(clientusers)

    con.close()

    return render_template("ISP_admin_approval_user.html", clientlist=json.dumps(clientusers))


# function to approve new client user
@app.route("/approve_user/<user>")
def approveclientuser(user):
    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    # fetching VPN username & password
    cursor.execute('select * from table1_client1users where user = "%s"' % user)

    vpnclient = cursor.fetchall()

    for client in vpnclient:
        usr = client[0]
        passwrd = client[1]
        site = client[3]

    # configuring user to router code goes here


    # updating VPN users
    cursor.execute('UPDATE table1_client1users SET existing = 1 WHERE user = "%s"' % user)

    con.commit()

    rows = cursor.fetchall()

    print(rows)

    con.close()

    return 'VPN user approved'


# function to reject new client user
@app.route("/reject_user/<user>")
def rejectclientuser(user):
    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    # deleting VPN users
    cursor.execute('DELETE FROM table1_client1users WHERE user = "%s"' % user)

    con.commit()

    rows = cursor.fetchall()

    print(rows)

    con.close()

    return 'VPN user removed'


# opening Site details page
@app.route("/open_site_details/<sitename>")
def open_site_details(sitename):
    updatesites()

    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    cursor.execute('select * from table2_client1device where site = "%s"' % sitename)

    sites = cursor.fetchall()

    cursor.close()

    print(sites)
    for site in sites:
        return render_template("SiteDetails.html", sit=sitename, status=site[1], time=site[2], ip=site[3])


# go to VPN user client list page
@app.route("/VPNUserList/<site>")
def vpnclientlist(site):
    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    # fetching VPN users
    cursor.execute('select * from table1_client1users where site = "%s"' % site)

    rows = cursor.fetchall()
    clientusers = []

    for row in rows:
        clientusers.append(row[0])

    print(clientusers)

    con.close()

    return render_template("Client_admin_VPNuserList.html", site=site, clientlist=json.dumps(clientusers))


# opening add user page
@app.route("/add_user/<site>")
def add_user(site):
    return render_template("add_user.html", sitename=site)


# function to add new client user to db
@app.route("/addUserToDB/<site>", methods=['POST'])
def addclient(site):
    # adding new users to db
    con = sqlite3.connect('mydatabase.db')

    cursor = con.cursor()

    user = request.form['username']
    passwrd = request.form['password']

    cursor.execute("insert into table1_client1users values (?, ?, 0, ?)", (user, passwrd, site))

    con.commit()

    con.close()

    return 'Request to add new user submitted'


if __name__ == "__main__":
    app.run()
