function removeAllItemsFromLocalStorage() {
    localStorage.removeItem("snack_id");
    localStorage.removeItem("snack_username");
    localStorage.removeItem("snack_token");
}

function delCheck() {
    var userId = localStorage.getItem("snack_id");
    if(!confirm("정말로 탈퇴하시겠습니까?")) return false;
    $.ajax({
        url: "/api/user/"+userId+"/",
        type: "DELETE",
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
    var data="";
    if(isUpgrade) data = {"is_staff": true, "is_superuser": true};
    else data = {"is_staff": false, "is_superuser": false};
    $.ajax({
        url: "/api/user/"+userId+"/",
        type: "PATCH",
        data: data,
        headers: {
            "Authorization": "Token "+token,
        },
    }).done(function(res){
        window.location.reload();
    }).fail(function(request, status, error){
        alert(request.responseText);
    })
}