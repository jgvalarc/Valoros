console.log("Bruh, you be loggin", 69);
const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn");
const form = document.querySelector("#registrationForm");

const handleToggleInput = (e) => {

    if(showPasswordToggle.textContent === "SHOW") {
        showPasswordToggle.textContent = "HIDE";
        passwordField.setAttribute("type", "text");
    } else {
        showPasswordToggle.textContent = "SHOW";
        passwordField.setAttribute("type", "password");
    }


}


usernameField.addEventListener("keyup", (e) => {
    console.log("aperta gostoso", 4444411111111);
    const usernameVal = e.target.value;

    usernameSuccessOutput.style.display = "none";

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = "none";

    if (usernameVal.length > 0) {
        usernameSuccessOutput.style.display = "block";
        usernameSuccessOutput.textContent = `Checking ${usernameVal}`; ;
        fetch("/authentication/validate-username/", {
            body: JSON.stringify({ username: usernameVal }),
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            usernameSuccessOutput.style.display = "none";
            if (data.username_error) {
                submitBtn.disabled = true;
                usernameField.classList.add("is-invalid");
                feedbackArea.style.display = "block";
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
            } else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }

    console.log('usernameVal', usernameVal);
});

emailField.addEventListener("keyup", (e) => {
    console.log("aperta gostoso", 4444411111111);
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch("/authentication/validate-email/", {
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.email_error) {
                    submitBtn.disabled = true;
                emailField.classList.add("is-invalid");
                emailFeedBackArea.style.display = "block";
                emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
            } else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }

    console.log('emailVal', emailVal);
});