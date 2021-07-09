var nav = document.querySelector("nav");
var toggles = document.querySelector(" .fa-bars");
var ul = document.querySelector("ul");
var times = document.querySelector(".fa-times");

window.addEventListener("load", () => {
    toggles.addEventListener("click", () => {
        nav.classList.toggle("nav-active");
        toggles.classList.toggle("j-active");
        ul.classList.toggle("ul-active");
        console.log("clicked");
        times.style.display = "flex";
    });
    times.addEventListener("click", () => {
        nav.classList.remove("nav-active");
        toggles.classList.remove("j-active");
        ul.classList.toggle("ul-active");
    });
});