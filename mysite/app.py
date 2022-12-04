from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
import sqlalchemy
=======
from sqlalchemy import func
>>>>>>> e6452c2cc106c77376477854009e57e88da312e8
from flask import Flask, request, render_template,json,redirect,url_for
from datetime import datetime,date
import os
import time

os.environ["TZ"] = "America/Recife"
time.tzset()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://K9Racao:projeto2022@K9Racao.mysql.pythonanywhere-services.com/K9Racao$default'
db = SQLAlchemy(app)

class funcionario(db.Model):
    cpf = db.Column(db.String(14),primary_key=True)
    nome= db.Column(db.String(70),nullable=False)
    telefone = db.Column(db.String(30),nullable=False)
    logins = db.relationship('login',cascade="all,delete", backref='funcionario', lazy=True)
    venda = db.relationship('venda',cascade="all,delete", backref='funcionario', lazy=True)
    funcio_cpf = db.relationship('funcionarios_has_loja_racoes', cascade='all,delete' ,backref='login', lazy=True)

    def to_json(self):
        return {"cpf":self.cpf,"nome":self.nome,"telefone":self.telefone,"login":self.logins,"venda":self.venda,"funcio_cpf":self.funcio_cpf}

class login(db.Model):
    usuario = db.Column(db.String(45),primary_key=True)
    senha= db.Column(db.String(45),nullable=False)
    cpf_funcionario = db.Column(db.String(14), db.ForeignKey('funcionario.cpf', onupdate="cascade", ondelete="cascade"), nullable=False,primary_key=True)


    def to_json(self):
        return {"usuario":self.usuario,"senha":self.senha,"cpf_funcionario":self.cpf_funcionario}

class loja_racao(db.Model):
    cnpj = db.Column(db.String(18),primary_key=True)
    telefone = db.Column(db.String(45), nullable=False)
    abertura = db.Column(db.Time, nullable=False)
    fechamento = db.Column(db.Time, nullable=False)
    enderecos = db.relationship('endereco', cascade='all,delete' ,backref='loja_racao', lazy=True)

    def to_json(self):
        return {"cnpj":self.cnpj,"telefone":self.telefone,"abertura":self.abertura,"fechamento":self.fechamento,"endereço":self.endereco}

class endereco(db.Model):
    UF = db.Column(db.String(2),nullable=False)
    cidade = db.Column(db.String(45), nullable=False)
    bairro = db.Column(db.String(45), nullable=False)
    rua = db.Column(db.String(70), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    comp = db.Column(db.String(60), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    cnpj_loja_racao = db.Column(db.String(18), db.ForeignKey('loja_racao.cnpj', onupdate="cascade", ondelete="cascade"), nullable=False,primary_key=True)

    def to_json(self):
        return {"UF":self.UF,"cidade":self.cidade,"bairro":self.bairro,"rua":self.rua,"numero":self.numero,"comp":self.comp,"cep":self.cep,
        "cpj_loja_racao":self.cnpj_loja_racao}

class funcionarios_has_loja_racoes(db.Model):
      cpf_funcionario = db.Column(db.String(14), db.ForeignKey('funcionario.cpf', onupdate="cascade", ondelete="cascade"), nullable=False,primary_key=True)
      cnpj_loja_racao = db.Column(db.String(18), db.ForeignKey('loja_racao.cnpj', onupdate="cascade", ondelete="cascade"), nullable=False,primary_key=True)

      def to_json(self):
        return {"cpj_loja_racao":self.cnpj_loja_racao,"cpf_funcionario":self.cpf_funcionario}

class venda(db.Model):
    id_venda = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.DateTime,nullable=False)
    valor_venda = db.Column(db.Numeric(10,2),nullable=False)
    desconto = db.Column(db.Numeric(10,2),nullable=False)
    cpf_funcionario = db.Column(db.String(14), db.ForeignKey('funcionario.cpf', onupdate="cascade", ondelete="cascade"), nullable=False)
    itens = db.relationship('itens_venda', cascade='all,delete' ,backref='venda', lazy=True)

    def to_json(self):
        return {"id_venda":self.id_venda,"data":self.data,"valor":self.valor_venda,"desconto":self.desconto,"cpf_funcionario":self.cpf_funcionario}

class produto(db.Model):
    id_produto = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(45),nullable=False)
    quantidade = db.Column(db.Numeric(6,2),nullable=False)
    categoria = db.Column(db.String(45),nullable=False)
    marca = db.Column(db.String(45),nullable=False)
    valor = db.Column(db.Numeric(6,2),nullable=False)
    validade = db.Column(db.Date,nullable=False)
    itens = db.relationship('itens_venda', cascade='all,delete' ,backref='produto', lazy=True)
    compras = db.relationship('compras', cascade='all,delete' ,backref='produto', lazy=True)
    pagamentos = db.relationship('forma_pag_comp', cascade='all,delete' ,backref='produto', lazy=True)

    def to_json(self):
        return {"id_produto":self.id_produto,"nome":self.nome,"quantidade":self.quantidade,
        "categoria":self.categoria,"marca":self.marca,"valor":self.valor,"validade":self.validade,"itens":self.itens,"compras":self.compras,
        "pagamentos":self.pagamentos}

