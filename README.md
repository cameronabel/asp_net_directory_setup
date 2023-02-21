# asp_net_directory_setup

- Clone the py file to your machine
- Open the py file in your text editor of choice
- Modify line 23 to point to your main project directory (where you hold all of your Epicodus projects)
  Alternatively, leave this string blank and the templater will build your project inside its directory at runtime.
- Save the py file
- Invoke by double-clicking or by navigating to the py file's directory in your terminal, then executing `python asp_net_project_setup.py`\
Answer the program when prompted:\
`What is your project name? (Omit the '.Solution')`\
This is the project's name. For instance, the TriangleTracker project might be named `TriangleTracker.Solution`. Your response here would be `TriangleTracker`\
\
`How many objects (Models) in your project? `\
This is the number of objects you would like to come pre-built in your project. For the TriangleTracker project, this might be `1`\
\
`Enter object name: `\
For each object, you will be prompted for a name. Using the TriangleTracker example again, this might be `Triangle`.\
Each object will have a Model and a ModelTest file built out with some boilerplate empty constructors and tests.\
\
Remember - commit your .gitignore (included) first!\
\
This is a rough, slapdash templater thrown together in the short few moments before class time - please reach out if you find any bugs or have features to request.

If you dont plan to include tests (tsk) you may safely delete the `.Tests` directory. Otherwise, you will need to execute `dotnet restore` from that directory in order to link the `.Tests.csproj` file to the program. You can then execute `dotnet test`. The project should build successfully and the empty tests should run.
