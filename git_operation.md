1. Fork from Origin repo

2. Git clone your forked repo

git clone https://github.com/your-username/forked-repo.git

3. Add your fork as remote repo

git remote add upstream https://github.com/your-username/forked-repo.git

4. If the original has update, you can pull the update to your fork

git fetch upstream
git merge upstream/main

5. Check all the remote repo

git remote -v

6. Push to my fork

git push origin main

7. Push to original repo 

git push upstream main
