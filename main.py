from flask import Flask, redirect
app = Flask(__name__)

# respond "/" request with index.html
@app.route("/")
def send_index():
    return app.send_static_file("index.html")

# respond "/resources/<path:path>" request with
# static file at `path` inside `static` folder
@app.route("/resources/<path:path>")
def send_resources(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run()
