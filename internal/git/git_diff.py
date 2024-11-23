import subprocess


def get_git_diff(branch1, branch2):
    try:
        result = subprocess.run(
            ["git", "diff", branch1, branch2],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
