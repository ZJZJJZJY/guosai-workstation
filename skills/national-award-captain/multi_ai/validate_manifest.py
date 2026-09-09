"""Validate a project's final_results_manifest.json before paper writing."""
import argparse
import json
from pathlib import Path


def validate(manifest_path, project_root):
    data = json.loads(Path(manifest_path).read_text(encoding="utf-8-sig"))
    if data.get("schema_version") != "1.0":
        raise ValueError("unsupported schema_version")
    items = data.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("items must be a non-empty list")
    root = Path(project_root).resolve()
    for item in items:
        required = ("qi_id", "result_file", "validation_report", "script", "status", "reviewed_by", "reproduce_command")
        missing = [key for key in required if not item.get(key)]
        if missing:
            raise ValueError(f"{item.get('qi_id', '<unknown>')}: missing {', '.join(missing)}")
        if item["status"] != "accepted":
            raise ValueError(f"{item['qi_id']}: status is {item['status']}, expected accepted")
        if not {"deepseek", "claude", "gpt"}.issubset(set(item["reviewed_by"])):
            raise ValueError(f"{item['qi_id']}: reviewed_by must include deepseek, claude, gpt")
        for key in ("result_file", "validation_report", "script"):
            path = (root / item[key]).resolve()
            if root not in path.parents and path != root:
                raise ValueError(f"{item['qi_id']}: path escapes project root: {item[key]}")
            if not path.is_file():
                raise ValueError(f"{item['qi_id']}: missing file {item[key]}")
    return len(items)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()
    try:
        count = validate(args.manifest, args.project_root)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(f"MANIFEST OK: {count} accepted item(s)")


if __name__ == "__main__":
    main()
