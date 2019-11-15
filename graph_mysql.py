import mysql.connector
from mysql.connector import errorcode
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

x = []
y = []
z = []


try:
  cnx = mysql.connector.connect(host='localhost',
                                user='root',
                                database='database_research')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    mycursor = cnx.cursor()

    
    mycursor.execute("SELECT UTCTIME, SO2_PPB, TRS_PPB, DATE1 FROM teledyne_instrument LIMIT 720")

    myresult = mycursor.fetchall()

 
    for item in myresult:
        x.append(str(item[0]))
        y.append(item[1])
        z.append(item[2])


    date = myresult[0][3]
    fig, ax = plt.subplots()
    plt.plot(x,y, label='SO2 PPB')
    plt.plot(x,z, label='TRS PPB')
    for index, label in enumerate(ax.xaxis.get_ticklabels()):
        if index % 50 != 0:
            label.set_visible(False)
    plt.xticks(x, x, rotation='vertical')
    plt.xlabel('Time')
    plt.ylabel('PPB')
    plt.title(date)
    plt.savefig("images/example1.png")
    plt.legend()
    plt.show()