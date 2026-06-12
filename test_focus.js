const fs = require('fs');

const cssFiles = [
    'void-styles.css',
    'proposta-styles.css',
    'gold-mold/css/styles.css'
];

let allHaveFocusVisible = true;
for (const file of cssFiles) {
    const content = fs.readFileSync(file, 'utf8');
    if (!content.includes(':focus-visible')) {
        console.log(`Missing :focus-visible in ${file}`);
        allHaveFocusVisible = false;
    }
}

if (allHaveFocusVisible) {
    console.log('All CSS files have :focus-visible rules.');
}
