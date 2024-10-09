import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from './pages/home/Home'

const home = createBrowserRouter([
  {
    path: "/",
    element: <Home/>
  }
])

function App() {
  return (
    <RouterProvider router={home}/>
  )
}

export default App
