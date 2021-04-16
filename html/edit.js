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
    row.appendChild(hiddenRowInput);

    let hiddenDeleteInput = document.createElement("input");
    hiddenDeleteInput.setAttribute("name", "delete");
    hiddenDeleteInput.value = false;
    hiddenDeleteInput.style = "display:none;";
    row.appendChild(hiddenDeleteInput);


    for (let i = 0; i < 6; i++) {
        let d = tds[i];
        let input = document.createElement("input");
        input.setAttribute("name", d.className);
        input.value = d.innerText;
        d.innerText = "";
        d.appendChild(input);
    }

    tds[6].querySelector("a").remove();

    let submit = document.createElement("a");
    submit.innerText = "🖫";
    submit.onclick = () => document.getElementById("editForm").submit();
    tds[6].appendChild(submit);

    let remove = document.createElement("a");
    remove.innerText = "🗑";
    remove.onclick = () => {
        document.querySelector("input[name=delete]").value = true;
        document.getElementById("editForm").submit();
    }
    tds[6].appendChild(remove);
}

function doneEditing(rowNumber) {
    edditing = -1;
}