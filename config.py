# -*- coding: utf-8 -*-
"""
config.py - SpineCobbAnalyzer configuration management
"""
import os, re, json, sys

def _project_root():
    try:
        exe = os.path.realpath(sys.executable)
        d = os.path.dirname(exe)
        if os.path.isfile(os.path.join(d, "SpineCobbAnalyzer.exe")) or \
           os.path.isfile(os.path.join(d, "Spine_COBB_Analyzer.py")):
            return d
    except Exception:
        pass
    return os.path.dirname(os.path.abspath(__file__))

def load_env(env_path=None):
    if env_path is None:
        env_path = os.path.join(_project_root(), ".env")
    if not os.path.isfile(env_path):
        return {}
    loaded = {}
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'" + '"' + "'"):
                value = value[1:-1]
            if key:
                os.environ[key] = value
                loaded[key] = value
    return loaded

def resolve_config(config_path=None):
    if config_path is None:
        config_path = os.path.join(_project_root(), "config.json")
    if not os.path.isfile(config_path):
        return {}
    with open(config_path, "r", encoding="utf-8") as f:
        text = f.read()
    import re
    text = re.sub(r"\${(\w+)}", lambda m: os.environ.get(m.group(1), m.group(0)), text)
    return json.loads(text)
