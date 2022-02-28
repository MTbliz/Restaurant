var slideIndex = 1;

// Next/previous controls
function plusSlides(n) {
  changePrevNextButtonsPosition()
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  changePrevNextButtonsPosition()
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  var captionText = document.getElementById("caption");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function changePrevNextButtonsPosition(){
  var prevButton = document.getElementsByClassName("prev")[0];
  var nextButton = document.getElementsByClassName("next")[0];
  prevButton.style.marginLeft = "22.4%";
  nextButton.style.marginRight = "23.7%";
  prevButton.style.marginTop = "10%";
  nextButton.style.marginTop = "10%";
}