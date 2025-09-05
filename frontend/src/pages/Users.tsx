import DataTable from "../components/DataTable";

const Users = () => {
  return (
    <div>
      <h1>Users</h1>
      <button>Add User</button>
      <button>Delete User</button>
      <DataTable caption="Users">
        <thead>
          <tr>
            <th>Display Name</th>
            <th>UPN</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>User One</td>
            <td>user1@contoso.com</td>
          </tr>
        </tbody>
      </DataTable>
    </div>
  )
}

export default Users
