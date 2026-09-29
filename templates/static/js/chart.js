// ==========================================
// Water Consumption Dashboard Charts
// Chart.js
// ==========================================

// ---------- Monthly Water Consumption ----------
const monthlyCanvas = document.getElementById("monthlyChart");

if (monthlyCanvas) {

    new Chart(monthlyCanvas, {

        type: "bar",

        data: {

            labels: monthlyLabels,

            datasets: [{

                label: "Average Water Consumption",

                data: monthlyValues,

                backgroundColor: [
                    "#42A5F5",
                    "#5C6BC0",
                    "#26A69A",
                    "#66BB6A",
                    "#FFA726",
                    "#EF5350",
                    "#AB47BC",
                    "#29B6F6",
                    "#26C6DA",
                    "#9CCC65",
                    "#FFCA28",
                    "#EC407A"
                ],

                borderRadius: 12

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                y: {

                    beginAtZero: true

                }

            }

        }

    });

}

// ---------- Temperature Chart ----------
const tempCanvas = document.getElementById("tempChart");

if (tempCanvas) {

    new Chart(tempCanvas, {

        type: "line",

        data: {

            labels: tempLabels,

            datasets: [{

                label: "Water Consumption",

                data: tempValues,

                borderColor: "#1565C0",

                backgroundColor: "rgba(21,101,192,0.15)",

                fill: true,

                tension: 0.4,

                pointRadius: 3

            }]

        },

        options: {

            responsive: true

        }

    });

}

// ---------- Rainfall Chart ----------
const rainCanvas = document.getElementById("rainChart");

if (rainCanvas) {

    new Chart(rainCanvas, {

        type: "line",

        data: {

            labels: rainLabels,

            datasets: [{

                label: "Rainfall Effect",

                data: rainValues,

                borderColor: "#00ACC1",

                backgroundColor: "rgba(0,172,193,0.25)",

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true

        }

    });

}

// ---------- Pie Chart ----------
const pieCanvas = document.getElementById("pieChart");

if (pieCanvas) {

    new Chart(pieCanvas, {

        type: "pie",

        data: {

            labels: pieLabels,

            datasets: [{

                data: pieValues,

                backgroundColor: [

                    "#42A5F5",

                    "#66BB6A",

                    "#FFA726",

                    "#AB47BC"

                ]

            }]

        },

        options: {

            responsive: true

        }

    });

}