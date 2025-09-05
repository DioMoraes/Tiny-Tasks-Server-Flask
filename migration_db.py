import psycopg2

try:
    query = """
    
    CREATE TABLE IF NOT EXISTS subscriber (
      id SERIAL PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      telephone VARCHAR(20),
      email VARCHAR(120) UNIQUE NOT NULL,
      country VARCHAR(50),
      languages VARCHAR(200),
      gender VARCHAR(10)
);
"""
    conn = psycopg2.connect("POSTGREE_URL")

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()   
    print("Conexão bem-sucedida")

except Exception as e:
    print(f"Erro na conexão: {e}")
    
    

