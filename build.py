from pathlib import Path
import json
R=Path(__file__).parent
data=json.loads((R/'data/portal.json').read_text())
safe=json.dumps(data,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
(R/'index.html').write_text((R/'template.html').read_text().replace('/*PUBLIC_DATA*/',safe))
