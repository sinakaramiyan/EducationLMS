class login{
    constructor(){
        this.login();
    }
    login() {
        const login = document.querySelector('#login');

        const studensvg = document.querySelector('#studensvg');
        const teachersvg = document.querySelector('#teachersvg');

        const content = document.querySelector('#content');
        const student = document.querySelector('#student');
        student.addEventListener('click', function () {
            content.textContent = 'ورود به بخش دانش آموزان';
            teacher.classList.remove('bg-zinc-200');
            student.classList.add('bg-zinc-200');
            studensvg.classList.add('-rotate-90');
            teachersvg.classList.remove('-rotate-90');
        })

        const teacher = document.querySelector('#teacher');
        teacher.addEventListener('click', function () {
            content.textContent = 'ورود به بخش اساتید';
            teacher.classList.add('bg-zinc-200');
            student.classList.remove('bg-zinc-200');
            teachersvg.classList.add('-rotate-90');
            studensvg.classList.remove('-rotate-90');
        });
    }
}

new login();