class itens_venda(db.Model):
      quantidade = db.Column(db.Numeric(6,2),nullable=False)
      venda_id_venda = db.Column(db.Integer, db.ForeignKey('venda.id_venda', onupdate="cascade", ondelete="cascade"),primary_key=True)
      produto_id_produto = db.Column(db.Integer,db.ForeignKey('produto.id_produto', onupdate="cascade", ondelete="cascade"),primary_key=True)

      def to_json(self):
        return {"quantidade":self.quantidade,"venda_id_venda":self.venda_id_venda,"produto_id_produto":self.produto_id_produto}

class fornecedores(db.Model):
   cnpj = db.Column(db.String(18),primary_key=True)
   nome = db.Column(db.String(45),nullable=False)
   telefone = db.Column(db.String(45),nullable=False)
   fornecedores_cnpj = db.relationship('compras', cascade='all,delete' ,backref='fornecedores', lazy=True)
   pagamentos = db.relationship('forma_pag_comp', cascade='all,delete' ,backref='fornecedores', lazy=True)

   def to_json(self):
        return {"cnpj":self.cnpj,"nome":self.nome,"telefone":self.telefone,"fornecedores_cnpj":self.fornecedores_cnpj,"pagamentos":self.pagamentos}

class compras(db.Model):
    id_compra = db.Column(db.Integer,primary_key=True)
    quantidade = db.Column(db.Numeric(6,2),nullable=False)
    data = db.Column(db.Date,nullable=False)
    valor = db.Column(db.Numeric(10,2),nullable=False)
    produtos_id_produto = db.Column(db.Integer,db.ForeignKey('produto.id_produto', onupdate="cascade", ondelete="cascade"),primary_key=True)
    cnpj_fornecedores = db.Column(db.String(18),db.ForeignKey('fornecedores.cnpj', onupdate="cascade", ondelete="cascade"),primary_key=True)

    def to_json(self):
        return {"id_compra":self.id_compra,"quantidade":self.quantidade,"data":self.data,"valor":self.valor,"produto_id_produto":self.produto_id_produto,
                "cnpj_forncedores":self.cnpj_forncedores}

class forma_pag_comp(db.Model):
    id_forma_pag_comp = db.Column(db.Integer,primary_key=True)
    tipo = db.Column(db.String(45),nullable=False)
    valor = db.Column(db.Numeric(6,2),nullable=False)
    compras_id_compra = db.Column(db.Integer,db.ForeignKey('compras.id_compra', onupdate="cascade", ondelete="cascade"),nullable=False)
    compras_produtos_id_produto = db.Column(db.Integer,db.ForeignKey('produto.id_produto', onupdate="cascade", ondelete="cascade"),nullable=False)
    compras_fornecedores_cnpj = db.Column(db.String(18),db.ForeignKey('fornecedores.cnpj', onupdate="cascade", ondelete="cascade"),nullable=False)

    def to_json(self):
        return {"id_forma_pag_comp":self.id_forma_pag_comp,"tipo":self.tipo,"valor":self.valor,"compras_id_compra":self.compras_id_compra,
        "compras_produtos_id_produto":self.compras_produtos_id_produto,"compras_fornecedores_cnpj":self.compras_fornecedores_cnpj}

@app.route('/')
def login_usuario():
    return render_template('login.html')

@app.route('/principal', methods = ['GET','POST'])
def principal():
    if request.method == 'POST':
            usuario = request.form['usuario']
            senha = request.form['password']
<<<<<<< HEAD
            acesso = login.query.filter_by(usuario=usuario,senha=sqlalchemy.func.md5(senha)).first()
            if acesso:
=======
            acesso = login.query.filter_by(usuario=usuario).first()
            senhas = login.query.filter_by(senha=func.md5(senha)).first()
            if acesso and senhas:
>>>>>>> e6452c2cc106c77376477854009e57e88da312e8
                return render_template('telainicial.html')
            else:
                return redirect(url_for('login_usuario'))
    else:
        return render_template('telainicial.html')

@app.route('/acrecentar')
def adicionar():
    return render_template('adicionarproduto.html')

@app.route('/editar')
def edicao():
    return render_template('edicaoproduto.html')

@app.route('/sobre')
def sobreproduto():
    return render_template('Sobreproduto.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/registro')
def registro():
    return render_template('registro-venda.html')