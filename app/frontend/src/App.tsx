import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Calendar from "./pages/сalendar/Calendar";
import Home from "./pages/home/Home"


const home = createBrowserRouter([
  {
    path: "/",
    element: <Home/>
  },
  {
    path: "/calendar",
    element: <Calendar/>
  },
  
])

function App() {
  return (
    <RouterProvider router={home}/>
  )
}

export default App
