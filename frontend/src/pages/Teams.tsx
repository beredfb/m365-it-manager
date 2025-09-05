import DataTable from "../components/DataTable";

const Teams = () => {
  return (
    <div>
      <h1>Teams Active Users (Last 7 Days)</h1>
      <DataTable caption="Active Users">
        <thead>
          <tr>
            <th>Display Name</th>
            <th>Last Activity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>User One</td>
            <td>2023-10-27</td>
          </tr>
        </tbody>
      </DataTable>
    </div>
  )
}

export default Teams;
