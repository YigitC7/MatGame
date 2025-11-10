from flask import Flask, render_template, request, session, url_for, redirect
from random import randint

class Main:
    def __init__(self):
        self.server = Flask(__name__)

        self.server.secret_key = "sfhasjfhsaj"

        @self.server.route("/")
        def home():
            session["DogruCevap"] = 0
            session["YanlisCevap"] = 0

            return render_template("home.html")
        
        @self.server.route("/oyun",methods=["POST","GET"])
        def oyun():
            if request.method == "POST":
                if not (request.form.get("sayi1") and request.form.get("sayi2") and request.form.get("operator")):
                    if "sayi1" in session:
                        pass
                    else:
                        return redirect(url_for("home"))
                    
                try:
                    if int(request.form.get("sayi1")) >= int(request.form.get("sayi2")):
                        return request(url_for("home"))
                except ValueError:
                    return redirect(url_for("home"))
                except TypeError:
                    pass

                try:
                    self.HomeVerileri = [int(request.form.get("sayi1")),int(request.form.get("sayi2")),request.form.get("operator")]
                    session["sayi1"] = self.HomeVerileri[0]
                    session["sayi2"] = self.HomeVerileri[1]
                    session["operator"] = self.HomeVerileri[2]
                except:
                    pass
                if request.form.get("cevap"):
                    if int(request.form.get("cevap")) == eval(session["soru"]):
                        session["DogruCevap"] +=1
                    else:
                        session["YanlisCevap"] +=1 

                session["soru"] = self.soruOlustur(session["sayi1"],session["sayi2"],session["operator"])
                
                
                return render_template("oyun.html",soru=session["soru"].replace("*","x"),dogru=session["DogruCevap"],yanlis=session["YanlisCevap"])
            
            else:
                return redirect(url_for("home"))

        self.server.run(debug=True,port=8888)

    def soruOlustur(self,s1,s2, op):
        self.RandomSoru = [randint(s1,s2),randint(s1,s2)]
        return f"{self.RandomSoru[0]} {op} {self.RandomSoru[1]}"

Main()