import subprocess


def git_diff(base_branch, target_branch):
    try:
        result = subprocess.run(
            ["git", "diff", base_branch, target_branch],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise Exception(f"Error running git diff: {result.stderr}")

        return result.stdout

    except Exception as e:
        return str(e)
