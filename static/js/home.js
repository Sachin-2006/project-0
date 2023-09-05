function openPopup(imageSrc) {
  var popup = document.getElementById('myModal');
  var popupImage = document.getElementById('popupImage');
  popup.style.display = 'block';
  popupImage.src = imageSrc;
}
function closepop(){
var popup = document.getElementById('myModal');
    popup.style.display = 'none';
}