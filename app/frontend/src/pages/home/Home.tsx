import Modal from "../../components/UI/Modal/Modal"
import { Roulette } from "../../modules/Roulette"
import { Header } from "../../modules/Header"

const Home = () => {

  return (
    <>
      <Modal>
        Приложение запущено в режиме Demo
      </Modal>,

      <Header />
      <Roulette />
    </>
  )
}

export default Home;