from app import create_app  
from dotenv import load_dotenv

import os

load_dotenv()

if __name__=="__main__":

    app=create_app()
    
    app.run(debug=True,port=5001)