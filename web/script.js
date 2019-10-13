var inn1 = document.getElementById("inner1");
var inn2 = document.getElementById("inner2");
var p_sub = document.getElementById("poem-submitter");
var p_con = document.getElementById("poem-container");

document.getElementById("btn-submit").onclick = () => {
  var verse = document.getElementById("poem-submitter").value.split(" ");
  var last_w = verse[verse.length - 1];
  var req = new XMLHttpRequest();
  req.open("GET", "http://0.0.0.0:5000/api?w=" + last_w, true);
  req.send();

  req.onreadystatechange = e => {
    p_con.innerHTML =
      "Roses are red, <br /> " + req.responseText + ", <br /> " + p_sub.value;
  };

  inn2.classList.remove("flipped");
  inn1.classList.add("flipped");
};

document.getElementById("btn-back").onclick = () => {
  inn1.classList.remove("flipped");
  inn2.classList.add("flipped");
  p_sub.value = "";
};


inn2.classList.add("flipped");
setTimeout(() => {inn2.style="visibility: visible"}, 1000);
