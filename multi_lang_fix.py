import json
import os
import re
import shutil
import sys

# Language Dictionaries
LANG_TERMS = {
    "es": {
        "workflow": "Flujo de trabajo", "invoice": "Factura", "purchase": "Compra", "order": "Pedido",
        "settings": "Configuración", "export": "Exportar", "import": "Importar", "supplier": "Proveedor",
        "approval": "Aprobación", "dashboard": "Tablero", "table": "Tabla", "permission": "Permiso",
        "email": "Correo electrónico", "error": "Error", "docbits": "DocBits", "image": "Imagen",
        "button": "Botón", "card": "Tarjeta", "rule": "Regla", "start": "Inicio", "end": "Fin",
        "new": "Nuevo", "edit": "Editar", "delete": "Eliminar", "save": "Guardar", "cancel": "Cancelar"
    },
    "fr": {
        "workflow": "Workflow", "invoice": "Facture", "purchase": "Achat", "order": "Commande",
        "settings": "Paramètres", "export": "Exporter", "import": "Importer", "supplier": "Fournisseur",
        "approval": "Approbation", "dashboard": "Tableau de bord", "table": "Tableau", "permission": "Permission",
        "email": "E-mail", "error": "Erreur", "docbits": "DocBits", "image": "Image",
        "button": "Bouton", "card": "Carte", "rule": "Règle", "start": "Début", "end": "Fin",
        "new": "Nouveau", "edit": "Modifier", "delete": "Supprimer", "save": "Enregistrer", "cancel": "Annuler"
    },
    "it": {
        "workflow": "Flusso di lavoro", "invoice": "Fattura", "purchase": "Acquisto", "order": "Ordine",
        "settings": "Impostazioni", "export": "Esporta", "import": "Importa", "supplier": "Fornitore",
        "approval": "Approvazione", "dashboard": "Dashboard", "table": "Tabella", "permission": "Permesso",
        "email": "E-mail", "error": "Errore", "docbits": "DocBits", "image": "Immagine",
        "button": "Pulsante", "card": "Scheda", "rule": "Regola", "start": "Inizio", "end": "Fine",
        "new": "Nuovo", "edit": "Modifica", "delete": "Elimina", "save": "Salva", "cancel": "Annulla"
    },
    "pl": {
        "workflow": "Przepływ pracy", "invoice": "Faktura", "purchase": "Zakup", "order": "Zamówienie",
        "settings": "Ustawienia", "export": "Eksport", "import": "Import", "supplier": "Dostawca",
        "approval": "Zatwierdzenie", "dashboard": "Pulpit", "table": "Tabela", "permission": "Uprawnienie",
        "email": "E-mail", "error": "Błąd", "docbits": "DocBits", "image": "Obraz",
        "button": "Przycisk", "card": "Karta", "rule": "Reguła", "start": "Start", "end": "Koniec",
        "new": "Nowy", "edit": "Edytuj", "delete": "Usuń", "save": "Zapisz", "cancel": "Anuluj"
    },
    "pt": {
        "workflow": "Fluxo de trabalho", "invoice": "Fatura", "purchase": "Compra", "order": "Pedido",
        "settings": "Configurações", "export": "Exportar", "import": "Importar", "supplier": "Fornecedor",
        "approval": "Aprovação", "dashboard": "Painel", "table": "Tabela", "permission": "Permissão",
        "email": "E-mail", "error": "Erro", "docbits": "DocBits", "image": "Imagem",
        "button": "Botão", "card": "Cartão", "rule": "Regra", "start": "Início", "end": "Fim",
        "new": "Novo", "edit": "Editar", "delete": "Excluir", "save": "Salvar", "cancel": "Cancelar"
    },
    "nl": {
        "workflow": "Workflow", "invoice": "Factuur", "purchase": "Aankoop", "order": "Bestelling",
        "settings": "Instellingen", "export": "Exporteren", "import": "Importeren", "supplier": "Leverancier",
        "approval": "Goedkeuring", "dashboard": "Dashboard", "table": "Tabel", "permission": "Toestemming",
        "email": "E-mail", "error": "Fout", "docbits": "DocBits", "image": "Afbeelding",
        "button": "Knop", "card": "Kaart", "rule": "Regel", "start": "Start", "end": "Einde",
        "new": "Nieuw", "edit": "Bewerken", "delete": "Verwijderen", "save": "Opslaan", "cancel": "Annuleren"
    },
    "tr": {
        "workflow": "İş akışı", "invoice": "Fatura", "purchase": "Satın alma", "order": "Sipariş",
        "settings": "Ayarlar", "export": "Dışa aktar", "import": "İçe aktar", "supplier": "Tedarikçi",
        "approval": "Onay", "dashboard": "Gösterge Paneli", "table": "Tablo", "permission": "İzin",
        "email": "E-posta", "error": "Hata", "docbits": "DocBits", "image": "Görüntü",
        "button": "Düğme", "card": "Kart", "rule": "Kural", "start": "Başla", "end": "Bitir",
        "new": "Yeni", "edit": "Düzenle", "delete": "Sil", "save": "Kaydet", "cancel": "İptal"
    }
}

