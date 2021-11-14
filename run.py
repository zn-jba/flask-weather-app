import sys

from app import create_app
from app import db
from app.models.city import City

app = create_app()


def main():
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()


if __name__ == "__main__":
    main()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "City": City
    }
