const crypto = require("crypto");
const express = require("express");
const session = require("express-session");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: false }));

app.use(
  session({
    secret: process.env.SECRET_KEY || crypto.randomBytes(16).toString("hex"), // SECRET_KEY IS FOR LOCAL TESTING, REMOTE WILL ALWAYS BE RANDOM
    resave: false,
    saveUninitialized: true,
    cookie: { sameSite: "STRICT" }
  })
);

app.use("/public", express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  const memo = req.session.memo || "";

  res.send(`
    <html>
      <head>
        <link rel="icon" href='data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" fill="black" /></svg>'>
        <title>SVART BOARD</title>
        <link rel="stylesheet" href="/public/style.css">
      </head>
      <body>
        <h1>SVART BO{</h1>
        <div class="note">(CTRL+S TO SAVE)</div>
        <form id="form" method="POST" action="/save">
          <textarea
            name="memo"
            id="memo"
            placeholder="6 + 7 = ..."
            autocomplete="off"
            autocorrect="off"
            autocapitalize="off"
            spellcheck="false"
          >${memo}</textarea>
        </form>

        <script>
          document.addEventListener("keydown", e => {
            if ((e.ctrlKey || e.metaKey) && e.key.toUpperCase() === "S") {
              e.preventDefault();
              form.submit();
            }
          });
        </script>
      </body>
    </html>
  `);
});

app.post("/save", (req, res) => {
  req.session.memo = req.body.memo || "";
  res.redirect("/");
});

app.listen(PORT, () => console.log(`LISTENING ON PORT ${PORT}`));
