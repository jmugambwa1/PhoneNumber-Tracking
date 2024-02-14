# Phone Number Tracking

This is a phone number tracking application built using Python. It allows users to input a phone number in the `myphone.py` module, which then utilizes the `phonenumbers` and `opencage` libraries to determine the country location and service provider associated with the phone number. Additionally, it generates an HTML file using `folium` library, which when opened, displays the location on Google Maps.

## Features

- Track phone numbers to determine the country location and service provider.
- Display the location on Google Maps via an HTML file.

## Requirements

- Python 3.x
- folium
- phonenumbers
- opencage

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/jmugambwa1/PhoneNumber-Tracking.git
    ```

2. Navigate to the project directory:

    ```bash
    cd PhoneNumber-Tracking
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `myphone.py` file.
2. Enter the phone number you want to track in the specified variable.
3. Run the `myphone.py` module.
4. The country location and service provider associated with the phone number will be displayed.
5. An HTML file will be generated in the `html` folder, which you can open to view the location on Google Maps.

## File Structure

- `myphone.py`: Contains the main Python script for phone number tracking.
- `html/`: Folder containing the generated HTML file.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to the developers of folium, phonenumbers, and opencage libraries for providing the tools necessary to build this application.
- Inspiration for this project came from the need for a simple phone number tracking tool.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## Author

Joel Mugambwa(https://github.com/jmugambwa1)
