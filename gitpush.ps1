# upload_to_github.ps1

# Check if there are any changes to commit
$status = git status --porcelain
if ($status) {
    # Changes exist, proceed with commit and push
    Write-Host "Changes detected. Proceeding with commit and push."

    # Stage all changes
    git add .

    # Prompt for commit message
    $commitMessage = Read-Host -Prompt "Enter your commit message"

    # Commit changes
    git commit -m $commitMessage

    # Push to the current branch
    $currentBranch = git rev-parse --abbrev-ref HEAD
    git push origin $currentBranch

    Write-Host "Changes have been pushed to GitHub successfully."
} else {
    # No changes to commit
    Write-Host "No changes detected. Nothing to commit and push."
}