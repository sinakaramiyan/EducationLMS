/**
 * Base class for handling various DOM interactions and events.
 */
class base{
    /**
    * Constructor for the Base class.
    */
    constructor(){
        this.base();
    }
    /**
    * Initializes the base functionality.
    */
    base(){
        // Search bar functionality
        const searchfull = document.querySelector('#searchfull');
        const searchbutton = document.querySelector('#searchbutton');
        const closesearch = document.querySelector('#closesearch');

        /**
        * Event listener for the search button click.
        * Removes the 'translate-y-full' class from the search full element and adds 'overflow-hidden' to the document element.
        */
        searchbutton.addEventListener('click', () => {
            searchfull.classList.remove('translate-y-full');
            document.documentElement.classList.add('overflow-hidden');
            
        })

        /**
        * Event listener for the close search button click.
        * Adds the 'translate-y-full' class to the search full element and removes 'overflow-hidden' from the document element.
        */
        closesearch.addEventListener('click', () => {
            searchfull.classList.add('translate-y-full');
            document.documentElement.classList.remove('overflow-hidden');
        })

        // Details elements functionality
        var details = [...document.querySelectorAll('details')];

        /**
        * Event listener for the document click.
        * Closes all details elements if the click is outside of any details element.
        */
        document.addEventListener('click', function (e) {
            if (!details.some(f => f.contains(e.target))) {
                details.forEach(f => f.removeAttribute('open'));
            } else {
                details.forEach(f => !f.contains(e.target) ? f.removeAttribute('open') : '');
            }
        })
        /**
        * Event listener for the window load.
        * Scrolls the window to the top smoothly.
        */
        window.addEventListener("load", (event) => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });

    }
}

new base();