
async function updateBotStatus(status) {
    const screenStatusElement = document.querySelector('.status')
    screenStatusElement.innerText = status
}

async function updateScreenToError() {
    const screenErrorState = document.querySelector('.screen-error-state')
    const chatMessageElement = document.querySelector('.chat-messages')
    const inputMessageElement = document.querySelector('.input-message-container')

    chatMessageElement.classList.add('hidden')
    inputMessageElement.classList.add('hidden')
    screenErrorState.classList.remove('hidden')
}


async function hiddenCircularLoadding() {
    const circularLoaddingElement = document.querySelector('.circular-loadding')
    circularLoaddingElement.classList.add('hidden')
}

async function enableInputsAndButtons() {
    const inputMessageElement = document.querySelector('.input-message')
    const buttonSendMsgElement = document.querySelector('.button-send-message')

    inputMessageElement.disabled = false
    buttonSendMsgElement.disabled = false
}



async function sendMessageToBot() {
    const textareaElement = document.querySelector('.input-message')

    const message = textareaElement.value
    console.log(message)
    
    textareaElement.value = ''
}


function registerClickEventInButton() {
    const buttonSendMsgElement = document.querySelector('.button-send-message')
    buttonSendMsgElement.addEventListener('click', sendMessageToBot)
}


async function messageHistory() {
    const response = await fetch('/chat/messages')
    const body = await response.json()

    hiddenCircularLoadding()
    enableInputsAndButtons()
    registerClickEventInButton()
}



async function checkStatusBot() {
    const response = await fetch('/health')
    const body = await response.json()

    updateBotStatus(body.status)
    
    if (response.status == 500) {
        updateScreenToError()
        return
    }

    messageHistory()
}


function main() {
    checkStatusBot()
}



document.addEventListener('DOMContentLoaded', main)