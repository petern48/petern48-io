// Copy the content of the html tag to the client's clipboard
function copyToClipboard(id) {
    let text = document.getElementById(id).innerHTML;
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied " + text + " to clipboard");
    });
}