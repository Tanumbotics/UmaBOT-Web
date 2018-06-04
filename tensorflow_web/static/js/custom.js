function showLoader() {
    if (document.getElementById("id_file").files.length == 0) {
        document.getElementById('preloader').style.display = "none";
    } else {
        document.getElementById('preloader').style.display = "block";
    }
}

document.getElementById('id_file').accept = 'image/*';
