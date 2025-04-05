<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form Popup</title>
    <style>
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #87CEEB;
            overflow: hidden;
        }
        /* login text style */
        .login-text{
            font-size: 24px;
            color: #007bff;
            cursor: pointer;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            transition: opacity 1s ease; /* slow opacity transition for login text */
        }
        /* login container style (hidden by default) */
        .login-container{
            position: absolute;
            width: 300px;
            height: 300px;
            padding: 20px;
            background: #DAA520;
            box-shadow: 0 4px 8px rgba(0, 0,0,0.2);
            border-radius: 10px;
            opacity: 0;
            pointer-events: none;/* prevent intersection initially */
            transform: scale(0.8);
            transition: opacity 1s ease, transform 1s ease, pointer-events 0s 1s;
            /* smooth transition  */
        }
        /* when mouse leaves the login-container, it disappears */
        .login-container:hover{
            opacity: 0;
        }
        /* when hovering on login text, the login container pops up */
        .login-text:hover + .login-container{
            opacity: 1;
            pointer-events: auto;
            /* enable intersection with login container: ; */
            transform: scale(1);
            /* scale to normal size */
        }
        /* when mouse leaves the login-container, it disappears */
        .login-container:hover{
            opacity: 1;
            pointer-events: auto;
            transform: scale(1);
        }
        .login-container{
            transition: opacity 1s ease, transform 1s ease, pointer-events 0s 1s;
        }
        /* input and button animations */
        .input-group, .login-btn {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1s ease, transform 1s ease;
            /* slower transition for input and button */
        }
        .login-container:hover .input-group,
        .login-container:hover .login-btn{
            opacity: 1;
            transform: translateY(0);
        }
        h2{
            margin-bottom: 20px;
            text-align: center;
        }
        input-group{
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }
        .input-group input{
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .login-btn{
            margin: auto;
            margin-top: 5px;
            display: block;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .login-btn:hover{
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <!-- login text -->
    <div class="login-text">Login</div>
    <!-- login form container (initially hidden -->
     <div class="login-container">
        <!-- username -->
        <h2>Login</h2>
        <div class="input-group">
            <label for="username">Username</label>
            <input type="text" id="username" placeholder="PIYUSH">
        </div>
        <!-- login password -->
        <div class="input-group">
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="PIYUSHRDX">
        </div>
        <!-- button login -->
        <button class="login-btn">Login</button>
     </div>
</body>
</html>