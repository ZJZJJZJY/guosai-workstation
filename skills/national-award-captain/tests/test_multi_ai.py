"""test_multi_ai.py — 零依赖自测：python tests/test_multi_ai.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "multi_ai")))

from multi_ai import call_llm, load_config, resolve_provider  # noqa: E402


def main():
    cfg_path = os.path.join(HERE, "..", "multi_ai", "config.example.json")
    cfg = load_config(cfg_path)
    assert set(("deepseek", "claude", "gpt")) <= set(cfg), "config 缺少本地三模型"
    for name in ("deepseek", "claude", "gpt"):
        p = resolve_provider(cfg, name)
        assert p is not None and p["transport"] == "cli", f"{name} 应解析为本地 CLI"

    # 保留 OpenAI 兼容 API 的回退路径，失败时必须优雅降级。
    legacy = {
        "endpoint": "http://127.0.0.1:1/v1/chat/completions",
        "api_key_env": "TEST_API_KEY",
        "model": "test",
    }
    os.environ["TEST_API_KEY"] = "test-key"
    p = resolve_provider({"legacy": legacy}, "legacy")
    assert p is not None and p["api_key"] == "test-key", "API 回退 provider 应解析成功"
    assert call_llm(p, "s", "u", timeout=0.5) is None, "失败应返回 None（优雅降级）"

    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()
