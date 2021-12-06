# pylint: disable=all
import esmf_git as git


def test():
    result = git.status(".")
    assert result.__class__.__name__ == "CompletedProcess"
