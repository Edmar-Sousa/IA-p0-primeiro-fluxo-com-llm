
function removeLoadding() {
    document.querySelector('.loadding-state').classList.add('hidden')
}


function addMessage(isSystem, message) {

    const messagesArea = document.querySelector('.messages-area') 
    const div = document.createElement('div')
    const p = document.createElement('p')

    div.classList.add('message')
    div.classList.add(isSystem ? 'left' : 'right')

    p.innerText = message

    div.appendChild(p)
    messagesArea.appendChild(div)
}


async function processMessage(message) {

    addMessage(false, message)

    const response = await fetch('/process-message', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }) 
    })

    const body = await response.json()
    addMessage(true, body.content)
}

function sendMessageToBot() {
    const input = document.querySelector('.input-message')
    const message = input.innerText

    if (message.length > 0) {
        processMessage(message)
    }
}

function updateStatusBot(body) {
    const status = document.querySelector('.status')

    status.classList.add(body.status)
    status.innerText = body.status
}

function registerEventsToSendMessage() {
    document.querySelector('.btn-send').addEventListener('click', sendMessageToBot)
}

function updateScreenToChat(body) {
    removeLoadding()
    document.querySelector('.message-input-area').classList.remove('hidden')
    document.querySelector('.messages-area').classList.remove('hidden')
    updateStatusBot(body)

    registerEventsToSendMessage()
}


function updateScreenToError(body) {
    removeLoadding()

    const errorScreen = document.querySelector('.error')
    const h3 = errorScreen.querySelector('h3')

    errorScreen.classList.remove('hidden')
    h3.innerText = body.details

    updateStatusBot(body)
}


async function checkStatusBot() {
    const response = await fetch('/health')
    const body = await response.json()

    if (response.status == 200)
        updateScreenToChat(body)
    else 
        updateScreenToError(body)
}


function main() {
    checkStatusBot()
}



document.addEventListener('DOMContentLoaded', main)