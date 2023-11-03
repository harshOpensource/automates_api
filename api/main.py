from flask import Flask,request
from flask_cors import CORS
from add_email.routes import create_account
from prisma import Prisma



app = Flask(__name__)
CORS(app)


    

@app.route('/')
def index():
    return "Hello World"

@app.route('/create_account', methods=['POST'])
async def accountCreate():
    if request.method == 'POST':
        prisma = Prisma()
        await prisma.connect()
        response = create_account(prisma)
        print(response)

        async def creating():
            create = await prisma.acc.create({
                "name": "Harsh"
            })
            return create

        # Await the 'creating' coroutine
        result = await creating()

        return "Done"  # Return a response after awaiting the 'creating' coroutine
    else:
        return "Wrong method request"