import { Loading } from "../../components/Loading/Loading";
import Modal from "../../components/UI/Modal/Modal";
import { Roulette } from "../../modules/Roulette"

const Home = () => {

  return (
    <>
    <Modal>
      <h1 style={{fontSize: "24px", marginTop: "10px", fontWeight: "700"}}>Крути рулетку и получай много призов!</h1>
      <br/>
      <div style={{ color: "#bbbbbb" }}>Рулетку можно крутить только раз в 24 часа</div>
    </Modal>
       <Loading/>
      <Roulette />
      
    </>
  )
}

export default Home;