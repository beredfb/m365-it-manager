import DataTable from "../components/DataTable";

const MFA = () => {
  return (
    <div>
      <h1>MFA Status</h1>
      <label>
        <input type="checkbox" />
        Show only disabled
      </label>
      <DataTable caption="MFA Status">
        <thead>
          <tr>
            <th>UPN</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>user1@contoso.com</td>
            <td>Enabled</td>
          </tr>
           <tr>
            <td>user2@contoso.com</td>
            <td>Disabled</td>
          </tr>
        </tbody>
      </DataTable>
    </div>
  )
}

export default MFA;
