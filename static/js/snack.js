function snackRequestListDone(snackRequests) {
    for (var i = 0; i < snackRequests.length; i++) {
        var snackRequest = snackRequests[i];
        var rowStr = "<tr>";
        rowStr += "<th>" + snackRequest.snack.name
            + "<br><button class=\"like btn btn-outline-primary mt-2\" style=\"font-size:10px\" onclick=\"express('like',"+snackRequest.id+")\">좋아요("+snackRequest.likes+")</button>"
            + "<button class=\"dislike btn btn-outline-danger mt-2 ms-1\" style=\"font-size:10px\" onclick=\"express('dislike',"+snackRequest.id+")\">싫어요("+snackRequest.dislikes+")</button>"
            + "</th>";
        rowStr += "<td><img src=\"" + snackRequest.snack.image + "\" width=\"100px\" height=\"100px\"></td>";
        rowStr += "<td><a href=\"" + snackRequest.snack.url + "\" style=\"font-size:12px\">구매 링크</a></td>";
        rowStr += "<td>" + snackRequest.description + "</td>";
        rowStr += "<td>" + snackRequest.create_dt + "</td>";
        if (snackRequest.is_accepted) rowStr += "<td><span style=\"color:mediumseagreen\">● </span>" + snackRequest.supply_year
            + "년 " + snackRequest.supply_month + "월 비치 예정</td>";
        else rowStr += "<td><span style=\"color:orange\">● </span>주문 대기중</td>";
        rowStr += "<td>";
        if (!snackRequest.is_accepted) rowStr += "<a href=\"/snack/" + snackRequest.id + "/edit/\" class=\"btn btn-outline-primary ms-2\">수정</a>";
        rowStr += "<a href=\"/snack/" + snackRequest.id + "/manage/\" class=\"btn btn-outline-success ms-2\">관리</a>";
        rowStr += "</td></tr>";
        $('#all-snack-table > tbody:last').append(rowStr);
    }
}

function createSnackNav(res, pageSize, currentPage){
    var totalPage = parseInt((Number(res.count)-1)/pageSize)+1;
    if(res.previous==null) var navStr = "<li class=\"page-item disabled\"><a class=\"page-link\">Previous</a></li>";
    else var navStr = "<li class=\"page-item\"><a href=\"#\" class=\"page-link\" onclick=\"getPaginatedSnackData("+(currentPage-1)+")\">Previous</a></li>";
    navStr += "<li class=\"ms-3 me-3 mt-1\"><span class=\"align-middle\">Page "+currentPage+" of "+totalPage+"</span></li>";
    if(res.next==null) navStr += "<li class=\"page-item disabled\"><a class=\"page-link\">Next</a></li>";
    else navStr += "<li class=\"page-item\"><a href=\"#\" class=\"page-link\" onclick=\"getPaginatedSnackData("+(currentPage+1)+")\">Next</a></li>";
    $('#pagination-nav > ul:last').html(navStr);
}

function express(emotion, snackRequestId) {
    $.ajax({
        url: "/api/snack_emotion/",
        type: "POST",
        data: {
            "name": emotion,
            "snack_request": snackRequestId
        },
        headers: {
            "Authorization": "Token " + token,
        },
        dataType: "json",
    }).done(function (res) {
        window.location.reload();
    }).fail(function (request, status, error) {
        alert(request.responseText);
    })
}

function isLogin() {
    if (localStorage.getItem("snack_username") == null) {
        alert("로그인이 필요합니다.");
        window.location.replace("/accounts/login/");
    }
}

function handleSnackUpdateFormData(formData) {
    if (!$("#id_is_accepted").is(":checked"))
        formData.append("is_accepted", "off");
    // if (!formData.get("image").size)
    //     formData.delete("image")
    return formData;
}

function snackUpdate(isAdmin) {
    var url_parts = window.location.href.split('/');
    var formData = new FormData($('#snack-update-form')[0]);
    // formData.append("image", $('[name="image"]')[0].files[0]);

    var urlPostfix = ""
    if (isAdmin) urlPostfix = "manage/"
    $.ajax({
        url: "/api/snack_request/" + url_parts[4] + "/" + urlPostfix,
        type: "PATCH",
        headers: {
            "Authorization": "Token " + token,
        },
        enctype: "multipart/form-data",
        data: handleSnackUpdateFormData(formData),
        processData: false,
        contentType: false,
    }).done(function (res) {
        window.location.replace('/');
    }).fail(function (request, status, error) {
        alert(request.responseText);
    })
};

function snackDelete() {
    if(!confirm("정말로 삭제하시겠습니까?")) return;
    var url_parts = window.location.href.split('/');
    $.ajax({
        url: "/api/snack_request/" + url_parts[4] + "/",
        type: "DELETE",
        headers: {
            "Authorization": "Token " + token,
        },
    }).done(function (res) {
        window.location.replace('/');
    }).fail(function (request, status, error) {
        alert(request.responseText);
    })
}