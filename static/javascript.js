function myFunction() {
  let y = document.getElementById("myDIV");
  let x = document.getElementById("numb").value;
  let text;
  let result = x.includes("https://www.youtube.com/watch?");
  let result1 = x.includes("https://youtu.be");

  if ((result || result1) != true) {
    text = "Input not valid";

  } else {
  function make_request(){
        let request = new XMLHttpRequest();
        request.open("GET", "/track");
        request.send();
        request.onload = () => {
        var percentage_complete = parseInt(request.response);
        console.log(percentage_complete);
        }

    }

    text = "";


    y.style.display = "block";
    /* change progress after 1 second (only for showcase) */
    setTimeout(() => changeProgress(16), 1500);
    setTimeout(() => changeProgress(23), 2600);
    setTimeout(() => changeProgress(28), 4600);
    setTimeout(() => changeProgress(28), 4600);
    setTimeout(() => changeProgress(33), 5266);
    setTimeout(() => changeProgress(39), 7200);
    setTimeout(() => changeProgress(55), 9000);
    setTimeout(() => make_request(), 9000);
    setTimeout(() => changeProgress(69), 10500);
    setTimeout(() => changeProgress(81), 12500);
    setTimeout(() => make_request(), 12500);
    setTimeout(() => changeProgress(100), 13200);
    document.getElementById('theForm').submit();


  }
  document.getElementById("validation").innerHTML = text;
}


const progressbar = document.querySelector(".progress");

const changeProgress = (progress) => {
  progressbar.style.width = `${progress}%`;
  if (progress === 0) {
  document.getElementById("bar-description").innerHTML = 'We are processing your video';
  }
  if (progress === 39) {
  document.getElementById("bar-description").innerHTML = 'Finding most important facts';
  }
  if (progress === 69) {
  document.getElementById("bar-description").innerHTML = 'Final touch';
  }
};


function copyText() {

            /* Select text area by id*/
            var Text = document.getElementById("textbox").textContent;

            /* Select the text inside text area. */
            console.log(Text);
            /* Copy selected text into clipboard */
            navigator.clipboard.writeText(Text);

        }

function copyText2() {

            /* Select text area by id*/
            var Text = document.getElementById("textbox2").textContent;

            /* Select the text inside text area. */
            console.log(Text);
            /* Copy selected text into clipboard */
            navigator.clipboard.writeText(Text);

        }