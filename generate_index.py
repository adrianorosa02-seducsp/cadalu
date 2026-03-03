import os

def generate():
    # Ignora arquivos do sistema e o próprio script
    ignore = ['.git', '.github', 'index.html', 'generate_index.py']
    
    # Pega as pastas (alunos)
    folders = [d for d in os.listdir('.') if os.path.isdir(d) and d not in ignore]
    folders.sort()

    links_html = "".join([f'<li><a href="./{f}/">{f}</a></li>' for f in folders])

    template = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Portal de Projetos</title>
        <style>
            body {{ font-family: sans-serif; line-height: 1.6; padding: 20px; color: #333; }}
            h1 {{ border-bottom: 2px solid #eee; }}
            ul {{ list-style: none; padding: 0; }}
            li {{ margin: 10px 0; padding: 10px; background: #f9f9f9; border-radius: 5px; }}
            a {{ text-decoration: none; color: #0066cc; font-weight: bold; }}
            a:hover {{ color: #003366; }}
        </style>
    </head>
    <body>
        <h1>📂 Projetos dos Alunos</h1>
        <ul>{links_html}</ul>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == "__main__":
    generate()