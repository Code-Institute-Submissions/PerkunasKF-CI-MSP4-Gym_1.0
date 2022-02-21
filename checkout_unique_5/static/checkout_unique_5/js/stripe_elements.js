/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key_unique').text().slice(1, -1);
var clientSecret = $('#id_client_secret_unique').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element-unique');

// Handle form submit
var form = document.getElementById('payment-form-unique');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button-unique').attr('disabled', true);
    $('#payment-form-unique').fadeToggle(100);
    $('#loading-overlay-unique').fadeToggle(100);

    // From ussing {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };
    // var url = '/checkout_unique_5/cache_checkout_data/';
    console.log('------ Test ----------')
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    username: $.trim(form.username.value),
                    email: $.trim(form.email.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                console.log('---------error---------')
                var errorDiv = document.getElementById('card-errors-unique');
                var html = `
                    <span role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form-unique').fadeToggle(100);
                $('#loading-overlay-unique').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button-unique').attr('disabled', false);
            } else {
                console.log('--------succeeded----------')
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // jus reload the page, the error will be in django messages
        location.reload();
    })
// });