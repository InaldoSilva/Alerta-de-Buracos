const exp = require("constants");
const express =  require("express");

const app = express("dotenv").config();

const port = proccess.env.PORT || 3000;

app.listen(port, () => {
    console.log(`O servidor está rodando na porta ${port}`);
});