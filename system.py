from flask import Flask,render_template,request,session,redirect,url_for
app:Flask=Flask(__name__)
stations=["上郡","有年","播州赤穂","坂越","西相生","相生","竜野","網干","はりま勝原","英賀保","手柄山平和公園","姫路",
"加古川","西明石","明石","神戸","三ノ宮","芦屋","尼崎","大阪","新大阪","高槻","京都","山科","大津","石山","南草津","草津","守山","野洲","近江八幡","能登川","彦根","米原","坂田","田村","長浜","虎姫","河毛","高月","木ノ本","余呉","近江塩津","新疋田","敦賀","大津京","比叡山坂本","堅田","近江舞子","北小松","近江高島","安曇川","新旭","近江今津","近江中庄","マキノ","永原"]
app.secret_key="secret_key_here1234567890"
#回答画面
@app.route("/",methods=["GET","POST"])
def index():
    if "answerd" not in session:
        session["answerd"]=[]
    result_q=""
    ans=""
    if request.method=="GET":
        return render_template("answer.html",result_q="")
    elif request.method=="POST":
        ans=request.form.get("answer")
        print(ans)
        user_answerd = session["answerd"]
        if ans=="ギブアップ":
            return redirect(url_for("result"))
        elif (ans in stations) and not(ans in session["answerd"]):
            user_answerd.append(ans)
            session["answerd"]=user_answerd
            result_q="正解"
        elif ans in stations and ans in session["answerd"]:
            result_q="回答済み"
        else:
            result_q="不正解"
        print(result_q)
        print(session["answerd"])
        ans=""
        return render_template("answer.html",result_q=result_q)

@app.route("/result")
def result():
    score=len(session["answerd"])
    session.clear()
    return render_template("result.html",score=score)
if __name__ == "__main__":
    app.run(debug=True)