function showLoading(){

    document.getElementById(
        "loading"
    ).style.display = "block";

}



let themeButton = document.getElementById(
    "theme-toggle"
);


themeButton.onclick = function(){

    document.body.classList.toggle(
        "light"
    );

};
