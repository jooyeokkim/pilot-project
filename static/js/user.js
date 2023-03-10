function removeAllItemsFromLocalStorage() {
    localStorage.removeItem("snack_username");
    localStorage.removeItem("snack_token");
}

function delCheck() {
    if(!confirm("정말로 탈퇴하시겠습니까?")) return false;
    $.ajax({
        url: "/api/user/quit/",
        type: "GET",
        headers: {
          "Authorization": "Token "+token,
        },
    }).done(function(res) {
        alert("탈퇴되었습니다.");
        removeAllItemsFromLocalStorage();
        window.location.replace("/");
    }).fail(function(request, status, error) {
        alert(request.responseText);
    })
}

function logoutCheck(){
    if(!confirm("로그아웃 하시겠습니까?")) return false;
    alert("로그아웃 되었습니다.")
    removeAllItemsFromLocalStorage();
    window.location.replace("/");
}

function changeAuth(userId, isUpgrade) {
    var grade = "downgrade";
    if(isUpgrade) grade = "upgrade";
    $.ajax({
        url: "/api/user/"+userId+"/"+grade+"/",
        type: "GET",
        headers: {
            "Authorization": "Token "+token,
        },
    }).done(function(res){
        window.location.reload();
    }).fail(function(request, status, error){
        alert(request.responseText);
    })
}