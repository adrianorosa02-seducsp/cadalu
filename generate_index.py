import os

def generate():
    # Arquivos e pastas para ignorar no portal
    ignore = ['.git', '.github', 'index.html', 'generate_index.py', '.gitignore']
    
    # Pega tudo que está no diretório atual
    items = [f for f in os.listdir('.') if f not in ignore]
    items.sort()

    links_html = ""
    for item in items:
        # Verifica se é pasta ou arquivo para colocar um ícone diferente
        icon = "📁" if os.path.isdir(item) else "📄"
        # Adiciona a barra no final se for pasta para garantir o caminho correto
        suffix = "/" if os.path.isdir(item) else ""
        links_html += f'<li><a href="./{item}{suffix}">{icon} {item}</a></li>'

    if not links_html:
        links_html = "<li>Nenhum arquivo encontrado no deploy.</li>"

    template = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portal de Arquivos</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; padding: 30px; background: #f4f7f6; color: #333; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 10px; shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            ul {{ list-style: none; padding: 0; }}
            li {{ margin: 8px 0; padding: 12px; background: #fff; border: 1px solid #eee; border-radius: 6px; transition: 0.2s; }}
            li:hover {{ background: #e9ecef; transform: translateX(5px); }}
            a {{ text-decoration: none; color: #2980b9; font-weight: 500; display: block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📂 Conteúdo do Projeto</h1>
            <ul>{links_html}</ul>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == "__main__":
    generate()