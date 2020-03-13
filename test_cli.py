from click.testing import CliRunner
from hello import make_apple


#search(path, ftype):
    
def test_make_apple():
  runner = CliRunner()
  result = runner.invoke(make_apple, ['--name', 'Larry'])
  assert result.exit_code == 0
  assert 'Larry-apple' in result.output