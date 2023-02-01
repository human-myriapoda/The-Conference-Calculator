# Instructions to use this repository (for collaborators)
## 1. Create a Github account
1. Go on https://github.com/.
2. Create an account with your preferred email address.
3. You must provide your Github username so that I can add you to the repository. For example, my username is `@human-myriapoda`.
4. Once I add you to the repository called `The-Conference-Calculator`, you should receive an email from Github.
5. Accept the invitation. The repository should appear on your Github.

---
## 2. Install Github desktop on your computer
1. Download it here: https://desktop.github.com/.
2. Once it's downloaded, open it.
3. On the top menu, click on `File`.
4. Click on `Options`.
5. In `Accounts`, connect to your Github account.
6. Close that window.
7. Now, the repository should appear on Github desktop. 
8. From there, there are two possibilities: Click on `Current repository` and select `The-Conference-Calculator` **OR** Clone `The-Conference-Calculator`.
9. The repository should appear locally on your computer. For example, mine is located in `C:\Users\myriampe\OneDrive\Documents\GitHub\The-Conference-Calculator`.
10. *Note for people new to Github* $\rightarrow$ now, any change you make in the repository can be 'committed' to Github; it means that everyone in the team will be able to see it! More on that later.
11. Don't close the application for now!

---
## 3. Install Python via Anaconda
1. *Note* $\rightarrow$ there are other ways to install Python, but the Anaconda distribution is really easy to use, especially for beginners. As long as you have Python installed!
2. Download it here: https://www.anaconda.com/.
3. Once it's downloaded, you can open the `Anaconda Navigator` if you want. On there you can find all the applications installed with Anaconda (e.g., Spyder and JupyterLab). You can also manage your environments (more on that in the next section).

### 3.1 Create an environment for the project (optional but highly recommended)
1. *Note* $\rightarrow$ what is an environment and why would we use one? *An environment is a virtual workspace with a set of specified modules and versions relevant to the current project. In other words, you can import any module or use a specific version of Python (e.g., 3.7) without clashing with other projects. It is recommended to have a different environment for each project you have!*
2. From your search bar (on your computer), search for `Anaconda Prompt (anaconda 3)` and open it. It is a terminal.
3. To create a new environment, write the following line in the terminal:
```
conda create -n ConferenceCalculator
```
4. Once it's created, activate the environment by typing:
```
conda activate ConferenceCalculator
```
5. From there, there are two options.
6. *Option 1*: access the repositery by typing `cd OneDrive\Documents\GitHub\The-Conference-Calculator`, write `conda install pip` and then `conda install -r requirements.txt`. This is meant to install the same modules as me. But it might not work (see option 2 instead).
7. *Option 2*: install the modules manually via `conda install MODULE_NAME --yes` or `pip install MODULE_NAME`. For now you can install `numpy` and `matplotlib`, but can import any module you want.
8. *Note* $\rightarrow$ for VS Code Studio (more on that later), you might have to install an extension to run Jupyter Notebooks (.ipynb files). You can write `conda install ipykernel --yes` or `pip install ipykernel`.
9. Don't close `Anaconda Prompt` just now, you might need it later.

---
## 4. Install VS Code Studio (IDE)
1. *Note* $\rightarrow$ what is an IDE? *An IDE (integrated development environment) is an application that falicitates coding. You can visualise, for example, the value of your variables and easily change the environment. It is great for beginners as well.*
2. *Note* $\rightarrow$ why choose VS Code Studio? *There are other IDEs for Python (e.g., PyCharm and Spyder), but I personnally think VS Code Studio is the easiest to set-up and use. It's up to you to decide which one you want to use, but the rest of this tutorial is based on VS Code Studio.*
3. Download it here: https://code.visualstudio.com/.
4. Once it's downloaded, open it. You can skip the initial set-up (or accept the default settings).
5. In `File`, click `Open Folder` and open the `The-Conference-Calculator` folder.

### 4.1 Link VS Code Studio to Github Desktop
1. On the left-hand-side menu, click on `Extensions` (four square icon).
2. Install the following extensions: `Python`, `Github Pull Requests and Issues`, `Jupyter` (might need to install other ones, but for now these ones should work).
3. On the left-hand-side menu, click on `GitHub` (Github logo) and connect to your Github account (there will be a webpage pop-up asking you for authorisation).

### 4.2 Install Git (optional, you might not need to do it)
1. Download it here: https://git-scm.com/downloads.
2. Sometimes it is required in VS Code Studio, so download it just if something is not working.

---
## 5. Test that everything is working