ASSET_DIRS = ['.gitbook/assets', 'readme/.gitbook/assets']

def generate_alt_text(filename, lang_code):
    name_no_ext = os.path.splitext(filename)[0]
    parts = name_no_ext.split('_')
    terms = LANG_TERMS.get(lang_code, {})
    translated_parts = []
    for part in parts:
        translated_parts.append(terms.get(part, part.capitalize()))
    return " ".join(translated_parts)

def process_branch_updates(lang_code):
    print(f"Processing updates for language: {lang_code}")
    with open('filename_mapping.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        
    updated_files_count = 0
    
    # 1. Rename Files
    for old_name, new_name in mapping.items():
        renamed = False
        for asset_dir in ASSET_DIRS:
            old_path = os.path.join(asset_dir, old_name)
            new_path = os.path.join(asset_dir, new_name)
            
            if os.path.exists(old_path):
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_name} -> {new_name}")
                    renamed = True
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")
            elif os.path.exists(new_path):
                renamed = True
        
    # Scan and Update Markdown
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    for old_name, new_name in mapping.items():
                        if old_name in content:
                            alt_text = generate_alt_text(new_name, lang_code)
                            escaped_old = re.escape(old_name)
                            escaped_new = new_name
                            
                            pattern = r'([/(])' + escaped_old + r'([)"\'])'
                            content = re.sub(pattern, r'\1' + escaped_new + r'\2', content)
                            
                            escaped_new_re = re.escape(new_name)
                            def update_md_alt(match):
                                return f'![{alt_text}]({match.group(2)})'
                            
                            # Using triple quotes for regex patterns to be safe
                            content = re.sub(r'''!\[(.*?)\]\(((?:[^)]*/)?{0})\)'''.format(escaped_new_re), update_md_alt, content)
                            
                            def update_html_alt(match):
                                return f'{match.group(1)}{alt_text}{match.group(3)}'
                            
                            content = re.sub(r'''(<img\s+[^>]*src=["\'].*?{0}["\'][^>]*alt=["\'])(.*?)(["\'])'''.format(escaped_new_re), update_html_alt, content)
                    
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated_files_count += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
                    
    print(f"Updated {updated_files_count} markdown files.")

if __name__ == "__main__":
    try:
        with open('.git/HEAD', 'r') as f:
            ref = f.read().strip()
            branch = ref.split('/')[-1]
            
        print(f"Detected branch: {branch}")
        if branch in LANG_TERMS:
            process_branch_updates(branch)
        else:
            print(f"Branch '{branch}' not in supported languages list. Using keys/default.")
            pass
            
    except Exception as e:
        print(f"Error: {e}")
