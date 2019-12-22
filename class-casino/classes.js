class Deck {
    constructor() {
      this.suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
      this.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
      this.faces = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10", "Jack": "10", "Queen": "10", "King": "10", "Ace": "11"}
      this.deck = []
      // this.faces.forEach(face => {
      for (const [face, value] of Object.entries(this.faces)) {
        this.suits.forEach(suit => {
          this.deck.push({card: `${face} of ${suit} value: ${("0" + value).slice(-2)}`})
        })
      }
      // console.log({card:`${this.deck.length} ${this.deck}`})
      // console.log(this.deck)
    }
  }
  const myDeck = new Deck()
  console.log(myDeck.deck)