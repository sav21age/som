(function () {
  "use strict";

  let forms = document.querySelectorAll(".callback-form");

  forms.forEach(function (e) {
    e.addEventListener("submit", function (event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute("action");
      //   let recaptcha = thisForm.getAttribute("data-recaptcha-site-key");
      let recaptcha = "6LeC_CAlAAAAAIiz1GO3IxByn5TsM3kM4OtgAH_l";

      if (!action) {
        displayError(thisForm, "The form action property is not set!");
        return;
      }
      // thisForm.querySelector(".overlay").style.removeProperty('display');
      // thisForm.querySelector(".overlay").style.display = 'block';
      thisForm
        .querySelector(".overlay")
        .classList.add(
          "d-flex",
          "align-items-center",
          "justify-content-center"
        );
      thisForm.querySelector(".loading").classList.remove("d-none");
      // thisForm.querySelector(".error-message").classList.remove("d-block");
      // thisForm.querySelector(".sent-message").classList.remove("d-block");

      let formData = new FormData(thisForm);

      if (recaptcha) {
        if (typeof grecaptcha !== "undefined") {
          grecaptcha.ready(function () {
            try {
              grecaptcha
                .execute(recaptcha, { action: "php_email_form_submit" })
                .then((token) => {
                  formData.set("recaptcha-response", token);
                  php_email_form_submit(thisForm, action, formData);
                });
            } catch (error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(
            thisForm,
            "The reCaptcha javascript API url is not loaded!"
          );
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
    fetch(action, {
      method: "POST",
      body: formData,
      headers: { "X-Requested-With": "XMLHttpRequest" },
    })
      .then((response) => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error(
            `${response.status} ${response.statusText} ${response.url}`
          );
        }
      })
      .then((data) => {
        thisForm.querySelector(".loading").classList.add("d-none");
        if (data.trim() == "OK") {
          thisForm.querySelector(".sent-message").classList.remove("d-none");
          setTimeout(function () {
            thisForm
              .querySelector(".overlay")
              .classList.remove(
                "d-flex",
                "align-items-center",
                "justify-content-center"
              );
            thisForm.querySelector(".overlay").classList.add("d-none");
            thisForm.reset();
          }, 7000);
        } else {
          throw new Error(
            data
              ? data
              : "Form submission failed and no error message returned from: " +
                action
          );
        }
      })
      .catch((error) => {
        displayError(thisForm, error);
      });
  }

  function displayError(thisForm, error) {
    thisForm.querySelector(".loading").classList.add("d-none");
    thisForm.querySelector(".error-message").innerHTML = error;
    thisForm.querySelector(".error-message").classList.remove("d-none");
    // thisForm.querySelector(".loading").classList.remove("d-block");
    // thisForm.querySelector(".error-message").innerHTML = error;
    // thisForm.querySelector(".error-message").classList.add("d-block");
  }
})();
