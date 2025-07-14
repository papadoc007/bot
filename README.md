# LeakGuard Proxy

Proxy server for LeaksAPI using Express.js

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env` file with your RapidAPI key:
```env
RAPIDAPI_KEY=your_rapidapi_key_here
```

3. Run the server:
```bash
npm start
```

## Usage

The proxy will be available at:
- Local: `http://localhost:3000`
- Render: `https://your-app-name.onrender.com`

### API Endpoint

`GET /leaks/:email`

Example:
```
GET /leaks/testemail@gmail.com
```

## Environment Variables

- `RAPIDAPI_KEY`: Your RapidAPI key for LeaksAPI
- `PORT`: Server port (default: 3000) 