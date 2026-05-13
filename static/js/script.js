document.addEventListener("DOMContentLoaded", function() {
    start(SERVER_DATA);
});

async function start(data) {
    console.log(data)
    const body = document.getElementById('body')
    const base_div = document.createElement('div')
    base_div.id = 'base_id'
    body.appendChild(base_div)

    const header_div = document.createElement('div')
    header_div.id = 'header_div'
    base_div.appendChild(header_div)

    const content_div = document.createElement('div')
    content_div.id = 'content_div'
    base_div.appendChild(content_div)

    const list_client = document.createElement('ul')
    list_client.id = 'list_client'
    content_div.appendChild(list_client)

    const Tresponse = await fetch(`/api`)
    const clients = await Tresponse.json()
    console.log(clients)

    for (let key in clients){
        const client_li = document.createElement('li')
        client_li.className = 'client_li'
        list_client.appendChild(client_li)

        const li_div = document.createElement('div')
        li_div.className = 'li_div'
        client_li.appendChild(li_div)

        const client_page = document.createElement('a')
        client_page.className = 'client_link'
        li_div.appendChild(client_page)
        client_page.innerHTML = clients[key]['email']
        client_page.href = 'http://127.0.0.1:5000/'
        
    }
}