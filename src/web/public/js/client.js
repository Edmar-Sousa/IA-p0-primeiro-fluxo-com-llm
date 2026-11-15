
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

function createButtonRetry() {

    const buttonElement = document.createElement('button')
    buttonElement.classList.add('button-empty')

    buttonElement.innerHTML = `<svg 
        xmlns="http://www.w3.org/2000/svg" 
        width="24" 
        height="24" 
        viewBox="0 0 24 24" 
        fill="none" 
        stroke="currentColor" 
        stroke-width="2" 
        stroke-linecap="round" 
        stroke-linejoin="round">
            <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
            <path d="M3 3v5h5"/>
    </svg>`

    return buttonElement
}

function createMessageElement(params) {
    const { message, reverse = false, isError = false, isRetry = false  } = params

    const messageElement = document.createElement('div')
    const textMessageContainerElement = document.createElement('div')
    const userCircleElement = document.createElement('div')

    const now = new Date()
    const minutes = now.getMinutes().toString().padStart(2, '0')

    messageElement.classList.add('message')

    if (reverse) {
        messageElement.classList.add('right')
        textMessageContainerElement.classList.add('right')
    }

    textMessageContainerElement.classList.add('text-message')

    if (isError) {
        textMessageContainerElement.classList.add('error')
    }

    userCircleElement.classList.add('user-circle')
    userCircleElement.innerText = 'VC'

    const messageTimeElement = document.createElement('p')
    const messageTextElement = document.createElement('p')

    messageTextElement.innerText = message
    
    messageTimeElement.innerText = `${now.getHours()}:${minutes}`
    messageTimeElement.classList.add('message-time')


    textMessageContainerElement.appendChild(messageTextElement)
    textMessageContainerElement.appendChild(messageTimeElement)

    messageElement.appendChild(reverse ? textMessageContainerElement : userCircleElement)
    messageElement.appendChild(reverse ? userCircleElement : textMessageContainerElement)

    if (isRetry) {
        const containerRetryElement = document.createElement('div')
        const buttonRetryElement = createButtonRetry()

        containerRetryElement.classList.add('message-retry-container')

        containerRetryElement.appendChild(messageElement)
        containerRetryElement.appendChild(buttonRetryElement)

        return containerRetryElement
    }

    return messageElement
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

    return {
        status: response.status,
        ...body
    }
}



async function insertMessageBeforeLLMLoaddingElement(messageElement) {
    const llmAnimationElement = document.querySelector('.animation-llm-response')
    llmAnimationElement.parentNode.insertBefore(messageElement, llmAnimationElement)
}


async function addMessageElementAndSendRequestToAPI(message) {
    toggleLLMResponseAnimation()

    const messageElement = createMessageElement({ message, reverse: true })
    insertMessageBeforeLLMLoaddingElement(messageElement)

    const response = await sendMessageToAPI(message)
    
    let statusCode = 0, isError = false, isRetry = false
    let statusAllowedRetry = ['JSON_LLM_RESPONSE_ERROR', 'LLM_TIMEOUT_ERROR', 'LLM_SERVICE_UNAVAILABLE']


    if (response.status != 200) {
        isRetry = statusAllowedRetry.includes(response.code_str)
        isError = true
    }
    
    let llmMessageElement = createMessageElement({ 
        message: response.message, 
        isError,
        isRetry,
    })

    insertMessageBeforeLLMLoaddingElement(llmMessageElement)

    toggleLLMResponseAnimation()
}


async function addMessagesHistoryInChat(messages) {

    for (let msg of messages) {
        const messageElement = createMessageElement({ message: msg.message, reverse: msg.type != 'system' })
        insertMessageBeforeLLMLoaddingElement(messageElement)
    }

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

    addMessagesHistoryInChat(body.chat)
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