import subprocess
import questionary


def get_available_branches():
    try:
        result = subprocess.run(
            ["git", "branch"],
            capture_output=True,
            text=True,
            check=True,
        )
        branches = [b.strip("* ") for b in result.stdout.split("\n") if b]
        return branches
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def get_git_diff(branch1=None, branch2=None):
    try:
        branches = get_available_branches()

        if not branches or isinstance(branches, str):
            return "Error: No se pudieron obtener las ramas"

        if not branch1 or not branch2:
            branch1 = questionary.select(
                "Selecciona la primera rama:", choices=branches
            ).ask()

            remaining_branches = [b for b in branches if b != branch1]

            branch2 = questionary.select(
                "Selecciona la segunda rama:", choices=remaining_branches
            ).ask()

        result = subprocess.run(
            ["git", "diff", branch1, branch2],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"
