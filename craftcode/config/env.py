import os

from craftcode.config import settings


def load_env_file(env_path):
    if not os.path.isfile(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as env_file:
        for raw_line in env_file:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'"")
            os.environ.setdefault(key, value)


def load_paths(project_root):
    env_path = os.path.join(project_root, ".env")
    load_env_file(env_path)
    input_path = os.environ.get("input") or os.environ.get("INPUT_PATH") or settings.DEFAULT_INPUT_PATH
    output_path = os.environ.get("output") or os.environ.get("OUTPUT_PATH") or settings.DEFAULT_OUTPUT_PATH
    return os.path.normpath(input_path), os.path.normpath(output_path)
