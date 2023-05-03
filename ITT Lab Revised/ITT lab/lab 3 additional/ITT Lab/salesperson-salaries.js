const minSalary = 200;
const maxSalary = 1000;
const salaryRange = 100;
const numRanges = (maxSalary - minSalary) / salaryRange + 1;
let salesCounts = new Array(numRanges).fill(0);

function addSales() {
  const salesInput = document.getElementById('sales-input');
  const sales = parseInt(salesInput.value);
  if (isNaN(sales) || sales < 0) {
    alert('Please enter a valid sales amount.');
    return;
  }

  let salary = 200 + 0.09 * sales;
  if (salary > maxSalary) {
    salary = maxSalary;
  }
  let range = Math.floor((salary - minSalary) / salaryRange);
  salesCounts[range]++;
  updateList();
  salesInput.value = '';
}

function updateList() {
  const salesList = document.getElementById('sales-list');
  salesList.innerHTML = '';
  for (let i = 0; i < numRanges; i++) {
    let salaryStart = minSalary + i * salaryRange;
    let salaryEnd = salaryStart + salaryRange - 1;
    if (salaryEnd > maxSalary) {
      salaryEnd = maxSalary;
    }
    let label = `$${salaryStart}-${salaryEnd}`;
    let count = salesCounts[i];
    let item = document.createElement('p');
    item.textContent = `${label}: ${count}`;
    salesList.appendChild(item);
  }
}
