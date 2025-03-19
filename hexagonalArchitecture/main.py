from application.use_cases.venda_use_case import VendaUseCase
from adapters.database.sqlite_adapter import SQLiteAdapter
from adapters.web.flask_adapter import FlaskAdapter

def main():
    # Initialize the database adapter
    db_adapter = SQLiteAdapter("my_database.db")
    
    # Initialize the use case with the database adapter
    venda_use_case = VendaUseCase(db_adapter)
    
    # Initialize the web adapter (Flask)
    web_adapter = FlaskAdapter(venda_use_case)
    
    # Start the web application
    web_adapter.run()

if __name__ == "__main__":
    main()