import SearchForm from './components/search/search'
import Result from './components/results/Result'
import Add from './components/add/Add'
import { getAllUsers } from './data/user_service'
import { useEffect, useState } from 'react'
import { userInterface } from './interfaces'

function App() {

  const [userList, setUserList] = useState<userInterface[]>()

  useEffect(() => {
    getAllUsers().then((users) => setUserList(users))

  }, [])

  return (
    <div className='container mx-auto my-xl'>
      <h1 className='text-3xl font-bold title flex justify-center items-center mx-auto'>
        Task App</h1>
      <div className='flex justify-around'>
        Tasks
        <Add></Add>
      </div>
      <div>
        <SearchForm></SearchForm>
      </div>
      <div>
        {
          userList && <Result users={userList}  ></Result>
        }
      </div>
    </div>
  )
}

export default App
