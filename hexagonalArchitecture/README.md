# Hexagonal Architecture Project

Este projeto implementa uma arquitetura hexagonal para um sistema de vendas, utilizando Python e SQLite como banco de dados. A estrutura do projeto é organizada em diferentes camadas, permitindo uma separação clara entre a lógica de negócios, a interface do usuário e a persistência de dados.

## Estrutura do Projeto

```
hexagonalArchitecture
├── adapters
│   ├── database
│   │   └── sqlite_adapter.py
│   └── web
│       └── flask_adapter.py
├── application
│   ├── use_cases
│   │   └── venda_use_case.py
│   └── interfaces
│       └── venda_repository.py
├── domain
│   ├── models
│   │   ├── item_de_venda.py
│   │   └── venda.py
│   └── services
│       └── venda_service.py
├── tests
│   ├── test_venda.py
│   └── test_item_de_venda.py
├── main.py
├── requirements.txt
└── my_database.db
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd hexagonalArchitecture
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar a aplicação, execute o seguinte comando:
```
python main.py
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Crie um fork do repositório, faça suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.