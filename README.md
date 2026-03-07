# 📍 PinLookup API

PinLookup is a simple **Flask-based API** that retrieves **Indian Postal PIN Code information** using the official India Post API.

It allows developers to fetch **Post Office details using a PIN Code**.

---

## 🚀 Features

* 🔎 Lookup Indian PIN Code details
* 📦 Returns Post Office information in JSON format
* ⚡ Fast API built with Flask
* 🌐 CORS enabled for frontend integration
* 🛡 Error handling for invalid PIN codes and server issues

---

## 📂 Project Structure

```
PinLookup
 ├── app.py
 └── README.md
```

---

## ⚙ Installation

Clone the repository:

```
git clone https://github.com/frharsh/PinLookup.git
cd PinLookup
```

Install dependencies:

```
pip install flask flask-cors requests
```

Run the server:

```
python app.py
```

The API will start at:

```
http://127.0.0.1:5000
```

---

## 🔎 Example API Request

```
GET /api/pincode/110001
```

Example URL:

```
http://127.0.0.1:5000/api/pincode/110001
```

---

## 📤 Example Response

```json
{
  "success": true,
  "pincode": "110001",
  "postOffice": [...]
}
```

---

## 🛠 Built With

* Python
* Flask
* Requests
* India Post API

---

## 👨‍💻 Author

Harsh
GitHub: https://github.com/frharsh
