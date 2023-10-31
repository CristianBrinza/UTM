# Adapter Design Pattern

## Introduction
The Adapter pattern allows classes with incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces. This pattern involves a single class called Adapter which joins functionalities of independent or incompatible interfaces. The Adapter pattern allows otherwise incompatible classes to work together by converting the interface of one class into an interface expected by the clients.

In this implementation, the Adapter pattern is used to provide compatibility between our system and a third-party printer service.

## Classes Involved
1. **ThirdPartyPrinter (Class)**: Represents a third-party printer service. This class simulates a printer that our system does not have direct compatibility with.
2. **PrinterAdapter (Class)**: Adapter class that provides compatibility between our system and the `ThirdPartyPrinter`.

## How it works
The `PrinterAdapter` class uses composition to hold an instance of `ThirdPartyPrinter`. When our system wants to print something using the third-party printer, it calls the `requestPrint` method of the `PrinterAdapter`. Internally, this method then delegates the print request to the `executePrintJob` method of the third-party printer.

This approach allows our system to use the third-party printer without any changes to our system's printing method or the third-party printer's method.

## Conclusion
The Adapter pattern provides a solution to integrate classes with incompatible interfaces. In our context, it allows our system to use a third-party printer service without modifying the existing code of either our system or the third-party printer.
