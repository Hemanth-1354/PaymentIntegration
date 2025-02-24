// script.js

document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Retrieve amount
    const amount = document.getElementById('amount').value;

    if (!amount || amount <= 0) {
        alert('Please enter a valid amount.');
        return;
    }

    // Simulate payment processing
    alert(`Proceeding to pay ₹${amount}`);
});
