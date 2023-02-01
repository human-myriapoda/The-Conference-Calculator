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
1. On the left-hand-side menu (VS Code Studio), click on `Explorer` (file icon, first icon).
2. Create a new file, e.g. `u_r_amazing.py`. Write whatever you want in it.
3. Now, the file should appear GREEN with a 'U' symbol $\rightarrow$ this means you **created** an new file. Similarly, if your file is ORANGE with a 'M' symbol, it means you've **modified** the file and if your file is RED, it means you've `deleted` the file (or removed something from the file).
4. On the left-hand-side menu, click on `Source Control` (branch icon; there should be a number on it - the number of changes you did). 
5. You can select `Push & Sync` and click `Always` on the pop-up window. This means that your changes will go on Github desktop.
6. Open Github desktop; you should see the changes you just made.
7. On the bottom-left, there a box with `Summary (required)` and `Description`. Write a short description of the changes you made in 'Summary' and click on `Commit to main`.
8. Now, in the middle panel, a new BLUE box should appear; with the option to `Push origin`. Click on it; this will 'publish' your changes to the Github repository so that everyone can see them! If you want to make sure it worked, refresh the Github webpage. 
9. *Note* $\rightarrow$ if someone made a change and it's not on your local computer yet, the BLUE box will appear with `Pull origin`. Click on it as often as possible to have the latest version.
10. *Note* $\rightarrow$ on the top menu of Github desktop, you can refresh the app to find new changes. 

>You should be setted up now and ready to start working on the code! Hopefully there were not too many problems :D 

---
## 6. Additional notes
- Avoid working on the same code at the same time with someone else. It might create multiple versions of the same document. 
- If you substantially change a file, make sure to leave a long comment when you commit.
- If you use someone else's code (from the internet), make sure to note the reference.
- If you want to create a folder in the repository, you must add a file inside of it.
- Use a `.py` (Python) file to write source code (coding itself) and use a `.ipynb` (Jupyter Notebook) to execute your functions (e.g. produce plots). If you're new to coding, start with a `.ipynb` file.
- Leave comments in your code! It helps understand it :)
