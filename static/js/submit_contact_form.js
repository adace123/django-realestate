const alertBox = document.querySelector('#alert-dialog');
const userMessage = document.querySelector('#alert-text');

document.getElementById('contact-form').onsubmit = async e => {
    e.preventDefault();
    const formValues = Array.from(new FormData(e.target).entries()).reduce((acc, [k, v]) => {
        acc[k] = v;
        return acc;
    }, {});
    formValues.listing = e.target.dataset.listing;
    const response = await fetch('/contact/', {
        method: 'POST',
        body: JSON.stringify(formValues),
        headers: {
            'Content-Type': 'application/json',
            'X-XSRF-TOKEN': formValues.csrfmiddlewaretoken
        }
    });
    const json = await response.json();
    alertBox.style.display = 'block';
    if (response.status != 200) {
        userMessage.classList.remove('alert-success');
        userMessage.classList.add('alert-danger');
        userMessage.textContent = `Missing ${json.missing}`;
    } else {
        userMessage.classList.remove('alert-danger');
        userMessage.classList.add('alert-success');
        userMessage.textContent = "Successfully sent!";
    }
}