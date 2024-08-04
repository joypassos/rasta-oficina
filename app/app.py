from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Funcionario, Cliente, OrdemDeServico, Material

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost/oficina_mecanica"
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/funcionarios", methods=["GET", "POST"])
def funcionarios():
    if request.method == "POST":
        funcionario = Funcionario(nome=request.form["nome"], cpf=request.form["cpf"])
        db.session.add(funcionario)
        db.session.commit()
        return redirect(url_for("funcionarios"))
    funcionarios = Funcionario.query.all()
    return render_template("funcionarios.html", funcionarios=funcionarios)

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == "POST":
        cliente = Cliente(nome=request.form["nome"], cpf=request.form["cpf"])
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("clientes"))
    clientes = Cliente.query.all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/ordens_de_servico", methods=["GET", "POST"])
def ordens_de_servico():
    if request.method == "POST":
        ordem_de_servico = OrdemDeServico(
            cliente_id=request.form["cliente_id"],
            funcionario_id=request.form["funcionario_id"],
            data_de_entrada=request.form["data_de_entrada"],
            data_de_entrega=request.form["data_de_entrega"],
            valor=request.form["valor"]
        )
        db.session.add(ordem_de_servico)
        db.session.commit()
        return redirect(url_for("ordens_de_servico"))
    ordens_de_servico = OrdemDeServico.query.all()
    return render_template("ordens_de_servico.html", ordens_de_servico=ordens_de_servico)

@app.route("/materiais", methods=["GET", "POST"])
def materiais():
    if request.method == "POST":
        material = Material(nome=request.form["nome"], preco=request.form["preco"])
        db.session.add(material)
        db.session.commit()
        return redirect(url_for("materiais"))
    materiais = Material.query.all()
    return render_template("materiais.html", materiais=materiais)

if __name__ == "__main__":
    app.run(debug=True)