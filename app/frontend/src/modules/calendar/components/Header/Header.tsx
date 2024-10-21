import style from './header.module.css'

const Header = () => {
  return (
    <div className={style.header}>
        <div className={style.container}>
            <div className={style.block1}></div>
            <div className={style.title}>Лучшие дни для урожая</div>
        </div>
        <div className={style.container}>
            <div className={style.block2}></div>
            <div className={style.title}>Худшие дни для урожая</div>
        </div>
    </div>
  )
}

export default Header