import React, { useState } from 'react'
import style from "./modal.module.css"
import { IModal } from './ModalTypes'
import ReactDOM from 'react-dom'

const portalElement = document.getElementById("portal")

const Modal: React.FC<IModal> = ({ children, funcOnClose }) => {
  const [isCloseModal, setIsCloseModal] = useState<boolean>(true)

  const close = () => {
    if (typeof funcOnClose !== 'undefined') {
      funcOnClose()
    }
    setIsCloseModal(false)
  }

  return (
    portalElement && ReactDOM.createPortal(
      <div className={`${style.wrapperModal} ${isCloseModal ? style.wrapperModalActive : ""}`}>
        <div className={style.modal}>
          <div className={style.close} onClick={() => close()}>×</div>
          {children}
        </div>
      </div>, portalElement)

  )
}

export default Modal