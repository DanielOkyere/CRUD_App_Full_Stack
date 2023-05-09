import { useState } from "react";

function SearchForm() {
    const [query, setQuery] = useState('');

    function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        event.preventDefault();
    }

    function handleInputChange(event: React.ChangeEvent<HTMLInputElement>) {
        setQuery(event.target.value);
    }

    return (
        <form onSubmit={handleSubmit}>
            <label className="sr-only">Search</label>
            <div className="flex items-center border-b-2 border-blue-500 py-2">
                <input placeholder="Search Name or Phonenumber"
                    value={query}
                    onChange={handleInputChange}
                    type="text" className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" />
            <button className="flex-shrink-0 bg-blue-500 hover:bg-blue-700 border-blue-500 hover:border-blue-700 text-sm border-4 text-white px-2 py-1 rounded">Search</button>
            </div>
        </form>
    )
}

export default SearchForm