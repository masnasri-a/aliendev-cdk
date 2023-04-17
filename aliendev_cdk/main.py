import typer
from aliendev_cdk.service import loginService

app = typer.Typer()

@app.command("register")
def register():
    print("register")
    
@app.command("login")
def login():
    loginService.login()


if __name__ == "__main__":
    app()