from application import app

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'fdb'
    }
connection = mysql.connector.connect(**config)
