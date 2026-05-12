function lengthOfLastWord (s) {
    const turnIntoArr = s.trim().split(' ')
    const getLastIndex = turnIntoArr.pop()

    return getLastIndex.length
}

const teste1 = lengthOfLastWord("Hello World") // output = 5
const teste2 = lengthOfLastWord("   fly me   to   the moon  ") // output = 4
const teste3 = lengthOfLastWord("luffy is still joyboy") // output = 6

