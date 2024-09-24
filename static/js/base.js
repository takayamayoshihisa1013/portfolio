document.addEventListener('DOMContentLoaded', function() {
    const $menu768 = document.querySelector(".menu768 i");
    const $sideNav = document.querySelector(".sideNav");
    
    $menu768.addEventListener("click", function() {
        $sideNav.style.right = "0";
    })

    document.addEventListener("click", function(event) {
        if (!$sideNav.contains(event.target) && !$menu768.contains(event.target)) {
            $sideNav.style.right = "-80%";
        }
    })
})