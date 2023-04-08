/* --------------------------------------------- 
# SCRIPTS 
--------------------------------------------- */

// 1) Script to auto close the alert after 3s
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function() {
        $(this).remove();
    });
}, 3000);