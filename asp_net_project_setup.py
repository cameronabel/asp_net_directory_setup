import os

def main():
    while True:
        print("What is your project name? (Omit the '.Solution')")
        project_name = input()
        if " " not in project_name:
            break
        print("Invalid project name")


    while True:
        try:
            object_number = int(input("How many objects (Models) in your project? "))
            if object_number >= 0:
                break
        except:
            pass
        print("Enter a valid integer")
        
    project_objects = [input("Enter object name: ") for _ in range(object_number)]
    
    parent_directory = r""
    
    path = os.path.join(parent_directory, project_name + ".Solution")
    os.mkdir(path)
    with open(os.path.join(path, ".gitignore"), "w") as g:
        g.write("[Bb]in/\n[Oo]bj/")
        
    with open(os.path.join(path + "\README.md"), "w") as g:
        g.write("")
    
    os.makedirs(os.path.join(path, f"{project_name}", "Controllers"))
    os.makedirs(os.path.join(path, f"{project_name}", "Models"))
    os.makedirs(os.path.join(path, f"{project_name}", "Properties"))
    os.makedirs(os.path.join(path, f"{project_name}", "Views", "Home"))
    
    
    with open(os.path.join(path, f"{project_name}", "Program.cs"), "w") as p:
        p.write(f"""using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

namespace {project_name}
""")
        p.write("""{
  class Program
  {
    static void Main(string[] args)
    {
      WebApplicationBuilder builder = WebApplication.CreateBuilder(args);

      builder.Services.AddControllersWithViews();

      WebApplication app = builder.Build();

      app.UseHttpsRedirection();

      app.UseRouting();

      app.MapControllerRoute(
        name: "default",
        pattern: "{controller=Home}/{action=Index}/{id?}"
      );

      app.Run();
    }
  }
}
""")
    
    with open(os.path.join(path, f"{project_name}", "Program.csproj"), "w") as p_csproj:
        p_csproj.write("""<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>

</Project>
""")
    
    with open(os.path.join(path, f"{project_name}", "Controllers", "HomeController.cs"), "w") as hc:
        hc.write(f"""using Microsoft.AspNetCore.Mvc;

namespace {project_name}.Controllers
""")
        hc.write("""{
  public class HomeController : Controller
  {

    [HttpGet("/")]
    public ActionResult Index()
    {
      return View();
    }

  }
}
""")

    with open(os.path.join(path, f"{project_name}", "Properties", "launchSettings.json"), "w") as prop:
        prop.write("""{
  "profiles": {
    "development": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "https://localhost:5001;http://localhost:5000",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "production": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "https://localhost:5001;http://localhost:5000",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Production"
      }
    }
  }
}
""")

    with open(os.path.join(path, f"{project_name}", "Views", "Home", "Index.cshtml"), "w") as ind:
        ind.write("""<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PAGE TITLE</title>
    <link 
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
      rel="stylesheet" 
      integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
      crossorigin="anonymous">
  </head>
  <body>
  </body>
</html>
""")
    
    os.makedirs(os.path.join(path, f"{project_name}.Tests", "ModelTests"))
    
    with open(os.path.join(path, f"{project_name}.Tests", f"{project_name}.Tests.csproj"), "w") as tcs:
        tcs.write(f"""<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.3.2" />
    <PackageReference Include="MSTest.TestAdapter" Version="2.2.10" />
    <PackageReference Include="MSTest.TestFramework" Version="2.2.10" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\{project_name}\Program.csproj" />  
  </ItemGroup>

</Project>
""")

    for proj_obj in project_objects:
        with open(os.path.join(path, f"{project_name}", "Models", f"{proj_obj}.cs"), "w") as ob:
            ob.write(f"""namespace {project_name}.Models
{'{'}
  public class {proj_obj}
  {'{'}
    public {proj_obj}()
      {'{'}
      
      {'}'}
  {'}'}
{'}'}""")
        
        with open(os.path.join(path, f"{project_name}.Tests", "ModelTests", f"{proj_obj}Tests.cs"), "w") as obt:
            obt.write(f"""using Microsoft.VisualStudio.TestTools.UnitTesting;
using {project_name}.Models;
using System;

namespace {project_name}.Tests
{'{'}
  [TestClass]
  public class {proj_obj}Tests
  {'{'}
  {'}'}
{'}'}
""")





if __name__ == "__main__":
    main()
