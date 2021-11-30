from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/classes/main.py", pty=True)

@task
def test(ctx):
	ctx.run("pytest src")

@task
def coverage_report(ctx):
	ctx.run("coverage report -m")
