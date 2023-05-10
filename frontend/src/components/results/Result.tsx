import { userInterface } from "../../interfaces";
import { deleteUser } from "../../data/user_service";

type Props = {
    users: userInterface[]
}

function Result({ users }: Props) {
    function handleOnDeleteClick(user: userInterface) {
        deleteUser(user.id)
    }

    return (
        <ul className="divide-y divide-gray-200">
            {
                users.map(user =>
                    <li key={user.id} className="flex py-4">
                        <div className="ml-3">
                            <h3 className="text-sm font-medium text-gray-900">
                                {user.first_name}  {user.last_name}
                            </h3>
                            <p className="text-sm text-gray-500">
                                <i className="fa fa-phone h-10 w-5"
                                    aria-hidden="true" ></i>
                                {user.phone_number}
                            </p>
                        </div>
                        <div className="ml-auto">
                            <button onClick={() => handleOnDeleteClick(user)}
                                className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                                <i className="fas fa-trash-alt mr"></i>
                            </button>
                        </div>
                    </li>
                )
            }
        </ul>
    )
}

export default Result