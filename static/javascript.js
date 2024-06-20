function myFunction() {
  var y = document.getElementById("myDIV");
  let x = document.getElementById("numb").value;
  let text;
  let result = x.includes("https://www.youtube.com/watch?");
  let result1 = x.includes("https://youtu.be");

  if ((result || result1) != true) {
    text = "Input not valid";
  } else {
    text = "Analyzing video";
    y.style.display = "block";
    document.getElementById('theForm').submit();

  }
  document.getElementById("validation").innerHTML = text;
}

const progressbar = document.querySelector(".progress");

const changeProgress = (progress) => {
  progressbar.style.width = `${progress}%`;
  if (progress === 39) {
  document.getElementById("validation").innerHTML = 'Finding most important facts';
  }
  if (progress === 69) {
  document.getElementById("validation").innerHTML = 'Final touch';
  }
};

/* change progress after 1 second (only for showcase) */
setTimeout(() => changeProgress(5), 2000);
setTimeout(() => changeProgress(22), 4600);
setTimeout(() => changeProgress(33), 5266);
setTimeout(() => changeProgress(39), 8000);
setTimeout(() => changeProgress(55), 10000);
setTimeout(() => changeProgress(69), 11200);
setTimeout(() => changeProgress(81), 12500);
setTimeout(() => changeProgress(100), 13200);