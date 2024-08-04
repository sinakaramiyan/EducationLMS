// Define a class named 'course'
class course{
    // Constructor method that gets called when an instance of the class is created
    constructor(){
        // Call the 'course' method to initialize the course functionality
        this.course();
    }

    // Method to handle course-related functionality
    course(){
        // Get the element with the id 'lessoncomplete'
        const lessoncomplete = document.querySelector('#lessoncomplete');
        // Add an event listener to the 'lessoncomplete' element to handle click events
        lessoncomplete.addEventListener('click', () => {
            // Get 'svg' elements that are children of the parent node of the 'lessoncomplete' element
            const svg = lessoncomplete.parentNode.parentNode.querySelectorAll('svg');
            // Get the first child element of the first 'svg' element (which is a 'path' element)
            const path = svg[0].firstElementChild; 
            // Set the 'stroke' attribute of the 'path' element to 'green'
            path.setAttribute("stroke", "green");
            // Add CSS classes 'duration-1000' and 'ease-in-out' to the 'path' element
            path.classList.add('duration-1000','ease-in-out');
            // Get the element with the id 'lock'
            const lock = document.querySelector('#lock');
            // Remove all child elements of the 'lock' element
            lock.replaceChildren()
        })
    }
}

// Create a new instance of the 'course' class
new course();