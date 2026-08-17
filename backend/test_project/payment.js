async function makePayment(amount) {

    const response = await axios.post(
        "https://api.payment.com/payment",
        {
            amount: amount
        }
    );

    const data = response.data;

    return data;
}


async function getPayment(paymentId) {

    const response = await axios.get(
        "https://api.payment.com/payment/" + paymentId
    );

    return response.data;
}