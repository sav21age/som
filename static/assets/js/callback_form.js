(function () {
  "use strict";

  let forms = document.querySelectorAll(".callback-form");

  forms.forEach(function (e) {
    e.addEventListener("submit", function (event) {
      event.preventDefault();

      let thisForm = this;
      let action = thisForm.getAttribute("action");
      let recaptcha = thisForm.getAttribute("data-recaptcha-site-key");

      if (!action) {
        displayError(thisForm, "Не установлен action для формы.");
        return;
      }
      thisForm
        .querySelector(".overlay")
        .classList.add(
          "d-flex",
          "align-items-center",
          "justify-content-center"
        );
      thisForm.querySelector(".loading").classList.remove("d-none");

      let formData = new FormData(thisForm);

      if (recaptcha) {
        if (typeof grecaptcha !== "undefined") {
          grecaptcha.ready(function () {
            try {
              grecaptcha
                .execute(recaptcha, { action: "form_submit" })
                .then((token) => {
                  formData.set("recaptcha", token);
                  form_submit(thisForm, action, formData);
                });
            } catch (error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(
            thisForm,
            "Не загружено reCaptcha javascript API."
          );
        }
      } else {
        form_submit(thisForm, action, formData);
      }



      // form_submit(thisForm, action, formData);
    });
  });

  function form_submit(thisForm, action, formData) {
    fetch(action, {
      method: "POST",
      body: formData,
      headers: { "X-Requested-With": "XMLHttpRequest" },
    })
      .then((response) => {
        return response.json();
        // if (response.ok) {
        //   return response.text();
        // } else {
        //   throw new Error(
        //     // `${response.status} ${response.statusText} ${response.url}`
        //   );
        // }
      })
      .then((data) => {
        thisForm.querySelector(".loading").classList.add("d-none");
        if (data.status == "ok") {
          displayOK(thisForm, data);
        } else {
          throw new Error(data.message);
        }
      })
      .catch((error) => {
        displayError(thisForm, error);
      });
  }

  function displayOK(thisForm, data) {
    const msg = thisForm.querySelector(".sent-message");
    msg.classList.remove("d-none");
    msg.innerHTML += data.message;
    thisForm.reset();
    // setTimeout(function () {
    //   thisForm
    //     .querySelector(".overlay")
    //     .classList.remove(
    //       "d-flex",
    //       "align-items-center",
    //       "justify-content-center"
    //     );
    //   msg.classList.add("d-none");
    // }, 3000);
  }

  function displayError(thisForm, error) {
    const err = thisForm.querySelector(".error-message");
    err.innerHTML = error.message;
    err.classList.remove("d-none");
  }
})();
