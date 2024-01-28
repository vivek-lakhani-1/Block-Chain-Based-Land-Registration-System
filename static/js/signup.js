document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById("signupForm");
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
  
    // Retrieve existing stored data
    const storedData = JSON.parse(localStorage.getItem("signupData")) || {};
  
    // Populate the form fields if "Remember me" is checked
    if (storedData.email && storedData.password && storedData.phonenumber) {
      document.getElementById("email").value = storedData.email;
      document.getElementById("password").value = storedData.password;
      document.getElementById("phonenumber").value = storedData.phonenumber;
    }
  
    signupForm.addEventListener("submit", function (e) {
      
  
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const phonenumber = document.getElementById("phonenumber").value;
  
      // Email validation using a regular expression
      const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  
      if (email === "" || password === "" || phonenumber === "") {
        e.preventDefault();
        alert("Please fill in all fields");
      } else if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
      } else if (phonenumber.length !== 10) {
        alert("Phone number must be exactly 10 digits long");
      } else {
        // If "Remember me" is checked, store the data in local storage
        const rememberMe = document.querySelector(".toggle").checked;
        if (rememberMe) {
          localStorage.setItem(
            "signupData",
            JSON.stringify({ email, password, phonenumber })
          );
        } else {
          // If "Remember me" is not checked, remove the stored data
          localStorage.removeItem("signupData");
        }
        var button = document.getElementById("btn_input");
        button.click();
  
        // Clear the form fields
        document.getElementById("email").value = "";
        document.getElementById("password").value = "";
        document.getElementById("phonenumber").value = "";
  
        // Display the response in an alert
        // alert("Form submitted successfully!\n\nResponse:\nEmail: " + email + "\nPassword: " + password + "\nPhone Number: " + phonenumber);
        // window.location.href = "./l"
      }
    });
  });
  