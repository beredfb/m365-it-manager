// A placeholder for a reusable DataTable component powered by shadcn/ui.
// In a real implementation, this would be a generic component.

const DataTable = ({ caption, children }: { caption: string; children: React.ReactNode }) => {
  return (
    <table>
      <caption>{caption}</caption>
      {children}
    </table>
  )
}

export default DataTable
