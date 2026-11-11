
let intervalId = null

function createOrder(order) {

    const div = document.createElement('div')
    const resume = document.createElement('p')
    const priority = document.createElement('p')
    const address = document.createElement('p')
    const h4 = document.createElement('h4')
    const ul = document.createElement('ul')

    resume.innerHTML = `<b>Resume:</b> ${order.summary}`
    priority.innerHTML = `<b>Prioridade:</b> ${order.priority}`
    address.innerHTML = `<b>Endereço:</b> ${order.order.address}`
    h4.innerText = 'Pedido:'

    for (food of order.order.foods) {
        const li = document.createElement('li')

        li.innerText = food
        ul.appendChild(li)
    }

    for (drink of order.order.drinks) {
        const li = document.createElement('li')
        
        li.innerText = drink
        ul.appendChild(li)
    }

    div.classList.add('order')

    div.appendChild(resume)
    div.appendChild(priority)
    div.appendChild(address)
    div.appendChild(h4)
    div.appendChild(ul)

    return div
}

function createComplaint(complaint) {

    const div = document.createElement('div')
    const resume = document.createElement('p')
    const priority = document.createElement('p')


    resume.innerHTML = `<b>Resume:</b> ${complaint.summary}`
    priority.innerHTML = `<b>Prioridade:</b> ${complaint.priority}`


    div.classList.add('complaint')

    div.appendChild(resume)
    div.appendChild(priority)

    return div
}


function updateResumeColumns(resume) {
    const ordersColumn = document.querySelector('.orders')
    const complaintsColumn = document.querySelector('.complaints')
    const complimentsColumn = document.querySelector('.compliments')

    ordersColumn.innerHTML = ''
    complaintsColumn.innerHTML = ''
    complimentsColumn.innerHTML = ''

    for (let order of resume.orders) {
        const ordersElement = createOrder(order)
        ordersColumn.appendChild(ordersElement)
    }

    for (let complaint of resume.complaints) {
        const complaintElement = createComplaint(complaint)
        complaintsColumn.appendChild(complaintElement)
    }

    for (let compliment of resume.compliments) {
        const complimentElement = createComplaint(compliment)
        complimentsColumn.appendChild(complimentElement)
    }
}


async function fetchResume() {
    const response = await fetch('/dashboard')
    return await response.json()
}

async function updateResume() {
    const body = await fetchResume()
    updateResumeColumns(body)
}

function main() {
    updateResume()
    intervalId = setInterval(updateResume, 5000)
}


document.addEventListener('DOMContentLoaded', main)
window.onbeforeunload = function () {
    clearInterval(intervalId)
    console.log('limpando o interval')
}
