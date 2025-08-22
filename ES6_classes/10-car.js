export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Laisse les sous-classes contrôler l'espèce créée
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Ctor = this.constructor[Symbol.species] || this.constructor;
    // On renvoie une nouvelle instance de la même classe,
    // sans arguments -> propriétés undefined comme dans l'exemple
    return new Ctor();
  }
}
