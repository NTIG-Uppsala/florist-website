
// Denna sektionen är för Kiruna!
// Allt som ska ändras här är nummer. Symbolerna måste vara på samma ställe då dessa separerar de olika nummerna.
let openHoursKiruna = [];
let openHoursLulea = [];

async function requestJsonKirunaAndFormat() {
    let data;
    try {
        const response = await fetch(`https://sheets.googleapis.com/v4/spreadsheets/1UPl5omRAHA6uMnlC--p_tKvYLEYgyrpn7ZJjtdvupoI/values/B11:C17?key=AIzaSyAEcN2gPi9-UMllfIveKJydPZTrmKjJFKY`);
        data = await response.json();
    } catch (e) {
        console.error("Error: " + e);
    }

    try {
        openHoursKiruna = [
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])],
            [parseInt(data.values[0][0]), parseInt(data.values[0][1])],
            [parseInt(data.values[1][0]), parseInt(data.values[1][1])],
            [parseInt(data.values[2][0]), parseInt(data.values[2][1])],
            [parseInt(data.values[3][0]), parseInt(data.values[3][1])],
            [parseInt(data.values[4][0]), parseInt(data.values[4][1])],
            [parseInt(data.values[5][0]), parseInt(data.values[5][1])],
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])]
        ]
        setTimesStatic('kiruna');
    } catch (e) {
        console.error("Error formatting. Make sure no letters or signs are entered.");
    }
}

async function requestJsonLuleaAndFormat() {
    let data;
    try {
        const response = await fetch(`https://sheets.googleapis.com/v4/spreadsheets/1UPl5omRAHA6uMnlC--p_tKvYLEYgyrpn7ZJjtdvupoI/values/B21:C27?key=AIzaSyAEcN2gPi9-UMllfIveKJydPZTrmKjJFKY`);
        data = await response.json();
    } catch (e) {
        console.error("Error: " + e);
    }
    
    try {
        openHoursLulea = [
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])],
            [parseInt(data.values[0][0]), parseInt(data.values[0][1])],
            [parseInt(data.values[1][0]), parseInt(data.values[1][1])],
            [parseInt(data.values[2][0]), parseInt(data.values[2][1])],
            [parseInt(data.values[3][0]), parseInt(data.values[3][1])],
            [parseInt(data.values[4][0]), parseInt(data.values[4][1])],
            [parseInt(data.values[5][0]), parseInt(data.values[5][1])],
            [parseInt(data.values[6][0]), parseInt(data.values[6][1])]
        ]
        setTimesStatic('lulea');
    } catch (e) {
        console.error("Error formatting. Make sure no letters or signs are entered.");
    }
}