"""One-time, authorized retirement of redundant project configuration."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
config=root/'PROJECT_CONFIG.md'
archive=root/'docs/research-notes.md'
if config.exists():
    text=config.read_text(encoding='utf-8')
    note='''# 研究設定與資料限制備查

本檔保留先前 PROJECT_CONFIG.md 的研究專屬資訊，供研究核對與歷史查閱。
它不是另一份必讀開發規範；最新開發規則在 AGENTS.md，操作與必要限制在 README.md，最新狀態在 PROJECT_CONTEXT.md。
以下交付範圍、三層文件與「本批」描述屬於當時狀態，不代表後續授權。原始研究主張仍需回到來源文件核對。

---

'''
    archive.write_text(note+text,encoding='utf-8')
    assert archive.read_text(encoding='utf-8').endswith(text)
    config.unlink()
    print('Preserved former settings in docs/research-notes.md; removed PROJECT_CONFIG.md.')
else:
    print('No redundant configuration file remains; no action.')
