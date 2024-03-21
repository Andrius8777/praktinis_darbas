
document.addEventListener('DOMContentLoaded', function () {
    const makeSelect = document.getElementById('id_make');
    const modelSelect = document.getElementById('id_model');

    const modelsByMake = {
        'Audi': ['A1', 'A2', 'A3', 'A5', 'A6', 'A7', 'A8', 'S4', 'S6', 'S7','S8', 'RS4', 'RS5', 'RS6', 'RS7', 'Q1', 'Q3', 'Q5', 'Q7', 'Q8' ],  
        'BMW': ['1 Series', '2 Series', '3 Series', '4 Series', '5 Series', '6 Series', '7 Series', '8 Series', 'X1', 'X3', 'X5', 'X6', 'X7', 'X8', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8'],  
        'Mercedes': ['A-Class', 'C-Class', 'E-Class', 'S-Class', 'GLA', 'GLC', 'GLE', 'GLS'],
        'VW': ['Golf', 'Polo', 'Passat', 'Tiguan', 'T-Roc', 'Touareg'],
        'Volvo': ['S60', 'S90', 'V60', 'V90', 'XC40', 'XC60', 'XC90'],
        'Peugeot': ['108', '208', '308', '508', '2008', '3008', '5008'],
        'Lexus': ['CT', 'IS', 'ES', 'GS', 'NX', 'RX', 'RX', 'UX'],
        'Skoda': ['Fabia', 'Octavia', 'Superb', 'Kodiaq', 'Karoq'],
        'Renault': ['Clio', 'Megane', 'Scenic', 'Captur', 'Kadjar'],
        'Citroen': ['C1', 'C3', 'C4', 'C5', 'Berlingo'],
        'Fiat': ['500', 'Panda', 'Tipo', '500L', '500X'],
        'Toyota': ['Yaris', 'Corolla', 'Camry', 'RAV4', 'Highlander'],
        'Ford': ['Fiesta', 'Focus', 'Mondeo', 'Kuga', 'Edge'],
        'Opel': ['Corsa', 'Astra', 'Insignia', 'Crossland X', 'Grandland X'],
        'Porsche': ['911', 'Cayenne', 'Panamera', 'Macan', 'Taycan'],
    };

    function updateModelOptions() {
        const selectedMake = makeSelect.value;
        modelSelect.innerHTML = ''; 

        modelsByMake[selectedMake].forEach(model => {
            const option = document.createElement('option');
            option.textContent = model;
            option.value = model;
            modelSelect.appendChild(option);
        });
    }


    makeSelect.addEventListener('change', updateModelOptions);

    updateModelOptions();
});
