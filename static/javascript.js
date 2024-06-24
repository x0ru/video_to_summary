function myFunction() {
        let pro = 0;
  let y = document.getElementById("myDIV");
  let zzz = document.getElementById("que").innerHTML;
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
        document.getElementById("que").innerHTML = pro;
        console.log(percentage_complete, 'this is from function');
        if ( pro < 100) {

        pro = pro + (1/percentage_complete);
        changeProgress(pro);

        }
        }
    }
    setInterval(make_request, 125);
    var percentage_complete = 1;
    text = "";


    y.style.display = "block";


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