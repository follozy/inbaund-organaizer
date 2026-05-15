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
    if (data['type'] == 'main'){
        const list_client = document.createElement('ul')
        list_client.id = 'list_client'
        content_div.appendChild(list_client)

        const Tresponse = await fetch(`/api?type=users`)
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

    if (data['type'] == 'add_server'){
        const lable = document.createElement('label')
        lable.id = 'server_add_lable'
        lable.innerHTML = 'Здесь вершатся сервера'
        content_div.appendChild(lable)

        const server_form = document.createElement('form')
        server_form.id = 'server_form'
        server_form.method = 'POST'
        server_form.action = window.location.host + '/api?action=add_server'
        content_div.appendChild(server_form)

        server_form.addEventListener('submit', function(event){
            event.preventDefault()

            const data_server = new FormData(server_form)
            console.log(data_server)

        })

        const Tresponse = await fetch(`/api?type=tables&name=servers`)
        const columns = await Tresponse.json()
        console.log(columns)
        for (key in columns){
            if (key == 0){
                continue
            }
            const field = document.createElement('input')
            field.id = `field_${columns[key]}`
            field.className = 'server_field'
            field.type = 'text'
            field.name = columns[key]
            field.placeholder = `${columns[key]} field`
            server_form.appendChild(field)

            const label_field = document.createElement('label')
            label_field.className = 'server_fields_label'
            label_field.innerHTML = columns[key]
            server_form.appendChild(label_field)

            server_form.appendChild(document.createElement('br'))
        }
        const send_data_b = document.createElement('input')
        send_data_b.id = 'send_data_b'
        send_data_b.type = 'submit'
        send_data_b.value = 'Add server'
        server_form.appendChild(send_data_b)


    }
}