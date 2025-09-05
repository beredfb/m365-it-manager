import DataTable from "../components/DataTable";

const Licenses = () => {
  return (
    <div>
      <h1>Licenses</h1>
      <button>Change License</button>
      <DataTable caption="Licenses">
        <thead>
          <tr>
            <th>UPN</th>
            <th>Assigned Licenses</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>user1@contoso.com</td>
            <td>O365 E3</td>
          </tr>
        </tbody>
      </DataTable>
    </div>
  )
}

export default Licenses;
