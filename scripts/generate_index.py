import os

# 設定: 知識ファイルのルートディレクトリ
KNOWLEDGE_DIR = 'knowledge'
# 設定: プロジェクトファイルのディレクトリ
PROJECTS_DIR = 'projects'
# 設定: Inboxディレクトリ
INBOX_DIR = 'inbox'
# 出力するファイル名
INDEX_FILE = 'index.ttl'

# index.ttl のヘッダー（固定部分）
HEADER = """@prefix ex: <http://example.com/aykg#> .
@prefix schema: <http://schema.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

##################################################################
# AY-Knowledge-Graph: Root Index (Auto-Generated)
# このファイルは scripts/generate_index.py によって自動生成されています。
# 手動で編集しても上書きされるためご注意ください。
##################################################################

ex:GraphRAGIndex a rdfs:Class ;
    rdfs:label "AY Knowledge Graph Root Index" ;
    rdfs:comment "知識グラフのルート。ここから各領域の知識へリンクします。" .

ex:GraphRAG a rdfs:Class ; rdfs:label "知識領域" .
ex:Project a rdfs:Class ; rdfs:label "プロジェクト" .
ex:InboxItem a rdfs:Class ; rdfs:label "未整理アイテム" .
"""

def find_ttl_files(root_dir):
    """指定されたディレクトリ以下の.ttlファイルを再帰的に探す"""
    ttl_files = []
    if not os.path.exists(root_dir):
        return ttl_files
        
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.ttl'):
                # パスを構築
                full_path = os.path.join(root, file)
                # Windowsのパス区切り文字を / に統一
                clean_path = full_path.replace(os.sep, '/')
                ttl_files.append(clean_path)
    return ttl_files

def generate_turtle_entry(file_path, category):
    """1つのファイルに対するTurtleエントリを生成する"""
    # ファイル名からIDっぽいものを作る (例: knowledge/me.ttl -> MeGraph)
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    # 先頭を大文字に、記号を除去
    node_id = base_name.capitalize().replace('_', '').replace('-', '') + "Node"
    
    entry = f"""
ex:{node_id} a ex:{category} ;
    rdfs:label "{base_name} ({category})" ;
    ex:entryFile "{file_path}" .
"""
    return entry

def main():
    content = HEADER
    
    # 1. Knowledgeフォルダの処理
    print(f"Scanning {KNOWLEDGE_DIR}...")
    files = find_ttl_files(KNOWLEDGE_DIR)
    if files:
        content += "\n# --- Domain Knowledge (GraphRAG) ---\n"
        for f in files:
            content += generate_turtle_entry(f, "GraphRAG")

    # 2. Projectsフォルダの処理
    print(f"Scanning {PROJECTS_DIR}...")
    files = find_ttl_files(PROJECTS_DIR)
    if files:
        content += "\n# --- Active Projects ---\n"
        for f in files:
            content += generate_turtle_entry(f, "Project")

    # 3. Inboxフォルダの処理
    print(f"Scanning {INBOX_DIR}...")
    files = find_ttl_files(INBOX_DIR)
    if files:
        content += "\n# --- Inbox (Drafts) ---\n"
        for f in files:
            content += generate_turtle_entry(f, "InboxItem")

    # ファイルに書き出し
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully generated {INDEX_FILE}")

if __name__ == '__main__':
    main()
