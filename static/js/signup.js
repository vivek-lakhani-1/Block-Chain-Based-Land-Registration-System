document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.querySelector("form");
  const emailPhoneInput = document.querySelector('input[name="emphn"]');
  const passwordInput = document.querySelector('input[name="password"]');
  const rememberMeCheckbox = document.querySelector(".toggle");

  const connectButton = document.getElementById("connectButton");
connectButton.addEventListener("click", async () => {
  try {
    await window.ethereum.request({ method: "eth_requestAccounts" });
    console.log("Connected to MetaMask");
    const web3 = new Web3(window.ethereum);
    const accounts = await web3.eth.getAccounts();
    console.log("Connected account:", accounts[0]);
    const message = "We Are Verifing Your Identity and Wallet Address.";
    const signature = await web3.eth.personal.sign(message, accounts[0]);
    console.log("Digital signature:", signature);
    var url = "http://127.0.0.1:8000/register/wallet_address";
    var xhr = new XMLHttpRequest();
    
  
    var queryParams = "data="+accounts[0]+"|||"+signature; // Replace with your specific data
    
    // Append the query parameters to the URL
    url = url + '?' + queryParams;
    
    xhr.open('GET', url, true);
    
    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4 && xhr.status == 200) {
        var response = xhr.responseText;
        
        if(response === '{"status":200,"message":"Working"}'){
          sessionStorage.setItem('wallet', accounts[0]);
          window.location.href = "/register/register_metamask"
        }
        else{
          sessionStorage.setItem('wallet', accounts[0]);
          window.location.href = "/user/dashboard"
        }
              
      }
    };
    
    xhr.send();

    
  } catch (error) {
    console.error("Error connecting to MetaMask:", error);
  }

});

  // Retrieve stored login data from localStorage (use the correct key "loginData")
  const storedLoginData = JSON.parse(localStorage.getItem("loginData")) || {};

  // Populate the form fields if "Remember me" is checked and data is available
  if (rememberMeCheckbox.checked && storedLoginData.emailPhone && storedLoginData.password) {
    emailPhoneInput.value = storedLoginData.emailPhone;
    passwordInput.value = storedLoginData.password;
  }

  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const emailPhone = emailPhoneInput.value;
    const password = passwordInput.value;

    if (emailPhone === "" || password === "") {
      alert("Please fill in all fields");
    } else {
      // Validation logic (you can add additional validation if needed)

      // If "Remember me" is checked, store the data in local storage
      if (rememberMeCheckbox.checked) {
        localStorage.setItem(
          "loginData",
          JSON.stringify({ emailPhone, password })
        );
      } else {
        // If "Remember me" is not checked, remove the stored data
        localStorage.removeItem("loginData");
      }

      // Clear the form fields
      emailPhoneInput.value = "";
      passwordInput.value = "";

      alert("Logged in successfully!\n\nEmail/Phone: " + emailPhone);
      window.location.href = "./index.html"
    }
  });
});
