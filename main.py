# Importa bibliotecas para executar outros scripts
import subprocess
import sys

# Lista de etapas do pipeline
# Primeiro gera os dados, depois transforma
steps = [
    "scripts/extract.py",
    "scripts/transform.py"
]

# Executa cada etapa em sequência
for step in steps:
    print(f"Executando {step}...")

    # Executa o script usando o mesmo Python do ambiente virtual
    result = subprocess.run(
        [sys.executable, step],
        capture_output=True,
        text=True
    )

    # Se o script falhar, mostra o erro e interrompe o pipeline
    if result.returncode != 0:
        print(f"Erro ao executar {step}")
        print(result.stderr)
        sys.exit(1)

    # Se der certo, mostra a saída do script
    print(result.stdout)

# Se tudo correr bem, mostra mensagem final
print("Pipeline executado com sucesso.")