class preloader{
    constructor(){
        this.preloader();
    }
    preloader(){
        const p = document.querySelector('#preloader');
        window.addEventListener('DOMContentLoaded', () => setTimeout(() => {
            p.classList.add('hidden');
        }, 3000));

        //admin menu toggler to hide and show with translate-x
        const menu = document.querySelector('#menu');
        const menutoggle = document.querySelector('#menu-toggle');
        const aside = document.querySelector('#aside');
        menu.addEventListener('click', (e)=>{
            aside.classList.remove('translate-x-full')
        });
        menutoggle.addEventListener('click', (e)=> {
            aside.classList.add('translate-x-full');
        });
    }
}

new preloader();