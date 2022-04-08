const button = document.getElementById("btn")
const color = document.querySelector(".color")


const colors = [
    "#DEB887FF",
    "#7EB973FF",
    "#B95A5AFF",
    "#AB4FC0FF"
];

const hex = [
    "1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"
]

button.addEventListener("click", () => {
    let hexColor = generateHex();
    document.body.style.backgroundColor = hexColor;
    color.textContent = hexColor;
});

function generateHex (){
    let hexColor = "#";
    for (let i = 0; i < 6; i++) {
        hexColor += hex[getRandomNumber()];
    }
    return hexColor
}

function getRandomNumber() {
    return Math.floor(Math.random() * colors.length)
}
