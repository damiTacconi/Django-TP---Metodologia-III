const btn = document.getElementById('btn-book')
            const closeAlert = (e) => e.parentElement.remove()

            const handleChange = (e) => {
                const totalElement = document.getElementById('total')
                let total = Number(totalElement.innerText)
                const rate = Number(document.getElementById('rate').innerText)
                if (e.checked) {
                    if (total == 0) btn.disabled = false
                    total += rate;
                }
                else {
                    total -= rate;
                    if (total == 0) btn.disabled = true
                }

                totalElement.innerHTML = total
            }