import type { ReactNode } from "react";

interface Props {
    children: ReactNode;
    onClose: () => void;
}
const Alert = ({children, onClose}: Props) => {
  return (
    //<div className="alert alert-primary" role="alert">{children}</div>
    <div className="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>{children}</strong>
      <button type="button" className="btn-close" data-bs-dismiss="alert" aria-label="Close" onClick={onClose}></button>
    </div>
  )
}

export default Alert