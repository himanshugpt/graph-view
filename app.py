import json

from flask import Flask, render_template
from metadata_dao import Metadata_Dao

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/metadata")
def get_metadata():
    metadata_dao = Metadata_Dao()
    metadata_list = metadata_dao.fetchAllMetadata()
    json_string = json.dumps([ob.__dict__ for ob in metadata_list], default=str)
    print(json_string)
    return json_string

if __name__ == "__main__":
    app.run(debug=True)
