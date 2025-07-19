 const photoInput = document.getElementById('pfpin');
  const pfp = document.getElementById('pfp');

  photoInput.addEventListener('change', function imageChanged  () {
    const file = photoInput.files[0];
    if (file) { //if the user has uploded a photo
      const reader = new FileReader();

      reader.addEventListener('load',function display (e)  {
        pfp.src = '';
        pfp.src = e.target.result;
        pfp.style.display = "block";
      });

      reader.readAsDataURL(file);
    }
  });