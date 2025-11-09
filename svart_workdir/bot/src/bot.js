// Force puppeteer to store everything to /tmp/
process.env.HOME = "/tmp";

const { delay, handleTargetCreated, handleTargetDestroyed, logMainInfo, logMainError } = require("./utils");
const crypto = require("crypto");
const puppeteer = require("puppeteer");

const APP_ORIGIN = process.env.APP_ORIGIN || "http://web:3000";

// Banner
const tips = ["Every console.log usage on the bot will be sent back to you :)", "There is a small race window (~10ms) when a new tab is opened where console.log won't return output :("];
console.log(`==========\nTips: ${tips[Math.floor(Math.random() * tips.length)]}\n==========`);

// Spawn the bot and navigate to the user provided link.
async function goto(url) {
	logMainInfo("Starting the browser...");
	const browser = await puppeteer.launch({
		headless: "new",
		ignoreHTTPSErrors: true,
		args: [
			"--no-sandbox",
			"--disable-gpu",
			"--disable-jit",
			"--disable-wasm",
			"--disable-dev-shm-usage",
			// `--proxy-pac-url=data:application/x-ns-proxy-autoconfig;base64,${PAC_B64}`,
		],
		executablePath: "/usr/bin/chromium-browser"
	});

	// Hook tabs events
	browser.on("targetcreated", handleTargetCreated.bind(browser));
	browser.on("targetdestroyed", handleTargetDestroyed.bind(browser));

	/* ** CHALLENGE LOGIC ** */
	const ctx = await browser.createBrowserContext();

	logMainInfo("Adding flag cookie...");
	await ctx.setCookie({
		name: "flag",
		value: process.env.FLAG,
		domain: new URL(process.env.APP_ORIGIN).hostname,
		path: "/"
	});

	logMainInfo("Going to the user provided link...");
	page = await ctx.newPage();
	await page.goto(url);
	await delay(20_000);

	logMainInfo("Leaving o/");
	await browser.close();
	return;
}

// Handle TCP data
process.stdin.on("data", (data) => {
	const url = data.toString().trim();

	if (!url || !(url.startsWith("http://") || url.startsWith("https://"))) {
		logMainError("You provided an invalid URL. It should start with http:// or https://.");
		process.exit(1);
	}

	goto(url)
	.then(() => process.exit(0))
	.catch((error) => {
		if (process.env.ENVIRONMENT === "development") {
			console.error(error);
		}
		process.exit(1);
	});
});
