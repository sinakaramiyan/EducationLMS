class app{
    constructor(){
        this.home();
    }
    home(){
        const python_cotent = document.querySelector('#python_cotent');
        const assembly_cotent = document.querySelector('#assembly_cotent');
        const cprgrmaing_cotent = document.querySelector('#cprgrmaing_cotent');
        const csharp_cotent = document.querySelector('#csharp_cotent');

        const python_svg = document.querySelector("#python_svg");
        const assembly_svg = document.querySelector("#assembly_svg");
        const cprograming_svg = document.querySelector("#cprograming_svg");
        const csharp_svg = document.querySelector("#csharp_svg");

        const python = document.querySelector('#python');
        const cprgrmaing = document.querySelector('#cprgrmaing');
        const assembly = document.querySelector('#assembly');
        const csharp = document.querySelector('#csharp');

        python.addEventListener("click", function () {
            if (python_cotent.classList.contains('hidden')) {
                python_svg.classList.add('-rotate-90');
                assembly_svg.classList.remove('-rotate-90');
                cprograming_svg.classList.remove('-rotate-90');
                csharp_svg.classList.remove('-rotate-90');

                python.classList.add('bg-zinc-200');
                assembly.classList.remove('bg-zinc-200');
                cprgrmaing.classList.remove('bg-zinc-200');
                csharp.classList.remove('bg-zinc-200');

                python_cotent.classList.remove('hidden');
                assembly_cotent.classList.add('hidden');
                cprgrmaing_cotent.classList.add('hidden');
                csharp_cotent.classList.add('hidden');
            }
        });

        assembly.addEventListener("click", function () {
            if (assembly_cotent.classList.contains('hidden')) {
                python_svg.classList.remove('-rotate-90');
                assembly_svg.classList.add('-rotate-90');
                cprograming_svg.classList.remove('-rotate-90');
                csharp_svg.classList.remove('-rotate-90');

                python.classList.remove('bg-zinc-200');
                assembly.classList.add('bg-zinc-200');
                cprgrmaing.classList.remove('bg-zinc-200');
                csharp.classList.remove('bg-zinc-200');

                python_cotent.classList.add('hidden');
                assembly_cotent.classList.remove('hidden');
                cprgrmaing_cotent.classList.add('hidden');
                csharp_cotent.classList.add('hidden');
            }
        });

        cprgrmaing.addEventListener("click", function () {
            if (cprgrmaing_cotent.classList.contains('hidden')) {
                python_svg.classList.remove('-rotate-90');
                assembly_svg.classList.remove('-rotate-90');
                cprograming_svg.classList.add('-rotate-90');
                csharp_svg.classList.remove('-rotate-90');

                python.classList.remove('bg-zinc-200');
                assembly.classList.remove('bg-zinc-200');
                cprgrmaing.classList.add('bg-zinc-200');
                csharp.classList.remove('bg-zinc-200');

                python_cotent.classList.add('hidden');
                assembly_cotent.classList.add('hidden');
                cprgrmaing_cotent.classList.remove('hidden');
                csharp_cotent.classList.add('hidden');
            }
        });
        csharp.addEventListener("click", function () {
            if (csharp_cotent.classList.contains('hidden')) {
                python_svg.classList.remove('-rotate-90');
                assembly_svg.classList.remove('-rotate-90');
                cprograming_svg.classList.remove('-rotate-90');
                csharp_svg.classList.add('-rotate-90');

                python.classList.remove('bg-zinc-200');
                assembly.classList.remove('bg-zinc-200');
                cprgrmaing.classList.remove('bg-zinc-200');
                csharp.classList.add('bg-zinc-200');

                python_cotent.classList.add('hidden');
                assembly_cotent.classList.add('hidden');
                cprgrmaing_cotent.classList.add('hidden');
                csharp_cotent.classList.remove('hidden');
            }
        });

        //dark mode toggle

        var themeToggleBtn = document.getElementById('theme-toggle');

        themeToggleBtn.addEventListener('click', function () {
            // if set via local storage previously
            if (localStorage.getItem('color-theme')) {
                if (localStorage.getItem('color-theme') === 'light') {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                } else {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                }
            } else {
                if (document.documentElement.classList.contains('dark')) {
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('color-theme', 'light');
                } else {
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('color-theme', 'dark');
                }
            }
        });
    }
}

new app();