$(document).ready(function() {
    $('tbody tr').on('click', function() {
        const flight = $(this).find('td:nth-child(2)').text();
        const from = $(this).find('td:nth-child(3)').text();
        const to = $(this).find('td:nth-child(4)').text();
        const price = $(this).find('td:nth-child(7)').text();
        
        alert(`Flight Details:\nFlight: ${flight}\nFrom: ${from}\nTo: ${to}\nPrice: ${price}`);
    });

    $('th').on('click', function() {
        const table = $(this).parents('table').eq(0);
        const rows = table.find('tr:gt(0)').toArray().sort(comparator($(this).index()));
        this.asc = !this.asc;
        if (!this.asc) {
            rows.reverse();
        }
        for (let i = 0; i < rows.length; i++) {
            table.append(rows[i]);
        }
    });

    function comparator(index) {
        return function(a, b) {
            const valA = getCellValue(a, index);
            const valB = getCellValue(b, index);
            return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB);
        };
    }

    function getCellValue(row, index) {
        return $(row).children('td').eq(index).text();
    }

    $('#search-input').on('keyup', function() {
        const value = $(this).val().toLowerCase();
        $('tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });
}); 
