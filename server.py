import os
from flask import Flask
from flask import request

# Khởi tạo Flask Server Backend
app = Flask(__name__)

# Apply Flask CORS
app.config['CORS_HEADERS'] = 'Content-Type'

# http://127.0.0.1/add
# http://127.0.0.1/minus
# http://127.0.0.1/multi
# http://127.0.0.1/div


@app.route('/add', methods=['POST', 'GET'] )
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    kq = a + b
    return 'Kết quả là: ' + str(kq)


@app.route('/minus', methods=['POST','GET'] )
def minus_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    kq = a - b
    return 'Kết quả là: ' + str(kq)


@app.route('/multi', methods=['POST','GET'] )
def multi_process():
    return "Hàm nhân"


@app.route('/div', methods=['POST','GET'] )
def div_process():
    return "Hàm chia"


@app.route('/viethoa', methods=['POST'] )
def viethoa_process():
    s = request.form.get("chuoiinput")
    #s = request.args.get("chuoiinput")
    return s.upper()

@app.route('/', methods=['POST','GET'] )
def home_process():
    return "hihihaha"

@app.route('/hello') #whenever this webserver is called with <hostname:port>/hello then this section is called
def hello(): #The subroutine name that handles the call
	output = 'Hello World'
	return output #Whatever is returned from this subroutine is what is returned to the requester and is shown on the browser page

# Start Backend
if __name__ == '__main__':
    port = int(os.environ.get('PORT',
                              5000))  # The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
    app.run(host='0.0.0.0', port=port)  # Start listening