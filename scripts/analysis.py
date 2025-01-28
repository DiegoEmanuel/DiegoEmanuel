import os
from datetime import datetime
from git import Repo

def analyze_commits():
    repo = Repo('.')
    commits = list(repo.iter_commits('main', max_count=5))  # Últimos 5 commits
    today = datetime.now().strftime("%Y-%m-%d")

    # Gera o resumo dos commits
    analysis = f"## 📅 Últimos Commits (gerado em {today})\n"
    for commit in commits:
        message = commit.message.strip()
        date = commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S")
        author = commit.author.name
        analysis += f"- **[{date}]** {message} (por {author})\n"

    # Atualiza o README
    with open('README.md', 'r+') as f:
        content = f.read()
        if "## 📅 Últimos Commits" in content:
            content = content.split("## 📅 Últimos Commits")[0]
        f.seek(0)
        f.write(content + '\n\n' + analysis)
        f.truncate()

if __name__ == "__main__":
    analyze_commits()
