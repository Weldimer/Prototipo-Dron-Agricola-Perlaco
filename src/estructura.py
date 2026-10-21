"""Punto de entrada del auditor analítico estructural STR-002 H3.

El valor predeterminado usa el baseline analítico independiente de 60 kg.
No realiza FEA ni certifica la estructura.
"""
try:
    from src.modelo_analitico_estructural import evaluar_modelo
except ModuleNotFoundError:
    from modelo_analitico_estructural import evaluar_modelo


def auditar_estructura(
    path_config="config/baseline_60kg_analitico.json"
):
    return evaluar_modelo(path_config)


if __name__ == "__main__":
    import json
    print(json.dumps(
        auditar_estructura(),
        indent=2,
        ensure_ascii=False,
        sort_keys=True
    ))
