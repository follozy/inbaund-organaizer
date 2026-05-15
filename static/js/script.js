document.addEventListener("DOMContentLoaded", function() {
    start(SERVER_DATA);
    
});

async function start(data) {
    console.log(data)
    const body = document.getElementById('body')


    const header_div = document.createElement('div')
    header_div.id = 'header_div'
    body.appendChild(header_div)

    const nav_div = document.createElement('div')
    nav_div.id = 'nav_div'
    header_div.appendChild(nav_div)

    const menus = ['users_list', 'servers_list', 'add_server']
    const name_menus = ['list of user', 'list of server', 'add new server']

    for(key in menus){
        const link = document.createElement('a')
        link.className = 'nav_link'
        link.href = `/page?page=${menus[key]}`
        link.innerHTML = name_menus[key]
        nav_div.appendChild(link)
    }


    const content_div = document.createElement('div')
    content_div.id = 'content_div'
    body.appendChild(content_div)


    if (data['type'] == 'users_list'){
        const list_client = document.createElement('ul')
        list_client.id = 'list_client'
        content_div.appendChild(list_client)

        const update_b = document.createElement('button')
        update_b.id = 'update_b'
        update_b.innerHTML = 'update users in db'
        header_div.appendChild(update_b)

        update_b.addEventListener('click', async function(event) {
            const response = await fetch('/api?type=users&action=update')
            console.log('user_updated')
        })

        const Tresponse = await fetch(`/api?type=users&action=list`)
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
            client_page.href = `/page?page=user&id=${clients[key]['id']}`
            
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
        server_form.action = window.location.host
        content_div.appendChild(server_form)

        server_form.addEventListener('submit', async function(event){
            event.preventDefault()

            const data_server = new FormData(server_form)
            console.log(data_server)

            try {
            const response = await fetch('/api?type=servers&action=add_server', {
            method: 'POST',
            body: data_server // Отправляем данные
            });
            const result = await response.json();
            console.log(result);
            } catch (error) {
            console.error('Ошибка:', error);
            }

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

    if (data['type'] == 'user'){
        const Tresponse = await fetch(`/api?type=users&action=take_one&id=${data['id']}`)
        const user = await Tresponse.json()
        console.log(user)

        const center_div = document.createElement('div')
        center_div.id = 'center_div'
        content_div.appendChild(center_div)

        for (key in user){
            const text = document.createElement('p')
            text.className = 'user_stat'
            center_div.appendChild(text)
            if (key == 'created' || key == 'lustupdate'){
                text.innerHTML = `${key}:${Date(user[key]).toLocaleString()}`
            }else{
                text.innerHTML = `${key}:${user[key]}`
            }
            
            

        }
    }
}
