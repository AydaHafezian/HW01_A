from pathlib import Path

# 1. pyproject.toml
pyproject_content = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "airbnb_ops"
version = "0.1.0"
authors = [
  { name="MLOps Student", email="student@example.com" },
]
description = "A reproducible data pipeline for Airbnb analysis"
requires-python = ">=3.10"
dependencies = [
    "pandas",
    "typer",
]

[project.scripts]
airbnb-ops = "airbnb_ops.cli:app"
"""
Path("pyproject.toml").write_text(pyproject_content)

# 2. requirements.txt
requirements_content = """pandas
typer
"""
Path("requirements.txt").write_text(requirements_content)

print("Created pyproject.toml and requirements.txt successfully.")