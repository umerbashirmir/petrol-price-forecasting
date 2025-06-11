from app import create_app
import os 
print("main.py is running ")



app = create_app()

if __name__ == '__main__':
    print("starting flask app")
    port = int(os.environ.get("PORT",5000))
    app.run(host = '0.0.0.0' , port = port)
