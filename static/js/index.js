const server = 'http://127.0.0.1:5000'
$('#execute').click(()=>{
    let db = $("#path").val()
    let query = $("#query").val()
    $("#bottom span")[0].textContent = "Executing query..."

    // ----------- FETCH ----------------------

   
    let config ={
        mode: 'no-cors',
        method: 'POST',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify( {
            "query": query,
            "db": db

        })
    }
    async function f(){
        const response = await fetch('http://127.0.0.1:5000/query',config)
        //console.log(response)
        const data = await response.json()
        console.log(data)
        table = document.createElement("table")
        table.className="table bordered"
        thead = document.createElement("thead")
        // ----------------- GET COLUMNS -------------------
        data.columns.forEach((c)=>{
            th = document.createElement("th")
            th.innerText = c
            thead.appendChild(th)
        })
        table.appendChild(thead)
        // ----------------- GET data -------------------
        data.content.forEach((r)=>{
            row = document.createElement("tr")
            r.forEach((d)=>{
                cell = document.createElement("td")
                cell.innerText = d
                row.appendChild(cell)
            })
            table.appendChild(row)
        })
        // ------------------ GET COUNT ----------------------

        $("#bottom span")[0].textContent = data.content.length +" rows gathered."

        // ------------------ INSERT DOM ----------------------
        $("#table").empty()
        $("#table").append(table)
    }
    f()


    
    //.then(response=>response.json())
    
    

    
    
    /*,{
        method: 'POST',
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json'
        }
        //body: JSON.stringify({})
    }).then(response => response.json())
    .then(data => console.log(data))*/

})