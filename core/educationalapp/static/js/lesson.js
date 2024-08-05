class lesson {
    constructor(){
        this.lesson();
    }

    lesson(){

        // scroll to top with smooth behavior
        window.addEventListener("load", (event) => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });

        // dynamic lesson
        // tab's number
        const main = document.querySelector('#main');
        const div = main.children;
        const innerdivlength = div.length;
        
        //insert progressbar relative
        const progressbar = document.querySelector('#progressbar');
        for (let i = 0; i < innerdivlength; i++) {
            // prgressbar background
            const progress = document.createElement('a');
            progress.classList.add('flex', 'w-full', 'h-3', 'bg-gray-200', 'overflow-hidden', 'dark:bg-neutral-700','cursor-pointer');
            
            // progressbar development
            const development = document.createElement('div');
            development.classList.add('flex' , 'flex-col', 'justify-center', 'items-center', 'overflow-hidden', 'bg-green-600', 'text-xs', 'text-white', 'text-center', 'whitespace-nowrap', 'transition', 'duration-500');
            
            // add progressbar development to prgressbar background
            progress.appendChild(development)
            
            progressbar.appendChild(progress);
            
            //for show related div
            progress.addEventListener('click', (e) => {
                console.log(progress);
                div[i].classList.add('hidden');
                for (let j = 0; j < innerdivlength; j++) {
                    if(i != j){
                        div[j].classList.add('hidden');
                    }else{
                        div[j].classList.remove('hidden');
                    }
                }
                // perviouse and next button control to show and hide
                if (i == (innerdivlength - 1)) {
                    next.classList.add('fill-gray-200');
                    next.classList.remove('cursor-pointer');
                    pervious.classList.remove('fill-gray-200');
                } else if (i == 0) {
                    next.classList.remove('fill-gray-200');
                    pervious.classList.add('fill-gray-200');
                    pervious.classList.remove('cursor-pointer');
                } else {
                    next.classList.remove('fill-gray-200');
                    pervious.classList.remove('fill-gray-200');
                    next.classList.add('cursor-pointer');
                    pervious.classList.add('cursor-pointer');
                }
            })           
        }

        //next tab button
        const next = document.querySelector('#next');
        next.addEventListener('click', () => {
            for (let i = 0; i < innerdivlength-1; i++) {
                if(!div[i].classList.contains('hidden')){
                    div[i].classList.add('hidden');
                    i += 1;
                    div[i].classList.remove('hidden');

                    // perviouse and next button control to show and hide
                    if(i == (innerdivlength - 1)){
                        next.classList.add('fill-gray-200');
                        next.classList.remove('cursor-pointer');
                        pervious.classList.remove('fill-gray-200');
                    } else {
                        next.classList.remove('fill-gray-200');
                        pervious.classList.remove('fill-gray-200');
                        next.classList.add('cursor-pointer');
                        pervious.classList.add('cursor-pointer');
                    }
                }
            }
        })

        //pervious tab button
        const pervious = document.querySelector('#pervious');
        pervious.addEventListener('click', () => {
            for (let i = 0; i < innerdivlength; i++) {
                if (!div[i].classList.contains('hidden') && i > 0) {
                    div[i].classList.add('hidden');
                    i -= 1;
                    div[i].classList.remove('hidden');
                    // perviouse and next button control to show and hide
                    if (i == 0) {
                        next.classList.remove('fill-gray-200');
                        pervious.classList.remove('cursor-pointer');
                        pervious.classList.add('fill-gray-200');
                    } else {
                        next.classList.remove('fill-gray-200');
                        pervious.classList.remove('fill-gray-200');
                        next.classList.add('cursor-pointer');
                        pervious.classList.add('cursor-pointer');
                    }
                }
            }
        })
        
        //change between content
        const link = document.querySelectorAll('#tabh');

        // link betwwen tabs and fill progress bar
        for (let i = 0; i < link.length; i++) {
            link[i].addEventListener('click', () => {
                for (let j = 0; j < innerdivlength; j++) {
                    div[i].classList.add('hidden');
                }
                progressbar.children[i].firstElementChild.classList.add('w-full');
                div[i+1].classList.remove('hidden');
            })      
        }

        // function for every tab complete
        const button = document.querySelector('#tabc');
        const t2 = document.querySelector('#t2');
        const progress = progressbar.children[0];
        const complete = document.querySelector('#complete');
        
        let currentProgress = 0;

        // correct answer direction
        button.addEventListener('click', (e) => {
            e.preventDefault();
            if (currentProgress < 100) {
                currentProgress += 20;          
                t2.classList.remove('hidden');
                window.location.href = 'http://127.0.0.1:8000/courses/coursename/lesson' + '#t2';
                t2.previousElementSibling.classList.remove('h-[80dvh]');
                if (currentProgress === 100) {
                    complete.classList.remove('hidden');
                }
                progress.firstElementChild.style = `width:  ${currentProgress}%`;
            }

            button.disabled = true;
            button2.disabled =true;
            button.classList.remove('border', 'border-zinc-300', 'cursor-pointer');
            button2.classList.remove('border', 'border-zinc-300', 'cursor-pointer', 'bg-zinc-200');
            button2.classList.add('bg-zinc-100');
        });
        
        const button2 = document.querySelector('#tabc1');
        const t3 = document.querySelector('#t3');

        // wrong answer direction
        button2.addEventListener('click', (e) => {
            e.preventDefault();
            if (currentProgress < 100) {
                currentProgress += 20;
                t3.classList.remove('hidden');
                window.location.href = 'http://127.0.0.1:8000/courses/coursename/lesson' + '#t3';
                t3.previousElementSibling.classList.remove('h-[80dvh]');
                if (currentProgress === 100) {
                    complete.classList.remove('hidden');
                }
                progress.firstElementChild.style = `width:  ${currentProgress}%`;
            }

            button.disabled = true;
            button2.disabled = true;
            button.classList.remove('border', 'border-zinc-300', 'cursor-pointer');
            button2.classList.remove('border', 'border-zinc-300', 'cursor-pointer', 'bg-zinc-200');
            button2.classList.add('bg-zinc-100');
        });

        const tabc2 = document.querySelector('#tabc2');

        tabc2.addEventListener('click', () => {
            if (currentProgress < 100) {
                currentProgress += 20;
                if (currentProgress === 100) {
                    complete.classList.remove('hidden');
                }
                progress.firstElementChild.style = `width:  ${currentProgress}%`;
            }
        })

        // quiz segment
        // find user naswers
        let checkedAnswers = [];
        const answers = document.querySelectorAll('#answer');
        const checkanswer = document.querySelector('#checkanswer');
        answers.forEach((checkbox, index) => {
            checkbox.addEventListener('click', () => {
                if (checkbox.checked) {
                    checkanswer.classList.remove('hidden');
                    // Add the checked answer to the array
                    checkedAnswers.push(index);
                } else {
                    // Remove the unchecked answer from the array
                    checkedAnswers = checkedAnswers.filter((answer) => answer !== index);
                    checkanswer.classList.add('hidden');
                }
            })
        });

        // check user answer 
        let correct = [ 0, 1];
        const correctmessage = document.querySelector('#correctmessage');
        const wrongmessage = document.querySelector('#wrongmessage');

        const tryingagain = document.querySelector('#tryingagain');
        const nextsection = document.querySelector('#nextsection');

        const t4 = document.querySelector('#t4');
        checkanswer.addEventListener('click', () => {
            // Comparing each element of array
            for (let i = 0; i < correct.length; i++){
                for (let j = 0; j < correct.length; j++) {
                    if (correct[i] != checkedAnswers[j]){
                        wrongmessage.classList.remove('hidden');
                        correctmessage.classList.add('hidden');

                        // if wrong show تلاش دوباره
                        tryingagain.classList.remove('hidden');
                        nextsection.classList.add('hidden');
                        checkanswer.classList.add('hidden');

                        tryingagain.addEventListener('click', () => {
                            answers.forEach( (checkbox, index) => {
                                checkbox.checked = false;
                                checkbox.disabled = false;
                                tryingagain.classList.add('hidden');
                                checkanswer.classList.remove('hidden');
                                wrongmessage.classList.add('hidden');
                            })
                        })
                    }
                    if (correct[i] == checkedAnswers[j]) {
                        correctmessage.classList.remove('hidden');
                        wrongmessage.classList.add('hidden');

                        // if correct got to next section
                        nextsection.classList.remove('hidden');
                        tryingagain.classList.add('hidden');
                        checkanswer.classList.add('hidden');

                        nextsection.addEventListener('click', () => {
                            t4.classList.remove('hidden');
                            window.location.href = 'http://127.0.0.1:8000/courses/coursename/lesson' + '#t4';
                            t2.previousElementSibling.classList.remove('h-[80dvh]');
                        })
                    }
                }
                answers.forEach((checkbox) => {
                    checkbox.disabled = true;
                });
            }
            checkedAnswers = []
        })

        // show guidance
        const guide = document.querySelector('#guide');
        const t21 = document.querySelector('#t21');
        guide.addEventListener('click', () => {
            t2.classList.add('hidden');
            t21.classList.remove('hidden');
        })

        // close guide page
        const rt21 = document.querySelector('#rt21');
        rt21.addEventListener('click', () => {
            t2.classList.remove('hidden');
            t21.classList.add('hidden')
        })

        // next section after two column page
        const nextsectiontwocolumn = document.querySelector('#nextsectiontwocolumn');
        nextsectiontwocolumn.addEventListener('click', () => {
            t5.classList.remove('hidden');
            window.location.href = 'http://127.0.0.1:8000/courses/coursename/lesson' + '#t5';
            t4.previousElementSibling.classList.remove('h-[80dvh]', 'mt-12');
        })


        // unchecked checkbox button after refresh
        answers.forEach((checkbox) => {
            checkbox.checked = false;
        });
    }
}

new lesson();