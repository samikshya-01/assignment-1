# Part A: Git & Project Foundations

## Git fundamentals

**1. Git has three places a change can live: the working directory, the staging area, and the repository. Describe each, and explain what you would lose if the staging area did not exist.**

Answer: Working directory is where you can edit the files. Staging area is a waiting area where you use git add. before comitting. Repository is where your work history gets saved. If the staging area didn't exist, I would lose the ability to choose which change to commit and everything will be messed up together.

**2. `git init` and `git clone` both leave you with a Git repository. Explain what each one actually does, and give a situation where each is the right choice.**

Answer: git init creates a completely new repository for you to work on while git clone is for cloning the existing repository into your workplace. git init is right choice for new project and git clone for existing project or while collaborating with colleagues.

**3. What does a commit store, and why is "committing" not the same as "saving a file"? Why is Git much less useful if `user.name` and `user.email` are unset or wrong?**

Answer: commit stores a snapshot of files, author, date, message and link to previous commit. Commiting is not the same as saving a file because saving only changes the file on disk not on the history of git. Git is less useful if username or email are unset or wrong because in git, we cannot see who made which change.

**4. `git status`, `git log`, and `git diff` answer three different questions. State the question each one answers, and describe a moment in your workflow where you would reach for each.**

Answer: git status answers for "What's changed?". git log answers for "What happened before?". git diff answers for "Which lines changed exactly?". In my assignment today, I used git status to know if earlier commits were successfully done.

**5. Explain what makes a commit message good. Why is "update" a genuine problem for a team six months later, and when is it worth writing a message body rather than just a summary line?**

Answer: A proper brief sentence which answers both what changed and why makes a commit message good. update is a genuine problem because after 6 months it tells nothing. It is worth writing a message body when the reason isn't familiar to others.

## Remotes and the everyday workflow

**6. Explain the relationship between your local repository and `origin`. What do `push` and `pull` each move, in which direction, and why is pulling before pushing the habit to build?**

Answer: origin is Github copy. push moves what I committed to GitHub while pull moves what GitHub has to my workspace. Pulling before pushing is the habit to build because that will allow us to see what our teamworks have already worked on and what's left to do. 

**7. `git fetch` and `git pull` are not the same command. What is the difference, and when would you deliberately choose `fetch`?**

Answer: git fetch only downloads the changes while git pull downloands and merge right away. I would deliberatly choose fetch to see the changes first rather than merging it directly with git pull to avoid any errors.

## Branching, merging, pull requests

**8. A branch in Git is often described as "just a pointer." Explain what that means, and explain concretely what goes wrong on a team when everyone commits directly to `main`.**

Answer: A branch is just a pointer because git can contain many branches which points to different commit for each. When everyone commits directly to main, it mixes code together causing the code to have many bugs and errors which will be a headache to recover.

**9. A merge conflict happens when two branches change the same lines of the same file. Explain why Git cannot resolve this automatically, what the `<<<<<<<`, `=======`, `>>>>>>>` markers mean, and what you must do to finish the merge.**

Answer: Git doesn't know which version is right because its upto us to decide. <<<<<<< means its my version, ======= means the divider and >>>>>>> means their version. To finish the merge, I have to pick the correct code first then, manually delete the markers then git add and git commit.

**10. You could merge a branch locally with `git merge` and push. What does opening a Pull Request add that a local merge does not? What belongs in a PR description?**

Answer: Pull Request adds review, discussion, comments and automated checks before merging which isn't done by a local merge. The answers to what changed and why and the problem belongs in a PR description.

## Issues

**11. Explain the purpose of labels and assignees on an Issue, and what `Fixes #12` in a merged PR does. Why is linking work to Issues better than closing them by hand?**

Answer: The purpose of labels is to label by type and priority, and the purpose of assignees is to see who is responsible. Fixes #12 in a merged PR closes the issue 12 automatically when PR merges.linking work to Issues better because closing by hand may accidentally mark something done when no fix were even made.

## Project structure, environments, secrets

**12. Why should `.gitignore` be one of your first commits? If a file is already tracked, does adding it to `.gitignore` stop Git from tracking it, and if not, what do you do instead?**

Answer: gitignore should be one of the first commits so that junk files like venv/ never gets committed. If a file is already tracked, adding gitignore won't make it stop tracking. To make it stop tracking, we need to use the command git rm --cached file.

**13. Explain the difference between `.env` and `.env.example`, and why they get opposite treatment. If a real API key was committed three weeks ago, why is deleting it in a new commit not a fix, and what should actually be done?**

Answer: .env is for adding secret keys and real values which needs to be hidden and .env.example is for other users who copy your repo so that they know what values to fill in with their own secret key. .env.example is provided instruction with fake keys and values. If a real API key was committed 3 weeks ago, deleting it will not fix anything since your API has already been exposed in older commits and might cost you a lot. If its ever exposed, then you should delete the key and use a new one and never share the key.

**14. What problem do a virtual environment and `requirements.txt` solve together? Why is `venv/` itself never committed, when `requirements.txt` always is?**

Answer: virtual environment solves the problem of clashing versions and provides separate environment per project. requirements.txt solves the problem of having to create separate environment, it gives the list with which any user can rebuild the same environemnt. venv is never committed because it takes up huge memory and is only for the host machine while requirements.txt is only the list of installed packages.

**15. Explain what `git push --force` does to a shared branch and whose work it can destroy. How does `--force-with-lease` behave differently, and why is that safer?**

Answer: git push --force overwrites the shared branch and destroy's work of other team members. --force-with-lease behaves differently and is safer because it checks first if anyone pushed anything after you fetched and refuses the command if they did pushed.