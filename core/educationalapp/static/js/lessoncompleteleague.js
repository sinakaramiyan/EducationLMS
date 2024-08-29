
class lessoncompleteleague{
    constructor(){
        this.completeleague();
    }

    completeleague() {
        // remove animate for medal
        const medal = document.querySelector('#medal');
        setTimeout(() => {
            medal.classList.remove('animate-bounce');
        }, 3500);

        // league transition elements
        const score = document.querySelectorAll('#score');
        const sort = document.querySelector('#sort');    

        // changable element
        let change = 7
        // change score number
        score[change].innerHTML = parseInt(900);

        // get related changable children in sort div
        const sort2 = sort.children[change];
       
        // add background before transition
        sort2.style.background = 'rgba(255, 255, 255, 1)'; // glassy background color
        sort2.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.2)'; // subtle shadow
        sort2.style.backdropFilter = 'blur(2px)'; // glassy blur effect
        sort2.style.borderRadius = '10px'; // rounded corners
        sort2.style.marginLeft = '10px'; // marginleft
        sort2.style.marginRight = '10px'; //marginright
        sort2.style.transition = 'transform 4s'; // add trnasition effect to element.
        
        // first scroll to target changable element
        sort2.scrollIntoView();
        
        for (let i = change; i > 0 ; i--) {
            
            if (parseInt(score[change].innerHTML) >= parseInt(score[i-1].innerHTML)){
                // chabge place of two pervious element
                const sort1 = sort.children[i-1];   
                const sortp = sort.children[i];           
                
                // change rank number of user
                const rankmain = parseInt(sort2.firstElementChild.querySelector('#rank').innerHTML);
                sort2.firstElementChild.querySelector('#rank').innerHTML = rankmain - 1;
                
                // change rank number of other users
                const rank = parseInt(sort1.firstElementChild.querySelector('#rank').innerHTML);
                sort1.firstElementChild.querySelector('#rank').innerHTML = rank + 1;
                
                // Add a transition effect to the elements
                sort1.style.transition = 'transform 4s';

                // Swap the positions of the elements
                sort1.style.transform = 'translateY(' + (sortp.offsetTop - sort1.offsetTop) + 'px)';
                sort2.style.transform = 'translateY(' + (sort1.offsetTop - sort2.offsetTop) + 'px)';

                // at each loop scroll to pervious element for better animation
                setTimeout(() => {
                    sortp.scrollIntoView({ behavior: "smooth", block: "end" });
                }, 1000);
            }
        }

        // remove background after transition
        sort2.addEventListener('transitionend', () => {
            sort2.style.background = '';
            sort2.style.boxShadow = '';
            sort2.style.filter = '';
            sort2.style.backdropFilter = '';
            sort2.style.borderRadius = '';
            sort2.style.marginLeft = '';
            sort2.style.marginRight = '';
        });
    }
}

new lessoncompleteleague();