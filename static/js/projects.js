function scrollToSection(sectionId) {
    console.log('Scolling');
    document.getElementById(sectionId)
    .scrollIntoView(alignToTop=true, behavior='smooth');
}