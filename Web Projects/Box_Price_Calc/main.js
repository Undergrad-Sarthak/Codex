const box_lth = document.getElementsByClassName("lth");
const box_wth = document.getElementsByClassName("wth");
const box_hht = document.getElementsByClassName("hht");

const sheet_lth = document.getElementById("slth");
const sheet_wth = document.getElementById("swth");

const calculate_btn = document.getElementsByClassName("calculate_btn")

const calculate = () => {
    sheet_length_value.innerHTML = box_lth.value + box_wth.value + 45;
    sheet_width_value.innerHTML = (box_wth.value * box_hht.value) * 2 + 12;
}

calculate_btn.addEventListener("click",calculate)