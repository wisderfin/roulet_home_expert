import { useState } from 'react'

function useModal(): [boolean, (params: boolean) => void, string | null, (params: string) => void] {
    
    const [isVisible, setIsVisible] = useState<boolean>(false)
    const [text, setText] = useState<string | null>(null)
    function visible(params: boolean) {
        setIsVisible(params)        
    }
    function setTextModal(params: string) {
        setText(params)        
    }
    return [isVisible, visible, text, setTextModal]
}
export default useModal