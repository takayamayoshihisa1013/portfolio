function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId); // 修正: `sectionId`をそのまま使用
    window.scrollTo({
        top: element.offsetTop,
        behavior: 'smooth'
    });
}

document.addEventListener("DOMContentLoaded", function () {
    const hash = window.location.hash;
    if (hash) {
        const targetElement = document.getElementById(hash.substring(1));
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop,
                behavior: 'smooth'
            });
        }
    }
});