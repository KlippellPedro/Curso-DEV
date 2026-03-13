from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def home():
    n1= 10
    n2= 20
    n3= 30
    n4= 40
    total= n1+n2+n3+n4
    resultado= total/4
    resultado_form= f"{resultado:.2f}"

    return render_template(
        "index.html",
        n1=n1,
        n2=n2,
        n3=n3,
        n4=n4,
        resultado=resultado,
        resultado_form=resultado_form
    )
if __name__=="__main__":
    app.run(debug=True)