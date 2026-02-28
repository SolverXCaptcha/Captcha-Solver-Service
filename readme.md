# WSSolver - Captcha Solving API
## 🆓 Free Trial


### Get started with **1000 free captcha solves** for testing:

👉 [https://wssolver.net](https://wssolver.net)

<div align="center">
  <img src="https://i.hizliresim.com/8hpunhl.png" alt="WSSolver Banner" width="600">
  
  [![API Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![Response Time](https://img.shields.io/badge/response-<1s-blue.svg)]()
  [![Success Rate](https://img.shields.io/badge/success%20rate-high-brightgreen.svg)]()
</div>

## 🚀 Overview

WSSolver is a high-performance captcha solving service that generates valid tokens for various captcha types including Turnstile and more. Our API provides a simple HTTP interface for seamless integration into your applications.

## ✨ Features

- **⚡ Lightning Fast** - Average response time under 1 second
- **🎯 High Success Rate** - Reliable token generation
- **🔌 Simple Integration** - Clean REST API interface
- **🔧 Multiple Captcha Types** - Support for various captcha systems
- **📦 JSON Responses** - Easy to parse and integrate

## 📖 API Documentation

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `apikey` | string | ✅ | Your API authentication key |
| `sitekey` | string | ✅ | The site key of the captcha |
| `siteurl` | string | ✅ | The URL where the captcha appears |

### Example Request

#### cURL
```bash
curl "https://wssolver.net/solve?apikey=YOUR_KEY&sitekey=0x4&siteurl=https://example.com"
```
