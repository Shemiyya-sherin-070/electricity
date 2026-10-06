const API_URL =
    "http://127.0.0.1:8000/api/calculate-bill/";
const calculateBtn =
    document.getElementById("calculateBtn");
const loading =
    document.getElementById("loading");
const errorMessage =
    document.getElementById("errorMessage");
const billResult =
    document.getElementById("billResult");
calculateBtn.addEventListener("click", calculateBill);
async function calculateBill() {
    const customerName =
        document.getElementById("customerName").value.trim();
    const units =
        document.getElementById("units").value;
    
    errorMessage.classList.add("d-none");
    billResult.classList.add("d-none");
    
    if (!customerName) {
        showError("Please enter customer name.");
        return;
    }
    if (units === "") {
        showError("Please enter electricity units.");
        return;
    }
    if (Number(units) < 0) {
        showError("Units cannot be negative.");
        return;
    }
    // Show loading
    loading.classList.remove("d-none");
    calculateBtn.disabled = true;
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                customer_name: customerName,
                units: units
            })
        });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(
                data.message || "Unable to calculate bill."
            );
        }
        displayBill(data.bill);
    } catch (error) {
        showError(error.message);
    } finally {
        loading.classList.add("d-none");
        calculateBtn.disabled = false;
    }
}
function displayBill(bill) {
    document.getElementById("resultCustomer").textContent = bill.customer_name;
    document.getElementById("resultUnits").textContent = bill.units;
    document.getElementById("energyCharge").textContent = "₹ " + bill.energy_charge;
    document.getElementById("fixedCharge").textContent = "₹ " + bill.fixed_charge;
    document.getElementById("subtotal").textContent = "₹ " + bill.subtotal;
    document.getElementById("tax").textContent = "₹ " + bill.tax;
    document.getElementById("totalBill").textContent = "₹ " + bill.total_bill;

    const usageMessage =
        document.getElementById("usageMessage");
    usageMessage.textContent = bill.usage_message;
    usageMessage.classList.remove(
        "alert-success",
        "alert-warning",
        "alert-danger"
    );

    if (bill.usage_message === "Low Usage") {
        usageMessage.classList.add("alert-success");
    } else if (bill.usage_message === "Normal Usage") {
        usageMessage.classList.add("alert-warning");
    } else {
        usageMessage.classList.add("alert-danger");
    }
    billResult.classList.remove("d-none");
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove("d-none");
}