from flask import Flask
import json
import requests

app = Flask(__name__)


@app.route("/<name>/<currency>")
def profile(name, currency):
    response1 = requests.get("https://api.niami.io/hsd/"+name)
    response = response1.json()
    address = None
    if response["success"] == True:
        data = response["data"]

        if name == data["name"]:
            dnsdata = data["dnsData"]
            for i in dnsdata:
                if i["type"] == "TXT":
                    long = i['txt']
                    if long[0].startswith("profile") == True:
                        wallet = long[0].replace("profile", "")
                        if "wallet" in wallet:
                            wallet = wallet.replace("wallet=", "")
                            wallet = wallet.replace(" ", "")
                            if wallet.startswith(currency):
                                address = wallet.replace(currency, "")
                            else:
                                address = ""
        else:
            address = ""
    return address
