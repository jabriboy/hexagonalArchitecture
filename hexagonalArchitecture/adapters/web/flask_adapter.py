from flask import Flask, request, jsonify
from application.interfaces.venda_repository import IVendaRepository

class FlaskAdapter:
    def __init__(self, venda_repository: IVendaRepository):
        self.app = Flask(__name__)
        self.venda_repository = venda_repository
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/vendas', methods=['POST'])
        def create_venda():
            data = request.json
            # Aqui você deve implementar a lógica para criar uma venda
            # Exemplo: venda = self.venda_repository.create(data)
            return jsonify({"message": "Venda criada com sucesso!"}), 201

        @self.app.route('/vendas/<int:venda_id>', methods=['GET'])
        def get_venda(venda_id):
            # Aqui você deve implementar a lógica para obter uma venda
            # Exemplo: venda = self.venda_repository.get(venda_id)
            return jsonify({"message": "Venda obtida com sucesso!"}), 200

    def run(self):
        self.app.run(debug=True)