class base{
    constructor(){
        this.base();
    }
    base(){
        //menu mobile responsive
        // const menumobile = document.querySelector('#menumobile');
        // const menutoggle = document.querySelector('#menu-toggle');
        // const closemenumobile = document.querySelector('#closemenumobile');
        // menutoggle.addEventListener('click', () => {
        //     menumobile.classList.remove('translate-x-full')
        // })
        // closemenumobile.addEventListener('click', () => {
        //     menumobile.classList.add('translate-x-full')
        // })

        //search bar
        const searchfull = document.querySelector('#searchfull');
        const searchbutton = document.querySelector('#searchbutton');
        const closesearch = document.querySelector('#closesearch');
        searchbutton.addEventListener('click', () => {
            searchfull.classList.remove('translate-y-full');
            document.documentElement.classList.add('overflow-hidden');
            
        })
        closesearch.addEventListener('click', () => {
            searchfull.classList.add('translate-y-full');
            document.documentElement.classList.remove('overflow-hidden');
        })

        var details = [...document.querySelectorAll('details')];
        document.addEventListener('click', function (e) {
            if (!details.some(f => f.contains(e.target))) {
                details.forEach(f => f.removeAttribute('open'));
            } else {
                details.forEach(f => !f.contains(e.target) ? f.removeAttribute('open') : '');
            }
        })

        window.addEventListener("load", (event) => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });

    }
}

new base();