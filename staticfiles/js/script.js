console.log("It is working");

let themeDots = document.getElementsByClassName("theme-dot");

for (var i = 0; themeDots.length > i; i++) {
    themeDots[i].addEventListener("click", function () {
        let mode = this.dataset.mode;
        console.log("Option clicked: ", mode);
        setTheme(mode);
    });
}

function setTheme(mode) {
    if (mode == "light") {
        document.getElementById("theme-style").href =
            "{{ STATIC_URL }} static/css/default.css";
    }

    if (mode == "blue") {
        document.getElementById("theme-style").href =
            "{{ STATIC_URL }} static/css/blue.css";
    }

    if (mode == "green") {
        document.getElementById("theme-style").href =
            "{{ STATIC_URL }}/css/green.css";
    }

    if (mode == "purple") {
        document.getElementById("theme-style").href =
            "{{ STATIC_URL }} static/css/purple.css";
    }
}
