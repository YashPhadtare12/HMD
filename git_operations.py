import subprocess
import os

def commit_and_push_changes():
    """Commit and push changes to the GitHub repository."""
    try:
        # Configure Git user
        subprocess.run(['git', 'config', '--global', 'user.name', 'YashPhadtare12'], check=True)
        subprocess.run(['git', 'config', '--global', 'user.email', 'yashphadtare211@gmail.com'], check=True)

        # Add the file to the staging area
        subprocess.run(['git', 'add', 'data.json'], check=True)

        # Commit the changes
        subprocess.run(['git', 'commit', '-m', 'Update data.json with new entries'], check=True)

        # Push the changes to the remote repository using the token
        repo_url = 'https://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@github.com/YashPhadtare12/HMD.git'
        subprocess.run(['git', 'push', repo_url, 'main'], check=True)

        print("Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes to GitHub: {e}")
