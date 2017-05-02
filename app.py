from flask import Flask, render_template
from metadata_dao import Metadata_Dao

app = Flask(__name__)

@app.route("/")
def hello():
    metadataDao = Metadata_Dao()
    metadataDao.fetchAllMetadata()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
