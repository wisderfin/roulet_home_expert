import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from './pages/home/Home'
import Calendar from "./pages/сalendar/Calendar";

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
