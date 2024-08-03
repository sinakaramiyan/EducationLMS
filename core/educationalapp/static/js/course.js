class course{
    constructor(){
        this.course();
    }

    course(){
        const lessoncomplete = document.querySelector('#lessoncomplete');
        lessoncomplete.addEventListener('click', () => {
            const svg = lessoncomplete.parentNode.parentNode.querySelectorAll('svg');
            const path = svg[0].firstElementChild; 
            path.setAttribute("stroke", "green")
            path.classList.add('duration-1000','ease-in-out')

            const lock = document.querySelector('#lock');
            lock.replaceChildren()
        })
    }
}

new course();