import { useState } from "react"
import { createUser } from "../../data/user_service";

function Add() {
    const [isOpen, setIsOpen] = useState(false)
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');

    function handleFirstNameChange(e) {
        setFirstName(e.target.value);
    }

    function handleLastNameChange(e) {
        setLastName(e.target.value);
    }

    function handlePhoneNumberChange(e) {
        setPhoneNumber(e.target.value);
    }

    function handleSubmit(e) {
        e.preventDefault();
        const newUser = {
            "first_name": firstName,
            "last_name": lastName,
            "phone_number": phoneNumber
        }
        const data = createUser(newUser)
        handleClose()
    }
    function handleOnClick() {
        setIsOpen(true)
    }

    function handleClose() {
        setIsOpen(false)
    }
    return (
        <>
            <button onClick={handleOnClick}
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                + Add Contact
            </button>
            {isOpen === true &&
                <div className="fixed z-10 inset-0 overflow-y-auto">
                    <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
                        <div className="fixed inset-0 transition-opacity" aria-hidden="true">
                            <div onClick={handleClose} className="absolute inset-0 bg-gray-500 opacity-75"></div>
                        </div>
                        <span className="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">
                            &#8203;
                        </span>
                        <div className="px-6 py-6 lg:px-8 inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
                            <h3 className="mb-4 text-xl font-medium text-gray-900 dark:text-white text-center">Add A New User</h3>
                            <form onSubmit={handleSubmit} className="space-y-6">
                                <div>
                                    <label htmlFor="first-name" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First Name:</label>
                                    <input
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                        type="text"
                                        id="first-name"
                                        name="first-name"
                                        value={firstName}
                                        onChange={handleFirstNameChange}
                                        required
                                    />
                                </div>
                                <div>
                                    <label htmlFor="last-name" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last Name:</label>
                                    <input
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                        type="text"
                                        id="last-name"
                                        name="last-name"
                                        value={lastName}
                                        onChange={handleLastNameChange}
                                        required
                                    />
                                </div>
                                <div>
                                    <label htmlFor="phone-number" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Phone Number:</label>
                                    <input
                                    className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                        type="tel"
                                        id="phone-number"
                                        name="phone-number"
                                        value={phoneNumber}
                                        onChange={handlePhoneNumberChange}
                                        required
                                    />
                                </div>
                                <div className="flex justify-between">
                                    <button type="submit" className="flex-shrink-0 bg-blue-500 hover:bg-blue-700 border-blue-500 hover:border-blue-700 text-sm border-4 text-white px-2 py-1 rounded">Add User</button>
                                    <button type="button" onClick={handleClose} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                                        Cancel
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            }
        </>


    )
}

export default Add