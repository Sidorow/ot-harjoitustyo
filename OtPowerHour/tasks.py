from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
	ctx.run("pytest src")

@task
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def lint(ctx):
	ctx.run("pylint src")
