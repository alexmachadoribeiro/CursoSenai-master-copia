# Formatação de números

# Exemplo básico
numero = 123456.789
formatado = f"{numero:.2f}"
print(f"Número: {numero} - Formatado: {formatado}")  # Saída: 123456.79

# Adicionando separadores de milhares
numero = 1234567890
formatado = f"{numero:,}".replace(",", ".")
print(f"Número: {numero} - Formatado: {formatado}")  # Saída: 1,234,567,890

# Porcentagem
taxa = 0.75
formato = f"{taxa:.2%}"
print(f"Taxa: {taxa} - Formatado: {formato}")  # Saída: 75.00%

# Moeda
valor = 1000
formato = f"R$ {valor:,.2f}".replace(",", ".")
print(f"Valor: {valor} - Formatado: {formato}")  # Saída: R$1,000.00

# Inteiro para decimal
numero_inteiro = 1234
formato = f"{float(numero_inteiro):.2f}"
print(f"Número inteiro: {numero_inteiro} - Formatado: {formato}")  # Saída: 1234.00