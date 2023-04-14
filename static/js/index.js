var genre_btn1 = document.getElementById("option1");

var mo_tag = document.getElementById("MO_tag");

mo_tag.style.display = "none"; // 초기 상태를 'none'으로 설정
genre_btn1.addEventListener("click", function() {
    if( mo_tag.style.display == 'none'){
        mo_tag.style.display = "block";
    } else{
        mo_tag.style.display = "none";
    }
  });
