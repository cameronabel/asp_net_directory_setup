using Microsoft.AspNetCore.Mvc;

namespace TriangleTracker.Controllers

{
  public class HomeController : Controller
  {

    [HttpGet("/")]
    public ActionResult Index()
    {
      return View();
    }

  }
}
