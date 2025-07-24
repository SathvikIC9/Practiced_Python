document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("askForm");
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        document.getElementById("waitMsg").innerText = "Let me think... 🤔";
        document.getElementById("answer").innerText = "";

        const userInput = document.getElementById("value").value;

        setTimeout(() => {
            fetch("/answer", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: new URLSearchParams({
                    value: "your input"
                })
            })

                .then((res) => res.json())
                .then((data) => {
                    document.getElementById("waitMsg").innerText = "";
                    document.getElementById("answer").innerText = data.reply;
                });
        }, 2000);
    });
});
