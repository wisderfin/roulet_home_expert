import { useEffect, useRef } from 'react';
import Stats from 'stats.js';

const FPSCounter = () => {
    const statsRef = useRef<Stats | null>(null);

    useEffect(() => {
        const stats = new Stats();
        stats.showPanel(0); // 0: FPS, 1: ms, 2: memory
        document.body.appendChild(stats.dom);
        statsRef.current = stats;

        const updateStats = () => {
            stats.begin();
            // Здесь можно добавить ваш код рендеринга
            stats.end();
            requestAnimationFrame(updateStats);
        };

        requestAnimationFrame(updateStats);

        return () => {
            // Удаляем элемент при размонтировании компонента
            document.body.removeChild(stats.dom);
        };
    }, []);

    return null; // Компонент не отображает ничего в интерфейсе
};

export default FPSCounter;
