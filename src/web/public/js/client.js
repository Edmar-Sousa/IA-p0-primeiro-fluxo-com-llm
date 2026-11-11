
function remove_loadding() {
    document.querySelector('.loadding-state').classList.add('hidden')
}

function update_status_bot(body) {
    const status = document.querySelector('.status')

    status.classList.add(body.status)
    status.innerText = body.status
}

function update_screen_to_chat(body) {
    remove_loadding()
    document.querySelector('.message-input-area').classList.remove('hidden')
    document.querySelector('.messages-area').classList.remove('hidden')
    update_status_bot(body)
}


function update_screen_to_error(body) {
    remove_loadding()

    const errorScreen = document.querySelector('.error')
    const h3 = errorScreen.querySelector('h3')

    errorScreen.classList.remove('hidden')
    h3.innerText = body.details

    update_status_bot(body)
}


async function check_status_bot() {
    const response = await fetch('/health')
    const body = await response.json()

    if (response.status == 200)
        update_screen_to_chat(body)
    else 
        update_screen_to_error(body)
}


function main() {
    check_status_bot()
}



document.addEventListener('DOMContentLoaded', main)