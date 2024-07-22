
function fastSubmit() {
document.getElementById('form-result').submit();
document.getElementById('formToHide').style.display = 'none';
document.getElementById('hiddenFormSpinner').style.display = 'flex';
document.getElementById('anotherToHide').style.display = 'flex';
}

function myFunction() {
        let pro = 0;
  let y = document.getElementById("myDIV");
  let x = document.getElementById("numb").value;
  let text;
  let result = x.includes("https://www.youtube.com/watch?");
  let result1 = x.includes("https://youtu.be");

  if ((result || result1) != true) {

      text = "Please enter correct youtube link";

  } else {

  function make_request(){
      console.log(pro)
        pro += 1;
        if (pro === 0) {
            document.getElementById("bar-description").innerHTML = 'We are processing your video';
        }
        if (pro === 50) {
            document.getElementById("bar-description").innerHTML = 'Finding most important facts';
        }
        if (pro === 100) {
            document.getElementById("bar-description").innerHTML = 'Let it cook';
        }
        if (pro === 180) {
            document.getElementById("bar-description").innerHTML = 'Video is quite long but we are getting there';
        }
        if (pro === 350) {
            document.getElementById("bar-description").innerHTML = 'It should not take much longer';
        }
    }
    setInterval(make_request, 100);

    y.style.display = "flex";

    document.getElementById('theForm').submit();
    document.getElementById('top-card').classList.add('display-none');
    document.getElementById('theForm').classList.add('display-none');
    document.getElementById('cardBody').classList.add('d-flexetc')
  }
  document.getElementById("validation").innerHTML = text;
}



function copyText() {
    let Text = document.getElementById("textbox").textContent;
    navigator.clipboard.writeText(Text);
}

function copyText2() {
    let Text = document.getElementById("textbox2").textContent;
    navigator.clipboard.writeText(Text);
}


document.getElementById('myVideo').playbackRate = 0.5;