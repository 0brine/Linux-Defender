let table = document.getElementById("table");
let edditing = -1;

function edit(rowNumber) {
    if (edditing != -1)
        return;

    edditing = rowNumber;

    let row = table.querySelector("tr.row-" + rowNumber);
    let tds = row.querySelectorAll("td");

    let hiddenRowInput = document.createElement("input");
    hiddenRowInput.setAttribute("name", "row");
    hiddenRowInput.value = rowNumber;
    hiddenRowInput.style = "display:none;";
    row.appendChild(hiddenRowInput)


    for (let i = 0; i < 5; i++) {
        let d = tds[i];
        let input = document.createElement("input");
        input.setAttribute("name", d.className);
        input.value = d.innerText;
        d.innerText = "";
        d.appendChild(input);
    }

    tds[5].querySelector("a").remove();
    let submit = document.createElement("input");
    submit.setAttribute("type","submit");
    submit.value = "🖫";
    submit.click = () => doneEditing(rowNumber);
    tds[5].appendChild(submit);

}

function doneEditing(rowNumber) {
    edditing = -1;
}