import fs from 'fs'
import { validateDocument, ValidationError } from '@byteplug/document'

const specs = {
    type: 'object',
    key: 'string',
    value: {
        type: 'number'
    },
    length: 2
}

const json = fs.readFileSync('./examples.yml', 'utf8')
const document = JSON.parse(json)

try {
    validateDocument(document, specs)
}
catch(err) {
    console.log("The document is not valid")
}