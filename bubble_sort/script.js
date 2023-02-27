/* 
How to use:
    "node bubble_sort/script.js" while in the repo folder
*/

/**
 * Does a series of passes (max array length) comparing adjacent elements until all elements are in order
 * @param {*} array an array of numbers, can be negative
 */
function bubbleSort(array) {

    const lastIndex = array.length - 1
    let totalIterations = 0
    let hasSwapped = true
    let i = 0

    while (hasSwapped) {
        hasSwapped = false

        console.log(`Pass ${i + 1}:`)

        for (let j = 0; j < lastIndex - i; j++) {
            totalIterations += 1

            const val1 = array[j],
            val2 = array[j + 1]

            if (val1 < val2) continue
            console.log(`   Swapped ${val1} at ${j} with ${val2} at ${j + 1}`)
            // i1 is greater than i2, swap

            array[j] = val2
            array[j + 1] = val1
            hasSwapped = true
        }

        i += 1
    }

    console.log('Result:')
    console.log('   Total iterations', totalIterations)
    console.log('   Slowest possible', array.length * (lastIndex) / 2)
    console.log('   Sorted array', array)
}

bubbleSort([6, 2, 1, 8, -10, 6, 100, 4, -4, -12])