import tomli
import click
from pathlib import Path
from {{cookiecutter.project_slug}} import __version__

@click.group()
def cli():
    pass


@click.command()
def version():
    """show version information"""
    click.echo(f"{{cookiecutter.project_slug}} version is: {__version__}")


@click.command(help="write version to __init__.py and pyproject.toml")
@click.option("--version", help="The new verison!", required=True)
def write(version):
    filepath = "src/ttc/__init__.py"
    with open(filepath, "w") as f:
        f.write(f'__version__ = "{version}"')

    p = Path("./pyproject.toml")
    res = tomli.load(p)
    res["tool"]["poetry"]["version"] = version
    # write back
    with open(p, "w") as f:
        tomli.dump(res, f)


enabled_cmd = [
    version,
    write,
]

for c in enabled_cmd:
    cli.add_command(c)
