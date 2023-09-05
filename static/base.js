const form = document.getElementById("guess-form");
const input = document.getElementById("guess");
let score = 0;
const scoreDisplay = document.getElementById('score');
const displayRes = document.getElementById('result');
const timer = document.getElementById('timer');
let seconds = 0;
const highScore = document.getElementById('high')

form.addEventListener("submit", submitHandler);

function updateScore(word, result){
    if (result.data.result === 'ok'){
        score += word.length;
        scoreDisplay.innerText = `Score: ${score}`;
    }
}

async function submitHandler(evt){
    evt.preventDefault();
    let guess = input.value;
    console.log(guess);
    input.value = '';
    let result = await axios.post('http://127.0.0.1:5000/guess', {'g': guess});
    displayRes.innerText = result.data.result;
    updateScore(guess, result);
}

let timerHandler = setInterval(async function() {
    if(seconds === 60){
        form.remove();
        let json = {'score': score};
        let result = await axios.post("http://127.0.0.1:5000/scores", json, {
            headers: {
              'Content-Type': 'application/json',
            },
          });
          highScore.innerText = `High Score: ${result.data.highscore}`;
        clearInterval(timerHandler);
    }
    timer.innerText = `Timer: ${seconds++}`;
}, 1000);

async function start(){
    let res = await axios.get('http://127.0.0.1:5000/highscore');
    highScore.innerText = `High Score: ${res.data.highscore}`
}
start();



