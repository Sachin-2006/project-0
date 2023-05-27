function openModal() {
      var modal = document.getElementById("myModal");
      modal.style.display = "block";
    }

    // Function to close the modal
    function closeModal() {
      var modal = document.getElementById("myModal");
      modal.style.display = "none";
    }

    // Close the modal when the user clicks anywhere outside of it
    window.onclick = function (event) {
      var modal = document.getElementById("myModal");
      if (event.target == modal) {
        modal.style.display = "none";
      }
    };
