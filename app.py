from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào, đây là ứng dụng đầu tiên tôi viết Flask on Render!"

if __name__ == '__main__':
    app.run()
