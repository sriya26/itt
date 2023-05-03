let customers = [];

function Charges(hoursParked) {
  let totalCharges = 0;
  if (hoursParked <= 3) {
    totalCharges = 2;
  } else {
    totalCharges = 2 + 0.5 * (hoursParked - 3);
  }
  return totalCharges;
}

function addCustomer(hoursParked) {
  let customerCharges = Charges(hoursParked);
  customers.push({
    hoursParked: hoursParked,
    charges: customerCharges,
  });
  return customerCharges;
}

function displayCustomers() {
  let output = "";
  for (let i = 0; i < customers.length; i++) {
    let customer = customers[i];
    output += "Customer " + (i + 1) + ": " + customer.hoursParked + " hours - Rs. " + customer.charges.toFixed(2) + "<br>";
  }
  document.getElementById("customers").innerHTML = output;
}

function handleSubmit() {
  let hoursParked = document.getElementById("hoursParked").value;
  let customerCharges = addCustomer(hoursParked);
  document.getElementById("charges").innerHTML = "Charges: Rs. " + customerCharges.toFixed(2);
  displayCustomers();
}
