


// All users to track their orders in real-time
document.addEventListener('DOMContentLoaded', function () {
    const trackButton = document.getElementById('track-button');
    const orderidInput = document.getElementById('orderid-input');
    const statusDisplay = document.getElementById('status-display');

    // Fetch order status from the server and update the display on button click
    trackButton.addEventListener('click', function () {
        const orderid = orderidInput.value.trim();
        if (!orderid) {
            alert('Please enter a valid Order ID.');
            return;
        }
        // Send a request to the server to get the order status
        fetch('/api/track-order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ orderid: orderid })
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    statusDisplay.textContent = data.error;
                } else {
                    statusDisplay.textContent = 'Order Status: ' + data.status + ' | Location: ' + data.location;
                }
            })
            .catch(() => {
                statusDisplay.textContent = 'Failed to fetch order status.';
            });
    });
});