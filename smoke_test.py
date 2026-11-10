from pathlib import Path
import json, re, subprocess
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
app=(root/'app.js').read_text(encoding='utf-8')
data_js=(root/'data'/'codigos.js').read_text(encoding='utf-8')
assert 'data/codigos.js' in html and 'app.js' in html and 'styles.css' in html
payload=data_js.split('window.LEGAL_DATA = ',1)[1].rsplit(';',1)[0]
data=json.loads(payload)
assert len(data['cc']['arts'])>2000 and len(data['cp']['arts'])>1000
for fn in ['inicio','curso','codigo','ruta','caseLab','jurisprudencia','practica','prog','saveCase','saveJuris','imp','exportBackup']:
    assert re.search(r'function '+fn+r'\s*\(',app), fn
subprocess.run(['node','--check',str(root/'app.js')],check=True)
subprocess.run(['node','--check',str(root/'data'/'codigos.js')],check=True)
print('OK: estructura, base legislativa JSON, módulos principales y sintaxis JavaScript.')
print(f"Artículos incluidos: CC {len(data['cc']['arts'])} | CPC {len(data['cp']['arts'])}")
