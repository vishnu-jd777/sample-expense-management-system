import './style.css'

type Expense = {
  id: number
  title: string
  amount: number
  category: string
  date: string
}

let expenses: Expense[] = []
let nextId = 1

const filterInput = document.getElementById('filter') as HTMLSelectElement
const form = document.getElementById('expense-form') as HTMLFormElement
const titleInput = document.getElementById('title') as HTMLInputElement
const amountInput = document.getElementById('amount') as HTMLInputElement
const categoryInput = document.getElementById('category') as HTMLSelectElement
const dateInput = document.getElementById('date') as HTMLInputElement
const expenseList = document.getElementById('expense-list') as HTMLTableSectionElement
const totalEl = document.getElementById('total') as HTMLSpanElement

form.addEventListener('submit', (event) => {
  event.preventDefault()

  const expense: Expense = {
    id: nextId++,
    title: titleInput.value.trim(),
    amount: Number(amountInput.value),
    category: categoryInput.value,
    date: dateInput.value,
  }

  expenses.push(expense)
  renderExpenses()
  form.reset()
})

function renderExpenses(): void {
  expenseList.innerHTML = ''
  const visible =
  filterInput.value === 'all'
    ? expenses
    : expenses.filter((expense) => expense.category === filterInput.value)

  for (const expense of visible) {
    const row = document.createElement('tr')

    const values = [expense.title, `₹${expense.amount}`, expense.category, expense.date]
    for (const value of values) {
      const cell = document.createElement('td')
      cell.textContent = value
      row.appendChild(cell)
    }

    const actionCell = document.createElement('td')
    row.appendChild(actionCell)
    const deleteButton = document.createElement('button')
    deleteButton.textContent = 'Delete'
    deleteButton.addEventListener('click', () => deleteExpense(expense.id))
    actionCell.appendChild(deleteButton)

    expenseList.appendChild(row)
  }
  updateTotal(visible)
}

function deleteExpense(id: number): void {
  expenses = expenses.filter((expense) => expense.id !== id)
  renderExpenses()
}

function updateTotal(list: Expense[]): void {
  const total = list.reduce((sum, expense) => sum + expense.amount, 0)
  totalEl.textContent = String(total)
}

filterInput.addEventListener('change', renderExpenses)