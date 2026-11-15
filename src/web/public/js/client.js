
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

async function toggleLLMResponseAnimation() {
    const animationElement = document.querySelector('.animation-llm-response')
    animationElement.classList.toggle('hidden')
}

async function enableInputsAndButtons() {
    const inputMessageElement = document.querySelector('.input-message')
    const buttonSendMsgElement = document.querySelector('.button-send-message')

    inputMessageElement.disabled = false
    buttonSendMsgElement.disabled = false
}


async function sendMessageToAPI(message) {
    const response = await fetch('/process-message', {
        method: 'POST',
        body: JSON.stringify({ message }),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    const body = await response.json()
    console.log(body)
}


async function insertUserMessageElement(message) {
    const messageElement = document.createElement('div')
    const textMessageContainerElement = document.createElement('div')
    const userCircleElement = document.createElement('div')

    const now = new Date()

    messageElement.classList.add('message')
    messageElement.classList.add('right')

    textMessageContainerElement.classList.add('text-message')
    textMessageContainerElement.classList.add('right')

    userCircleElement.classList.add('user-circle')
    userCircleElement.innerText = 'VC'


    const messageTimeElement = document.createElement('p')
    const messageTextElement = document.createElement('p')

    messageTextElement.innerText = message

    const minutes = now.getMinutes().toString().padStart(2, '0')

    messageTimeElement.innerText = `${now.getHours()}:${minutes}`
    messageTimeElement.classList.add('message-time')

    textMessageContainerElement.appendChild(messageTextElement)
    textMessageContainerElement.appendChild(messageTimeElement)

    messageElement.appendChild(textMessageContainerElement)
    messageElement.appendChild(userCircleElement)


    const llmAnimationElement = document.querySelector('.animation-llm-response')
    llmAnimationElement.parentNode.insertBefore(messageElement, llmAnimationElement)
}


async function addMessageElementAndSendRequestToAPI(message) {
    toggleLLMResponseAnimation()
    insertUserMessageElement(message)
    await sendMessageToAPI(message)
    toggleLLMResponseAnimation()
}


async function sendMessageToBot() {
    const textareaElement = document.querySelector('.input-message')

    const message = textareaElement.value
    textareaElement.value = ''

    if (message.length > 0) {
        addMessageElementAndSendRequestToAPI(message)
    }
    
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