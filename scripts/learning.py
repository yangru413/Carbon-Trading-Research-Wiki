"""Retired entry point retained to avoid silently restoring the old course wording.

The research-guide renderer is scripts/build-demo.py.
Editable chapter text lives in content/ and topic metadata in data/topics.json.
"""

def build_learning(*args, **kwargs):
    raise RuntimeError('舊閱讀路徑產生器已停用；請執行 scripts/build-demo.py。')
