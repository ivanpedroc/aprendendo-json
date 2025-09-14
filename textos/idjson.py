import json
import os

# Pasta onde estão os arquivos .txt
pasta_entrada = "."

# Listar todos os arquivos .txt da pasta
arquivos_txt = [f for f in os.listdir(pasta_entrada) if f.endswith(".txt")]

if not arquivos_txt:
    print("Nenhum arquivo .txt encontrado na pasta.")
else:
    for arquivo_txt in arquivos_txt:
        # Nome do arquivo JSON de saída
        arquivo_json = os.path.splitext(arquivo_txt)[0] + ".json"
        
        # Lista para armazenar os dados
        dados = []

        try:
            # Tenta abrir e ler o arquivo TXT com encoding utf-8
            with open(os.path.join(pasta_entrada, arquivo_txt), "r", encoding="utf-8") as f:
                linhas = [linha.strip() for linha in f if linha.strip()]
        except UnicodeDecodeError:
            # Se falhar, tenta com encoding latin-1
            print(f"Erro de codificação com UTF-8 em '{arquivo_txt}'. Tentando com LATIN-1...")
            with open(os.path.join(pasta_entrada, arquivo_txt), "r", encoding="latin-1") as f:
                linhas = [linha.strip() for linha in f if linha.strip()]
        
        # Processar 2 linhas por item
        for i in range(0, len(linhas) - len(linhas) % 2, 2):
            item = {
                "ingles": linhas[i],
                "portugues": linhas[i + 1]
            }
            dados.append(item)

        # Salvar no arquivo JSON
        with open(os.path.join(pasta_entrada, arquivo_json), "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print(f"Arquivo '{arquivo_json}' criado com sucesso com {len(dados)} itens!")

print("Conversão concluída para todos os arquivos .txt da pasta.")