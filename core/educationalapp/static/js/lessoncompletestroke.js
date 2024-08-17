class lessoncompletestroke{
    constructor(){
        this.func();
    }

    func(){
        const strike = document.querySelector('#strike');
        const next = document.querySelector('#next');
        next.addEventListener('click', handliClick);

        function handliClick(e){
            e.preventDefault();
        }
        setTimeout(() => {
            strike.classList.remove('animate-bounce');
            next.removeEventListener('click', handliClick);
            next.setAttribute('href', '/courses/coursename/lesson/lessoncompleteleague');
        }, 4500);
    }
}

new lessoncompletestroke();